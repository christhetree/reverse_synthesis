import copy
import hashlib
import logging
import ntpath
import os
from itertools import combinations
from typing import List, Dict, Optional, Any, Set

import librenderman as rm
import numpy as np
import soundfile as sf
import yaml
from tqdm import tqdm

from config import CONFIGS_DIR, RANDOM_GEN_THRESHOLD, MAX_DUPLICATES
from effects import DESC_TO_PARAM, get_effect, PARAM_TO_DESC, param_to_effect
from serum_util import setup_serum, set_preset
from util import get_render_names, generate_exclude_descs, parse_save_name

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(level=os.environ.get('LOGLEVEL', 'INFO'))


class RenderConfig:
    def __init__(self,
                 preset: str,
                 sr: int,
                 note_length: float,
                 render_length: float,
                 midi: int,
                 vel: int,
                 gran: int,
                 n: int = -1,
                 max_n: int = -1,
                 root_dir: Optional[str] = None,
                 exclude_dirs: List[str] = None,
                 effects: List[Dict[str, Any]] = None,
                 use_hashes: bool = False) -> None:
        super().__init__()
        if effects is None:
            effects = []
        if exclude_dirs is None:
            exclude_dirs = []
        self.root_dir = root_dir
        self.exclude_dirs = exclude_dirs
        self.n = n
        self.max_n = max_n
        self.preset = preset
        self.sr = sr
        self.note_length = note_length
        self.render_length = render_length
        self.midi = midi
        self.vel = vel
        self.gran = gran
        self.effects = effects
        self.use_hashes = use_hashes

    def effect_names(self) -> List[str]:
        return sorted(list({e['name'] for e in self.effects}))


class PatchGenerator:
    def __init__(self, rc: RenderConfig) -> None:
        super().__init__()
        self.gran = rc.gran

        n_combos = 1
        params = set()
        effect_names = set()
        param_choices = {}
        param_n_choices = {}
        param_defaults = {}

        if rc.effects is not None:
            for effect_render_data in rc.effects:
                effect_name = effect_render_data['name']
                if effect_name in effect_names:
                    log.warning(f'Duplicate effect "{effect_name}" in config.')
                    continue

                effect_names.add(effect_name)
                effect = get_effect(effect_name)

                for desc, choices in effect_render_data.items():
                    if desc == 'name':
                        continue

                    if desc not in DESC_TO_PARAM:
                        raise KeyError(f'{desc} not a valid param description.')

                    param = DESC_TO_PARAM[desc]
                    params.add(param)
                    default_value = effect.default[param]
                    default = int((default_value * self.gran) + 0.5)
                    param_defaults[param] = default

                    if effect.binary and param in effect.binary:
                        n_choices = 2
                    elif effect.categorical and param in effect.categorical:
                        n_choices = effect.categorical[param]
                    elif effect.continuous and param in effect.continuous:
                        n_choices = rc.gran + 1
                    else:
                        raise KeyError(
                            f'{desc} could not be found in {effect.name}.')

                    len_choices = len(choices)
                    if len_choices > 0:
                        n_combos *= len_choices
                        param_choices[param] = choices
                    else:
                        n_combos *= n_choices
                        param_choices[param] = n_choices

                    param_n_choices[param] = n_choices

        curr_params = sorted(list(params))
        effect_names = sorted(list(effect_names))

        curr_patch = {}
        default_diff = {}
        for param, choices in param_choices.items():
            if type(choices) is list:
                choice = np.random.choice(choices)
            else:
                choice = np.random.randint(0, choices)

            if choice != param_defaults[param]:
                default_diff[param] = choice

            n_choices = param_n_choices[param]
            param_v = float(choice / (n_choices - 1))
            curr_patch[param] = param_v

        self.n_combos = n_combos
        self.params = params
        self.effect_names = effect_names
        self.curr_params = curr_params
        self.param_choices = param_choices
        self.param_n_choices = param_n_choices
        self.param_defaults = param_defaults
        self.default_diff = default_diff
        self.curr_patch = curr_patch
        self.param_n_digits = {k: len(str(v))
                               for k, v in self.param_n_choices.items()}

    def generate_random_patch(
            self,
            n_changes: int = -1
    ) -> (Dict[int, int], Dict[int, float]):
        if n_changes == -1:
            n_changes = len(self.curr_params)

        for param in self.curr_params[:n_changes]:
            choices = self.param_choices[param]
            if type(choices) is list:
                choice = np.random.choice(choices)
            else:
                choice = np.random.randint(0, choices)

            if choice != self.param_defaults[param]:
                self.default_diff[param] = choice
            elif param in self.default_diff:
                del self.default_diff[param]

            n_choices = self.param_n_choices[param]
            param_v = float(choice / (n_choices - 1))
            self.curr_patch[param] = param_v

        if n_changes < len(self.curr_params):
            self.curr_params = self.curr_params[n_changes:] \
                               + self.curr_params[:n_changes]

        return self.default_diff, self.curr_patch

    def _set_patch_rec(
            self,
            params: List[int],
            default_diff: Dict[int, int],
            patch: Dict[int, float]
    ) -> (Dict[int, int], Dict[int, float]):
        if not params:
            yield default_diff, patch
        else:
            param = params[0]
            params = params[1:]

            choices = self.param_choices[param]
            if type(choices) is not list:
                choices = list(range(choices))

            for choice in choices:
                if choice != self.param_defaults[param]:
                    default_diff[param] = choice
                elif param in default_diff:
                    del default_diff[param]

                n_choices = self.param_n_choices[param]
                param_v = float(choice / (n_choices - 1))
                patch[param] = param_v

                yield from self._set_patch_rec(params, default_diff, patch)

    def generate_all_combos(self):
        default_diff = {}
        patch = {}
        yield from self._set_patch_rec(self.curr_params, default_diff, patch)


