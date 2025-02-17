import logging
import ntpath
import os
from collections import defaultdict
from typing import Set, List, DefaultDict

import numpy as np
from tqdm import tqdm

from config import DATASETS_DIR
from effects import PARAM_TO_TYPE, DESC_TO_PARAM, \
    PARAM_TO_EFFECT, PARAM_TO_DESC
from training_util import EFFECT_TO_Y_PARAMS
from util import parse_save_name

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(level=os.environ.get('LOGLEVEL', 'INFO'))


def parse_render_name_for_y(y: DefaultDict[str, List],
                            render_name: str,
                            binary_params: List[int],
                            categorical_params: List[int],
                            continuous_params: List[int],
                            gran: int) -> None:
    render_name_info = parse_save_name(render_name, is_dir=False)
    render_name_params = {}
    for desc, value in render_name_info.items():
        if desc == 'name':
            continue

        param = DESC_TO_PARAM[desc]
        render_name_params[param] = value

    bin_values = []
    for param in binary_params:
        if param in render_name_params:
            bin_values.append(float(render_name_params[param]))
        else:
            effect = PARAM_TO_EFFECT[param]
            bin_values.append(effect.default[param])

    if bin_values:
        y['binary'].append(bin_values)

    for param in categorical_params:
        desc = PARAM_TO_DESC[param]
        if param in render_name_params:
            value = int(render_name_params[param])
        else:
            effect = PARAM_TO_EFFECT[param]
            n_categories = effect.categorical[param]
            value = int((effect.default[param] * n_categories) + 0.5)
        y[desc].append(value)

    cont_values = []
    for param in continuous_params:
        if param in render_name_params:
            cont_values.append(render_name_params[param] / gran)
        else:
            effect = PARAM_TO_EFFECT[param]
            cont_values.append(effect.default[param])

    if cont_values:
        y['continuous'].append(cont_values)


def generate_y(path: str,
               params: Set[int],
               gran: int = 100) -> None:
    assert os.path.isfile(path)

    data_npz_name = os.path.splitext(ntpath.basename(path))[0]

    params = sorted(list(params))
    log.info(f'Calculating y for the following params: {params}')

    param_types = defaultdict(list)
    for param in params:
        param_types[PARAM_TO_TYPE[param]].append(param)
    binary_params = sorted(param_types['binary'])
    categorical_params = sorted(param_types['categorical'])
    continuous_params = sorted(param_types['continuous'])

    log.info(f'Binary params: {binary_params}')
    log.info(f'Categorical params: {categorical_params}')
    log.info(f'Continuous params: {continuous_params}')

    data = np.load(path, allow_pickle=True)
    render_names = data['render_names'].tolist()
    log.info(f'{len(render_names)} renders found in {data_npz_name}')
    y = defaultdict(list)

    for render_name in tqdm(render_names):
        parse_render_name_for_y(y,
                                render_name,
                                binary_params,
                                categorical_params,
                                continuous_params,
                                gran)

    y = dict(y)
    y['gran'] = gran

    log.info('Converting to ndarray.')
    for key in tqdm(y):
        if key == 'binary' or key == 'continuous':
            y[key] = np.array(y[key], dtype=np.float32)
        else:
            y[key] = np.array(y[key], dtype=np.int32)

        log.info(f'{key} ndarray shape: {y[key].shape}')

    n_categories = []
    param_to_desc = []
    for param in categorical_params:
        effect = PARAM_TO_EFFECT[param]
        n_classes = effect.categorical[param]
        desc = PARAM_TO_DESC[param]
        param_to_desc.append(desc)
        n_categories.append(n_classes)

    log.info(f'n_categories = {n_categories}')
    if binary_params:
        y['binary_params'] = np.array(binary_params, dtype=np.int32)
    if categorical_params:
        y['categorical_params'] = np.array(categorical_params, dtype=np.int32)
        y['n_categories'] = np.array(n_categories, dtype=np.int32)
        y['param_to_desc'] = np.array(param_to_desc)
    if continuous_params:
        y['continuous_params'] = np.array(continuous_params, dtype=np.int32)

    save_dir = os.path.split(path)[0]
    save_name = f'{data_npz_name}__y_{"_".join(str(p) for p in params)}.npz'
    save_path = os.path.join(save_dir, save_name)
    log.info(f'Saving as {save_name}')
    np.savez(save_path, **y)


def generate_y_individual(data_dir: str,
                          params: Set[int],
                          gran: int = 100) -> None:
    save_dir = os.path.join(data_dir, 'y')

    if not os.path.exists(save_dir):
        log.info(f'Making new save dir for {save_dir}')
        os.makedirs(save_dir)
    else:
        log.info(f'Save dir {save_dir} already exists.')

    params = sorted(list(params))  # TODO
    log.info(f'Calculating y for the following params: {params}')

    param_types = defaultdict(list)
    for param in params:
        param_types[PARAM_TO_TYPE[param]].append(param)
    binary_params = sorted(param_types['binary'])
    categorical_params = sorted(param_types['categorical'])
    continuous_params = sorted(param_types['continuous'])

    log.info(f'Binary params: {binary_params}')
    log.info(f'Categorical params: {categorical_params}')
    log.info(f'Continuous params: {continuous_params}')

    x_dir = os.path.join(data_dir, 'x')
    for npz_name in tqdm(os.listdir(x_dir)):
        if not npz_name.endswith('.npz'):
            continue

        render_name = np.load(
            os.path.join(x_dir, npz_name))['render_name'].item()
        y = defaultdict(list)
        parse_render_name_for_y(y,
                                render_name,
                                binary_params,
                                categorical_params,
                                continuous_params,
                                gran)
        y = dict(y)
        for key, value in y.items():
            assert len(value) == 1
            if key == 'binary' or key == 'continuous':
                y[key] = np.array(value[0], dtype=np.float32)
            else:
                y[key] = np.array(value, dtype=np.int32)

        save_name = f'{npz_name}__y_{"_".join(str(p) for p in params)}.npz'
        save_path = os.path.join(save_dir, save_name)
        np.savez(save_path, **y)


if __name__ == '__main__':
    gran = 100

    effect = 'compressor'
    # effect = 'distortion'
    # effect = 'eq'
    # effect = 'phaser'
    # effect = 'reverb-hall'
    params = EFFECT_TO_Y_PARAMS[effect]

    presets_cat = 'basic_shapes'
    # presets_cat = 'adv_shapes'
    # presets_cat = 'temporal'

    datasets_dir = DATASETS_DIR

    generate_y_individual(
        # os.path.join(datasets_dir, f'testing__{effect}'), params
        # os.path.join(datasets_dir, f'seq_5_v3__{presets_cat}__{effect}'), params
        os.path.join(datasets_dir, f'seq_5_v3__proc__{presets_cat}__{effect}'), params
    )
