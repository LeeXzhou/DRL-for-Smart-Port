import gym
import torch


class Port(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.action_space = None
        self.observation_space = None
        pass

    def step(self, action):
        return self.state, reward, done, {}

    def reset(self):
        return self.state

    def render(self, mode='human'):
        return None

    def close(self):
        return None