def generate_render_hash(effect_names: List[str],
                         default_diff: Dict[int, int],
                         param_n_digits: Dict[int, int]) -> str:
    hash_tokens = ['_'.join(effect_names)]

    for effect_name in effect_names:
        effect = get_effect(effect_name)
        for param in effect.order:
            if param in default_diff:
                choice = default_diff[param]
                desc = PARAM_TO_DESC[param]
                n_digits = param_n_digits[param]
                hash_tokens.append(f'{desc}_{choice:0{n_digits}}')

    render_hash = '__'.join(hash_tokens)

    if not render_hash:
        render_hash = 'dry'

    render_hash = f'{render_hash}.wav'
    return render_hash


def render_patch(engine: rm.RenderEngine,
                 patch: Dict[int, float],
                 rc: RenderConfig,
                 save_dir: Optional[str],
                 render_name: Optional[str]) -> np.ndarray:
    set_preset(engine, patch)
    engine.render_patch(rc.midi,
                        rc.vel,
                        rc.note_length,
                        rc.render_length,
                        False)
    audio = np.array(engine.get_audio_frames(), dtype=np.float64)

    save_name = render_name
    if rc.use_hashes:
        render_hash = hashlib.sha1(render_name.encode('utf-8')).hexdigest()
        render_hash = f'{render_hash}.wav'
        save_name = render_hash

    if save_dir and save_name:
        save_path = os.path.join(save_dir, save_name)
        if rc.use_hashes:
            with open(os.path.join(save_dir, 'mapping.txt'), 'a') as mapping_f:
                sf.write(save_path, audio, rc.sr)
                mapping_f.write(f'{save_name}\t{render_name}\n')
        else:
            sf.write(save_path, audio, rc.sr)

    return audio


def _create_save_dir(rc: RenderConfig,
                     create_dirs: bool = True) -> str:
    if not create_dirs:
        assert os.path.exists(rc.root_dir)

    if not os.path.exists(rc.root_dir):
        log.info(f'Making new dir for {rc.root_dir}')
        os.makedirs(rc.root_dir)
    else:
        log.info(f'Root dir {rc.root_dir} already exists.')

    preset_name = os.path.splitext(ntpath.basename(rc.preset))[0]
    int_dir_name = f'{preset_name}__sr_{rc.sr}__nl_{rc.note_length:.2f}__rl_' \
                   f'{rc.render_length:.2f}__vel_{rc.vel:03}__midi_{rc.midi:03}'

    save_dir = os.path.join(rc.root_dir, int_dir_name)
    if not create_dirs:
        assert os.path.exists(save_dir)

    if not os.path.exists(save_dir):
        log.info(f'Making new dir for {int_dir_name}')
        os.makedirs(save_dir)
    else:
        log.info(f'Save dir {int_dir_name} already exists.')

    if not rc.effect_names():
        effect_dir_name = 'dry'
    else:
        effect_dir_name = '_'.join(rc.effect_names())
    effect_dir_name = f'{effect_dir_name}__gran_{rc.gran}'

    save_dir = os.path.join(save_dir, effect_dir_name)
    if not create_dirs:
        assert os.path.exists(save_dir)

    if not os.path.exists(save_dir):
        log.info(f'Making new dir for {effect_dir_name}')
        os.makedirs(save_dir)
    else:
        log.info(f'Save dir {effect_dir_name} already exists.')

    save_dir = os.path.join(save_dir, 'renders')
    if not create_dirs:
        assert os.path.exists(save_dir)

    if create_dirs and not os.path.exists(save_dir):
        log.info('Making new dir for renders.')
        os.makedirs(save_dir)

    return save_dir


