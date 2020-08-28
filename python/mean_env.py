import logging
import os
from typing import Dict, Any

import gym
import numpy as np
from gym.spaces import Box, MultiDiscrete
from stable_baselines3 import PPO, A2C
from stable_baselines3.common import make_vec_env
from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import SubprocVecEnv, DummyVecEnv
import torch as th

# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'DEBUG'))
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
log = logging.getLogger(__name__)


class MeanEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self,
                 target_v: float = 0.5,
                 n_params: int = 3,
                 change_step: float = 0.1,
                 max_ep_steps: int = 50) -> None:
        super().__init__()
        self.n_params = n_params
        self.target_v = target_v
        self.change_step = change_step
        self.max_ep_steps = max_ep_steps
        self.seen_params = set()

        self.curr_step_idx = 0
        self.prev_action = None

        self.action_space = MultiDiscrete([self.n_params, 2])
        self.observation_space = Box(low=0.0,
                                     high=1.0,
                                     shape=(self.n_params,),
                                     dtype=np.float32)
        self.reward_range = (-1.0, 1.0)

        self.curr_v = np.random.uniform(0.0,
                                        1.0,
                                        (self.n_params,)).astype(np.float32)

    def _reward_fn(self, obs: np.ndarray) -> (bool, float):
        mean = np.mean(obs)
        mean_reward = self.target_v - abs(self.target_v - mean)  # TODO

        mid = int(self.n_params / 2)
        n_over = 0
        n_under = 0

        for idx, obs_v in enumerate(obs):
            if idx < mid and obs_v > self.target_v:
                n_over += 1
            if (2 * mid) > idx >= mid and obs_v <= self.target_v:
                n_under += 1

        if self.n_params == 1:
            over_under_reward = 0.0
            mean_reward *= 2
        else:
            over_under_reward = ((n_over / mid) + (n_under / mid)) / 4

        reward = mean_reward + over_under_reward
        done = False
        if abs(self.target_v - mean) <= (self.change_step / 2) \
                and n_over == mid and n_under == mid:
            done = True

        return done, reward

    def step(self,
             action: np.ndarray) -> (np.ndarray, float, bool, Dict[Any, Any]):
        prev_v = np.copy(self.curr_v)
        param_idx = action[0]
        change_idx = action[1]
        if change_idx == 0:
            change_amount = -self.change_step
        else:
            change_amount = self.change_step

        self.curr_v[param_idx] += change_amount
        self.curr_v = np.clip(self.curr_v, 0.0, 1.0)
        self.curr_step_idx += 1

        done, reward = self._reward_fn(self.curr_v)

        if self.prev_action is not None:
            if action[0] == self.prev_action[0] \
                    and action[1] != self.prev_action[1]:
                return self.curr_v, -1.0, False, {'stuck': True}
        self.prev_action = action

        if np.allclose(prev_v, self.curr_v):
            return self.curr_v, -1.0, False, {'stuck': True}

        if self.curr_step_idx >= self.max_ep_steps:
            return self.curr_v, reward, True, {'stuck': True}

        return self.curr_v, reward, done, {'stuck': False}

    def reset(self) -> np.ndarray:
        self.curr_step_idx = 0
        self.prev_action = None
        self.seen_params = set()
        self.curr_v = np.random.uniform(0.0,
                                        1.0,
                                        (self.n_params,)).astype(np.float32)
        return self.curr_v

    def render(self, mode: str = 'human') -> None:
        pass

    def close(self) -> None:
        pass


def render(model: BaseAlgorithm,
           n_render_steps: int) -> (int, int):
    render_env = MeanEnv()

    n_done = 0
    n_stuck = 0
    curr_step_idx = 0
    done_steps = []
    stuck_steps = []

    obs = render_env.reset()
    for i in range(n_render_steps):
        action, _states = model.predict(obs, deterministic=False)
        curr_step_idx += 1
        log.debug(f'render prev_obs = {obs}')
        obs, reward, done, info = render_env.step(action)
        log.debug(f'render action = {action}')
        log.debug(f'render obs = {obs}')
        log.debug(f'render reward = {reward}')

        if done:
            if not info['stuck']:
                log.debug('done!')
                obs = render_env.reset()
                log.debug(f'env reset to {obs}')
                n_done += 1
                done_steps.append(curr_step_idx)
                curr_step_idx = 0
            else:
                log.debug('stuck!')
                obs = render_env.reset()
                log.debug(f'env reset to {obs}')
                n_stuck += 1
                stuck_steps.append(curr_step_idx)
                curr_step_idx = 0

        log.debug('')

    render_env.close()
    log.info(f'n_train_steps = {n_train_steps}')
    log.info(f'n_render_steps = {n_render_steps}')
    log.info(f'n_done = {n_done}')
    log.debug(f'len done_steps = {len(done_steps)}')
    if done_steps:
        log.info(f'mean done_steps = {np.mean(done_steps):.4f}')
    log.debug(f'sum done_steps = {sum(done_steps)}')

    log.info(f'n_stuck = {n_stuck}')
    log.debug(f'len stuck_steps = {len(stuck_steps)}')
    if stuck_steps:
        log.info(f'mean stuck_steps = {np.mean(stuck_steps):.4f}')
    log.debug(f'sum stuck_steps = {sum(stuck_steps)}')

    log.info(f'ending curr_step_idx = {curr_step_idx}')
    log.info(f'step sum = {sum(done_steps) + sum(stuck_steps) + curr_step_idx}')

    return n_done, n_stuck


if __name__ == '__main__':
    # train_env = MeanEnv()
    # check_env(train_env)
    # exit()
    train_env = make_vec_env(MeanEnv, n_envs=4, vec_env_cls=DummyVecEnv)
    # train_env = make_vec_env(MeanEnv, n_envs=4, vec_env_cls=SubprocVecEnv)
    # env = make_vec_env(MeanEnv, n_envs=4, vec_env_cls=SubprocVecEnv)

    # policy_kwargs = dict(activation_fn=th.nn.ReLU, net_arch=[4])
    policy_kwargs = dict(net_arch=[64, 64])
    # policy_kwargs = dict(net_arch=[dict(vf=[8], pi=[8])])
    model = PPO('MlpPolicy', train_env, policy_kwargs=policy_kwargs, verbose=1)
    # model = A2C('MlpPolicy', train_env, policy_kwargs=policy_kwargs, verbose=1)
    # model = PPO('MlpPolicy',
    #             env,
    #             verbose=1)
    # model = A2C('MlpPolicy', env, verbose=1)
    # model = SAC('MlpPolicy', env, verbose=1)
    # model = TD3('MlpPolicy', env, verbose=1)
    n_train_steps = 10000
    n_render_steps = 1000

    log.info('Random render')
    render(model, n_render_steps)

    log.info('Training')
    model.learn(total_timesteps=n_train_steps)
    # model.save('testing_model.zip')

    log.info('Rendering')
    render(model, n_render_steps)
