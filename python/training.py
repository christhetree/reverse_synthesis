import logging
import os
from collections import namedtuple
from typing import List, Union, Set, Tuple, Any

import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.python.keras.utils.data_utils import Sequence
from tqdm import tqdm

from config import OUT_DIR, DATASETS_DIR
from effects import DESC_TO_PARAM, PARAM_TO_EFFECT
from models import build_effect_model, baseline_cnn_2x, baseline_cnn, \
    exposure_cnn, baseline_lstm, baseline_cnn_shallow
from util import parse_save_name

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(level=os.environ.get('LOGLEVEL', 'INFO'))

GPU = 0
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    log.info(f'GPUs available: {physical_devices}')
    tf.config.experimental.set_visible_devices(physical_devices[GPU], 'GPU')
    # tf.config.experimental.set_memory_growth(physical_devices[GPU], enable=True)

YModelData = namedtuple(
    'YModelData',
    'n_bin n_cate cate_names n_cont y_s y_losses metrics'
)

XYMetaData = namedtuple(
    'XYMetaData',
    'data_dir x_dir in_x in_y y_dir y_params y_params_str n_bin n_cate n_cont '
    'descs cate_names y_losses metrics'
)


class TestDataGenerator(Sequence):
    def __init__(self,
                 x_ids: List[Tuple[str, str, str]],
                 x_y_metadata: XYMetaData,
                 batch_size: int = 1,
                 shuffle: bool = True,
                 channel_mode: int = 1) -> None:
        assert len(x_ids) >= batch_size
        assert channel_mode == 1
        assert batch_size == 1

        if shuffle:
            log.info('Shuffling x_ids!')
            np.random.shuffle(x_ids)

        assert channel_mode == -1 or channel_mode == 0 or channel_mode == 1
        if channel_mode == -1:
            log.warning('Data generator is using (b, b) channel mode!')
        elif channel_mode == 0:
            log.info('Data generator is using (x, x) channel mode.')
        else:
            log.info('Data generator is using (x, b) channel mode.')

        self.x_ids = x_ids
        self.x_dir = x_y_metadata.x_dir
        self.in_x = x_y_metadata.in_x
        self.in_y = x_y_metadata.in_y
        self.y_dir = x_y_metadata.y_dir
        self.y_params_str = x_y_metadata.y_params_str
        self.n_bin = x_y_metadata.n_bin
        self.descs = x_y_metadata.descs
        self.n_cont = x_y_metadata.n_cont
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.channel_mode = channel_mode

    def __len__(self) -> int:
        return int(np.floor(len(self.x_ids) / self.batch_size))

    def __getitem__(self, idx: int) -> ((np.ndarray, str, str, str), List[np.ndarray]):
        start_idx = idx * self.batch_size
        end_idx = (idx + 1) * self.batch_size
        batch_x_ids = self.x_ids[start_idx:end_idx]
        x = self._create_x_batch(batch_x_ids)
        y = self._create_y_batch(batch_x_ids)
        return x, y

    def _create_x_batch(self,
                        batch_x_ids: List[Tuple[str, str, str]]) -> Any:
        x = np.empty((self.batch_size, self.in_x, self.in_y, 2),
                     dtype=np.float32)
        render_name = None
        base_render_name = None
        preset = None

        for idx, (x_id, mel_path, base_mel_path) in enumerate(batch_x_ids):
            if self.channel_mode == 1:
                mel_info = np.load(mel_path)
                base_mel_info = np.load(base_mel_path)
                render_name = mel_info['render_name'].item()
                base_render_name = base_mel_info['render_name'].item()
                preset = x_id.split('__')[0]
                mel = mel_info['mel']
                base_mel = base_mel_info['mel']
                x[idx, :, :, 0] = mel
                x[idx, :, :, 1] = base_mel
            elif self.channel_mode == 0:
                mel = np.load(mel_path)['mel']
                x[idx, :, :, 0] = mel
                x[idx, :, :, 1] = mel
            else:
                base_mel = np.load(base_mel_path)['mel']
                x[idx, :, :, 0] = base_mel
                x[idx, :, :, 1] = base_mel

        return x, render_name, base_render_name, preset

    def _create_y_batch(
            self, batch_x_ids: List[Tuple[str, str, str]]) -> List[np.ndarray]:
        y_bin = None
        y_cates = []
        y_cont = None
        if self.n_bin:
            y_bin = np.empty((self.batch_size, self.n_bin), dtype=np.float32)

        for _ in self.descs:
            y_cates.append(np.empty((self.batch_size,), dtype=np.int32))

        if self.n_cont:
            y_cont = np.empty((self.batch_size, self.n_cont), dtype=np.float32)

        for idx, (x_id, _, _) in enumerate(batch_x_ids):
            y_id = f'{x_id}__y_{self.y_params_str}.npz'
            y_data = np.load(os.path.join(self.y_dir, y_id))
            if self.n_bin:
                y_bin[idx] = y_data['binary']

            for desc, y_cate in zip(self.descs, y_cates):
                y_cate[idx] = y_data[desc]

            if self.n_cont:
                y_cont[idx] = y_data['continuous']

        y = []
        if self.n_bin:
            y.append(y_bin)
        y.extend(y_cates)
        if self.n_cont:
            y.append(y_cont)

        return y