def render_audio(rc: RenderConfig,
                 max_duplicates_in_a_row: int = MAX_DUPLICATES) -> None:
    pg = PatchGenerator(rc)
    assert rc.effect_names() == pg.effect_names
    save_dir = _create_save_dir(rc, create_dirs=True)

    render_names = get_render_names(save_dir,
                                    assert_unique=True,
                                    use_hashes=rc.use_hashes)
    n_existing_renders = len(render_names)
    log.info(f'{n_existing_renders} existing renders found.')

    engine = setup_serum(rc.preset, sr=rc.sr, render_once=True)

    log.info(f'{pg.n_combos} no. of possible rendering combos.')
    log.info(f'{pg.effect_names} effects in patch generator.')

    for effect_name in pg.effect_names:
        effect = get_effect(effect_name)
        log.info(f'Setting default {effect.name} params.')
        set_preset(engine, effect.default)

    if rc.n > 0 and RANDOM_GEN_THRESHOLD * rc.n > pg.n_combos:
        log.warning(f'n of {rc.n} is too big, so generating all combos.')
        n_to_render = -1
    else:
        n_to_render = rc.n

    if n_to_render > 0 and 0 < rc.max_n < n_existing_renders + n_to_render:
        n_to_render = max(0, rc.max_n - n_existing_renders)
        log.info(f'n reduced to {n_to_render} due to max n of {rc.max_n}')

    # TODO
    for exclude_dir in rc.exclude_dirs:
        log.info(f'Excluding renders in {exclude_dir}')
        n_existing_renders = len(render_names)
        for render_name in os.listdir(exclude_dir):
            if render_name.endswith('.wav'):
                render_names.add(render_name)

        n_increase = len(render_names) - n_existing_renders
        if n_increase > 0:
            log.info(f'Existing renders increased by {n_increase} to '
                     f'{len(render_names)}')

    if n_to_render == -1:
        pbar = tqdm(total=pg.n_combos)

        for default_diff, patch in pg.generate_all_combos():
            render_name = generate_render_hash(pg.effect_names,
                                               default_diff,
                                               pg.param_n_digits)

            if render_name in render_names:
                log.debug(f'Duplicate render generated: {render_name}')
            else:
                render_patch(engine,
                             patch,
                             rc,
                             save_dir,
                             render_name)

                render_names.add(render_name)

            pbar.update(1)
    else:
        n_rendered = 0
        duplicates_in_a_row = 0
        pbar = tqdm(total=n_to_render)
        while n_rendered < n_to_render:
            default_diff, patch = pg.generate_random_patch()
            render_name = generate_render_hash(pg.effect_names,
                                               default_diff,
                                               pg.param_n_digits)

            if render_name in render_names:
                duplicates_in_a_row += 1
                log.debug(f'Duplicate render generated: {render_name}')

                if duplicates_in_a_row > max_duplicates_in_a_row:
                    log.warning('Too many duplicates generated in a row.')
                    break
            else:
                render_patch(engine,
                             patch,
                             rc,
                             save_dir,
                             render_name)

                render_names.add(render_name)
                n_rendered += 1
                duplicates_in_a_row = 0
                pbar.update(1)