def get_effect_names(render_name: str) -> List[str]:
    render_info = parse_save_name(render_name, is_dir=False)
    effect_names = render_info['name'].split('_')
    if 'dry' in effect_names:
        effect_names.remove('dry')

    return effect_names


def get_eval_cnn_spec(gen: TestDataGenerator,
                      save_name: str,
                      max_n: int = 1000) -> None:
    x_s = []
    render_names = []
    base_render_names = []
    presets = []
    for (x, render_name, base_render_name, preset), y in tqdm(gen):
        if len(render_names) >= max_n:
            break

        effect_names = get_effect_names(render_name)
        base_effect_names = get_effect_names(base_render_name)
        if len(base_effect_names) + 1 == len(effect_names):
            x_s.append(x)
            render_names.append(render_name)
            base_render_names.append(base_render_name)
            presets.append(preset)

    assert len(x_s) == len(render_names) == len(base_render_names) == len(presets)
    log.info(f'Length of x_s = {len(x_s)}')
    log.info(f'Saving: {save_name}')
    save_path = os.path.join(OUT_DIR, save_name)
    log.info('converting')
    x_s = np.concatenate(x_s, axis=0)
    log.info(x_s.shape)
    log.info('converting done')
    np.savez(save_path,
             x_s=x_s,
             render_names=render_names,
             base_render_names=base_render_names,
             presets=presets)


class DataGenerator(Sequence):
    def __init__(self,
                 x_ids: List[Tuple[str, str, str]],
                 x_y_metadata: XYMetaData,
                 batch_size: int = 128,
                 shuffle: bool = True,
                 channel_mode: int = 1) -> None:
        assert len(x_ids) >= batch_size

        if shuffle:
            np.random.shuffle(x_ids)

        assert channel_mode == -1 or channel_mode == 0 or channel_mode == 1
        if channel_mode == -1:
            log.warning('Data generator is using (b, b) channel mode!')
        elif channel_mode == 0:
            log.info('Data generator is using (x, x) channel mode.')
        else:
            log.info('Data generator is using (x, b) channel mode.')

        self.x_ids = x_ids
        self.x_dir = x_y_metadata.x_dir
        self.in_x = x_y_metadata.in_x
        self.in_y = x_y_metadata.in_y
        self.y_dir = x_y_metadata.y_dir
        self.y_params_str = x_y_metadata.y_params_str
        self.n_bin = x_y_metadata.n_bin
        self.descs = x_y_metadata.descs
        self.n_cont = x_y_metadata.n_cont
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.channel_mode = channel_mode

    def __len__(self) -> int:
        return int(np.floor(len(self.x_ids) / self.batch_size))

    def __getitem__(self, idx: int) -> (np.ndarray, List[np.ndarray]):
        start_idx = idx * self.batch_size
        end_idx = (idx + 1) * self.batch_size
        batch_x_ids = self.x_ids[start_idx:end_idx]
        x = self._create_x_batch(batch_x_ids)
        y = self._create_y_batch(batch_x_ids)
        return x, y

    def _create_x_batch(self,
                        batch_x_ids: List[Tuple[str, str, str]]) -> np.ndarray:
        x = np.empty((self.batch_size, self.in_x, self.in_y, 2),
                     dtype=np.float32)

        for idx, (_, mel_path, base_mel_path) in enumerate(batch_x_ids):
            if self.channel_mode == 1:
                mel = np.load(mel_path)['mel']
                base_mel = np.load(base_mel_path)['mel']
                x[idx, :, :, 0] = mel
                x[idx, :, :, 1] = base_mel
            elif self.channel_mode == 0:
                mel = np.load(mel_path)['mel']
                x[idx, :, :, 0] = mel
                x[idx, :, :, 1] = mel
            else:
                base_mel = np.load(base_mel_path)['mel']
                x[idx, :, :, 0] = base_mel
                x[idx, :, :, 1] = base_mel

        return x

    def _create_y_batch(
            self, batch_x_ids: List[Tuple[str, str, str]]) -> List[np.ndarray]:
        y_bin = None
        y_cates = []
        y_cont = None
        if self.n_bin:
            y_bin = np.empty((self.batch_size, self.n_bin), dtype=np.float32)

        for _ in self.descs:
            y_cates.append(np.empty((self.batch_size,), dtype=np.int32))

        if self.n_cont:
            y_cont = np.empty((self.batch_size, self.n_cont), dtype=np.float32)

        for idx, (x_id, _, _) in enumerate(batch_x_ids):
            y_id = f'{x_id}__y_{self.y_params_str}.npz'
            y_data = np.load(os.path.join(self.y_dir, y_id))
            if self.n_bin:
                y_bin[idx] = y_data['binary']

            for desc, y_cate in zip(self.descs, y_cates):
                y_cate[idx] = y_data[desc]

            if self.n_cont:
                y_cont[idx] = y_data['continuous']

        y = []
        if self.n_bin:
            y.append(y_bin)
        y.extend(y_cates)
        if self.n_cont:
            y.append(y_cont)

        return y

    def on_epoch_end(self) -> None:
        if self.shuffle:
            np.random.shuffle(self.x_ids)


def train_model(
        model: Model,
        x: Union[np.ndarray, List[np.ndarray]],
        y: Union[np.ndarray, List[np.ndarray]],
        model_name: str,
        batch_size: int = 512,
        epochs: int = 128,
        val_split: float = 0.20,
        patience: int = 8,
        output_dir_path: str = OUT_DIR) -> None:
    save_path = os.path.join(
        output_dir_path,
        # model_name + '_e{epoch:03d}_vl{val_loss:.4f}.h5'
        f'{model_name}__best.h5'
    )
    es = EarlyStopping(monitor='val_loss',
                       min_delta=0,
                       patience=patience,
                       verbose=1)
    cp = ModelCheckpoint(save_path,
                         monitor='val_loss',
                         save_best_only=True,
                         verbose=1)
    model.fit(x,
              y,
              shuffle=True,
              batch_size=batch_size,
              epochs=epochs,
              validation_split=val_split,
              callbacks=[es, cp],
              verbose=1)