def render_base_audio(orig_rc: RenderConfig,
                      exclude_effects: Set[str] = None,
                      exclude_params: Set[str] = None,
                      use_hashes: bool = False) -> None:
    if exclude_effects is None:
        exclude_effects = set()
    if exclude_params is None:
        exclude_params = set()
    exclude_descs = generate_exclude_descs(exclude_effects, exclude_params)
    log.info(f'Exclude effects = {exclude_effects}')
    log.info(f'Exclude params = {exclude_params}')
    log.info(f'Exclude descs = {exclude_descs}')

    orig_save_dir = _create_save_dir(orig_rc, create_dirs=False)
    log.info(f'Original save dir = {orig_save_dir}')

    orig_render_names = get_render_names(orig_save_dir,
                                         assert_unique=True,
                                         use_hashes=orig_rc.use_hashes)
    log.info(f'{len(orig_render_names)} existing original renders found.')

    rc = RenderConfig(preset=orig_rc.preset,
                      sr=orig_rc.sr,
                      note_length=orig_rc.note_length,
                      render_length=orig_rc.render_length,
                      midi=orig_rc.midi,
                      vel=orig_rc.vel,
                      gran=orig_rc.gran,
                      n=orig_rc.n,
                      max_n=orig_rc.max_n,
                      root_dir=orig_rc.root_dir,
                      effects=copy.deepcopy(orig_rc.effects),
                      use_hashes=use_hashes)

    for desc in exclude_descs:
        for effect in rc.effects:
            if desc in effect:
                del effect[desc]

    rc.effects = list(filter(lambda e: len(e) > 1, rc.effects))
    base_effect_names = rc.effect_names()
    log.info(f'{base_effect_names} effects in base render config.')

    log.info(f'Creating base renders directory.')
    save_dir = _create_save_dir(rc, create_dirs=True)
    log.info(f'Base save dir = {save_dir}')

    base_render_names = get_render_names(save_dir,
                                         assert_unique=True,
                                         use_hashes=rc.use_hashes)
    n_existing_renders = len(base_render_names)
    log.info(f'{n_existing_renders} existing base renders found.')

    engine = setup_serum(rc.preset, sr=rc.sr, render_once=True)

    for effect_name in base_effect_names:
        effect = get_effect(effect_name)
        log.info(f'Setting default {effect.name} params.')
        set_preset(engine, effect.default)

    for orig_render_name in tqdm(orig_render_names):
        render_info = parse_save_name(orig_render_name, is_dir=False)
        rc_effects = {}
        for desc, param_v in render_info.items():
            if desc != 'name' and desc not in exclude_descs:
                param = DESC_TO_PARAM[desc]
                effect_name = param_to_effect[param].name
                if effect_name not in rc_effects:
                    rc_effects[effect_name] = {'name': effect_name}
                rc_effect = rc_effects[effect_name]
                rc_effect[desc] = [param_v]

        rc.effects = list(rc_effects.values())
        pg = PatchGenerator(rc)
        assert pg.n_combos == 1
        assert rc.effect_names() == pg.effect_names

        # Using base effect names is important due to render naming convention
        for effect_name in base_effect_names:
            effect = get_effect(effect_name)
            set_preset(engine, effect.default)

        default_diff, patch = list(pg.generate_all_combos())[0]
        render_name = generate_render_hash(base_effect_names,
                                           default_diff,
                                           pg.param_n_digits)

        if render_name in base_render_names:
            log.debug(f'Duplicate base render generated: {render_name}')
        else:
            render_patch(engine,
                         patch,
                         rc,
                         save_dir,
                         render_name)

            base_render_names.add(render_name)

    log.info(f'{len(base_render_names) - n_existing_renders} new base '
             f'renders rendered.')


if __name__ == '__main__':
    # render_config_path = os.path.join(CONFIGS_DIR, 'rendering/seq_5_train.yaml')
    # with open(render_config_path, 'r') as config_f:
    #     render_config = yaml.full_load(config_f)
    #
    # rc = RenderConfig(**render_config)
    # render_audio(rc)
    # exit()

    all_effects = ['flanger', 'phaser', 'compressor', 'eq', 'distortion']
    all_combos = []
    for n_effects in range(len(all_effects) + 1):
        for combo in combinations(all_effects, n_effects):
            all_combos.append(set(list(combo)))

    all_combos.reverse()

    log.info(f'All exclude combos = {all_combos}')
    log.info(f'Len of exclude combos = {len(all_combos)}')

    render_config_path = os.path.join(CONFIGS_DIR, 'rendering/seq_5_train.yaml')
    with open(render_config_path, 'r') as config_f:
        render_config = yaml.full_load(config_f)

    orig_rc = RenderConfig(**render_config)

    for combo in all_combos:
        if len(combo) > 2:  # TODO
            use_hashes = False
        else:
            use_hashes = True
        exclude_effects = set(combo)
        render_base_audio(orig_rc,
                          exclude_effects=exclude_effects,
                          use_hashes=use_hashes)
    exit()