def train_model_gen(model: Model,
                    train_gen: DataGenerator,
                    val_gen: DataGenerator,
                    model_name: str,
                    epochs: int = 100,
                    patience: int = 8,
                    output_dir_path: str = OUT_DIR,
                    use_multiprocessing: bool = True,
                    workers: int = 8) -> None:
    save_path = os.path.join(
        output_dir_path,
        # model_name + '_e{epoch:03d}_vl{val_loss:.4f}.h5'
        f'{model_name}__best.h5'
    )
    es = EarlyStopping(monitor='val_loss',
                       min_delta=0,
                       patience=patience,
                       verbose=1)
    cp = ModelCheckpoint(save_path,
                         monitor='val_loss',
                         save_best_only=True,
                         verbose=1)
    model.fit(train_gen,
              validation_data=val_gen,
              epochs=epochs,
              callbacks=[es, cp],
              use_multiprocessing=use_multiprocessing,
              workers=workers,
              verbose=1)


def prepare_y_model_data(y_data_path: str) -> YModelData:
    y_npz_data = np.load(y_data_path)

    n_bin = 0
    n_cate = []
    cate_names = []
    n_cont = 0
    y_s = []
    y_losses = {}
    metrics = {}

    if 'binary_params' in y_npz_data:
        bin_params = y_npz_data['binary_params'].tolist()
        n_bin = len(bin_params)
        y_bin = y_npz_data['binary']
        log.info(f'y_bin shape = {y_bin.shape}')
        assert y_bin.shape[-1] == n_bin
        y_s.append(y_bin)
        y_losses['bin_output'] = 'bce'
        metrics['bin_output'] = 'acc'

    if 'categorical_params' in y_npz_data:
        n_cate = y_npz_data['n_categories'].tolist()
        descs = y_npz_data['param_to_desc'].tolist()

        for n_classes, desc in zip(n_cate, descs):
            y_cate = y_npz_data[desc]
            cate_name = desc.strip().lower().replace(' ', '_')
            log.info(f'{cate_name} n_classes = {n_classes}')
            log.info(f'{cate_name} max = {np.max(y_cate)}')
            log.info(f'{cate_name} min = {np.min(y_cate)}')
            assert 0 <= np.max(y_cate) < n_classes
            assert 0 <= np.min(y_cate) < n_classes
            cate_names.append(cate_name)
            y_s.append(y_cate)
            y_losses[cate_name] = 'sparse_categorical_crossentropy'
            metrics[cate_name] = 'acc'

    if 'continuous_params' in y_npz_data:
        cont_params = y_npz_data['continuous_params'].tolist()
        n_cont = len(cont_params)
        y_cont = y_npz_data['continuous']
        assert y_cont.shape[-1] == n_cont
        log.info(f'y_cont shape = {y_cont.shape}')
        y_s.append(y_cont)
        y_losses['cont_output'] = 'mse'
        metrics['cont_output'] = 'mae'

    log.info(f'y_losses = {y_losses}')
    log.info(f'metrics = {metrics}')

    y_model_data = YModelData(n_bin=n_bin,
                              n_cate=n_cate,
                              cate_names=cate_names,
                              n_cont=n_cont,
                              y_s=y_s,
                              y_losses=y_losses,
                              metrics=metrics)

    return y_model_data


def get_x_y_metadata(data_dir: str,
                     y_params: Set[int]) -> XYMetaData:
    assert os.path.exists(data_dir)
    x_dir = os.path.join(data_dir, 'x')
    assert os.path.exists(x_dir)

    sample_x_name = None
    sample_x_data = None
    for npz_name in os.listdir(x_dir):
        if npz_name.endswith('.npz'):
            sample_x_name = npz_name
            sample_x_data = np.load(os.path.join(x_dir, sample_x_name))
            break
    assert sample_x_name
    assert sample_x_data is not None

    sample_mel_path = sample_x_data['mel_path'].item()
    assert os.path.exists(sample_mel_path)
    sample_mel = np.load(sample_mel_path)['mel']

    log.info(f'Input spectrogram shape = {sample_mel.shape}')
    assert len(sample_mel.shape) == 2
    in_x = sample_mel.shape[0]
    in_y = sample_mel.shape[1]

    sample_base_mel_path = sample_x_data['base_mel_path'].item()
    assert os.path.exists(sample_base_mel_path)
    sample_base_mel = np.load(sample_base_mel_path)['mel']
    assert sample_mel.shape == sample_base_mel.shape

    y_dir = os.path.join(data_dir, 'y')
    assert os.path.exists(y_dir)

    y_params = sorted(list(y_params))
    y_params_str = '_'.join(str(p) for p in y_params)

    sample_y_data = np.load(
        os.path.join(y_dir, f'{sample_x_name}__y_{y_params_str}.npz'))
    n_bin = 0
    n_cont = 0
    descs = []

    for key, values in sample_y_data.items():
        if key == 'binary':
            n_bin = len(values)
        elif key == 'continuous':
            n_cont = len(values)
        else:
            descs.append(key)

    descs = sorted(descs)
    log.info(f'n_bin = {n_bin}')
    log.info(f'descs = {descs}')
    log.info(f'n_cont = {n_cont}')

    n_cate = []
    cate_names = []
    y_losses = {}
    metrics = {}

    if n_bin:
        y_losses['bin_output'] = 'bce'
        metrics['bin_output'] = 'acc'

    for desc in descs:
        param = DESC_TO_PARAM[desc]
        effect = PARAM_TO_EFFECT[param]
        n_cate.append(effect.categorical[param])

        cate_name = desc.strip().lower().replace(' ', '_')
        cate_names.append(cate_name)

        y_losses[cate_name] = 'sparse_categorical_crossentropy'
        metrics[cate_name] = 'acc'

    if n_cont:
        y_losses['cont_output'] = 'mse'
        metrics['cont_output'] = 'mae'

    log.info(f'n_cate = {n_cate}')
    log.info(f'cate_names = {cate_names}')
    log.info(f'y_losses = {y_losses}')
    log.info(f'metrics = {metrics}')

    x_y_metadata = XYMetaData(data_dir=data_dir,
                              x_dir=x_dir,
                              in_x=in_x,
                              in_y=in_y,
                              y_dir=y_dir,
                              y_params=set(y_params),
                              y_params_str=y_params_str,
                              n_bin=n_bin,
                              n_cate=n_cate,
                              n_cont=n_cont,
                              descs=descs,
                              cate_names=cate_names,
                              y_losses=y_losses,
                              metrics=metrics)

    return x_y_metadata


def get_x_ids(data_dir: str,
              val_split: float = 0.10,
              test_split: float = 0.05,
              max_n: int = -1,
              use_cached: bool = True) -> (List[Tuple[str, str, str]],
                                           List[Tuple[str, str, str]],
                                           List[Tuple[str, str, str]]):
    assert val_split + test_split < 1.0
    train_x_ids_path = os.path.join(data_dir, 'train_x_ids.npy')
    val_x_ids_path = os.path.join(data_dir, 'val_x_ids.npy')
    test_x_ids_path = os.path.join(data_dir, 'test_x_ids.npy')

    if use_cached \
        and all(os.path.exists(p)
                for p in [train_x_ids_path, val_x_ids_path, test_x_ids_path]):
        log.info('Using cached x_ids.')
        train_x_ids = np.load(train_x_ids_path)
        val_x_ids = np.load(val_x_ids_path)
        test_x_ids = np.load(test_x_ids_path)
    else:
        log.info('Creating new x_ids.')
        x_dir = os.path.join(data_dir, 'x')
        x_ids = []
        for npz_name in tqdm(os.listdir(x_dir)):
            if not npz_name.endswith('.npz'):
                continue

            npz_data = np.load(os.path.join(x_dir, npz_name))
            mel_path = npz_data['mel_path'].item()
            base_mel_path = npz_data['base_mel_path'].item()
            x_ids.append((npz_name, mel_path, base_mel_path))

        log.info(f'Found {len(x_ids)} data points.')

        np.random.shuffle(x_ids)
        if max_n > 0:
            x_ids = x_ids[:max_n]

        val_idx = int(len(x_ids) * (1.0 - val_split - test_split))
        test_idx = int(len(x_ids) * (1.0 - test_split))

        train_x_ids = x_ids[:val_idx]
        val_x_ids = x_ids[val_idx:test_idx]
        test_x_ids = x_ids[test_idx:]

        log.info('Caching x_ids.')
        np.save(train_x_ids_path, train_x_ids)
        np.save(val_x_ids_path, val_x_ids)
        np.save(test_x_ids_path, test_x_ids)

    return train_x_ids, val_x_ids, test_x_ids


if __name__ == '__main__':
    # effect = 'compressor'
    # params = {270, 271, 272}
    # effect = 'distortion'
    # params = {97, 99}
    # effect = 'eq'
    # params = {89, 91, 93}
    # effect = 'phaser'
    # params = {112, 113, 114}
    effect = 'reverb-hall'
    params = {81, 84, 86}

    # architecture = baseline_cnn
    architecture = baseline_cnn_2x
    # architecture = baseline_cnn_shallow
    # architecture = exposure_cnn
    # architecture = baseline_lstm

    batch_size = 128
    epochs = 100
    val_split = 0.10
    test_split = 0.05
    patience = 8
    used_cached_x_ids = True
    max_n = -1
    channel_mode = 1
    use_multiprocessing = True
    workers = 8
    load_prev_model = False
    # load_prev_model = True

    # presets_cat = 'basic_shapes'
    # presets_cat = 'adv_shapes'
    presets_cat = 'temporal'

    # model_name = f'testing__{effect}__{architecture.__name__}__cm_{channel_mode}'
    model_name = f'seq_5_v3__{presets_cat}__{effect}__{architecture.__name__}' \
                 f'__cm_{channel_mode}'

    datasets_dir = DATASETS_DIR
    # data_dir = os.path.join(datasets_dir, f'testing__{effect}')
    data_dir = os.path.join(datasets_dir, f'seq_5_v3__{presets_cat}__{effect}')
    log.info(f'data_dir = {data_dir}')

    x_y_metadata = get_x_y_metadata(data_dir, params)
    train_x_ids, val_x_ids, test_x_ids = get_x_ids(data_dir,
                                                   val_split=val_split,
                                                   test_split=test_split,
                                                   max_n=max_n,
                                                   use_cached=used_cached_x_ids)
    log.info(f'train_x_ids length = {len(train_x_ids)}')
    log.info(f'val_x_ids length = {len(val_x_ids)}')
    log.info(f'test_x_ids length = {len(test_x_ids)}')
    log.info(f'batch_size = {batch_size}')

    # test_x_ids = test_x_ids[:100]
    spec_gen = TestDataGenerator(test_x_ids,
                                 x_y_metadata,
                                 batch_size=1,
                                 channel_mode=1,
                                 shuffle=True)
    save_name = f'{model_name}__eval_spec_data.npz'
    get_eval_cnn_spec(spec_gen, save_name)
    print('done!')
    exit()

    train_gen = DataGenerator(train_x_ids,
                              x_y_metadata,
                              batch_size=batch_size,
                              channel_mode=channel_mode)
    val_gen = DataGenerator(val_x_ids,
                            x_y_metadata,
                            batch_size=batch_size,
                            channel_mode=channel_mode)

    model = build_effect_model(x_y_metadata.in_x,
                               x_y_metadata.in_y,
                               architecture=architecture,
                               n_bin=x_y_metadata.n_bin,
                               n_cate=x_y_metadata.n_cate,
                               cate_names=x_y_metadata.cate_names,
                               n_cont=x_y_metadata.n_cont)

    if load_prev_model:
        log.info('Loading previous best model.')
        model.load_weights(os.path.join(OUT_DIR, f'{model_name}__best.h5'))

    model.compile(optimizer='adam',
                  loss=x_y_metadata.y_losses,
                  metrics=x_y_metadata.metrics)
    model.summary()

    train_model_gen(model,
                    train_gen,
                    val_gen,
                    model_name,
                    epochs=epochs,
                    patience=patience,
                    use_multiprocessing=use_multiprocessing,
                    workers=workers)
