import gym
import torch
import numpy as np
import utils
import boat_move

class Port(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self, map_path: str, boat_capacity : int = 70, seed: int = 0) -> None:
        '''
        :param map_path: read map file path
        :param seed: for random generating goods
        map description:
        . -> 0 land
        * -> -1 sea
        # -> -2 obstacle
        A -> -3 robot position
        B -> -4 port position, consist of 4 * 4 points
        a positive number means that here is a good and the number means its value
        '''
        self.action_space = None
        self.observation_space = None
        self.map_path = map_path
        self.map = np.zeros((200, 200))
        self.capacity = boat_capacity
        self.boat = []
        self.score = 0
        self.goods_info = []
        self.reset()
        pass

    def step(self, actions):
        for action in actions:
            option = action[:2]
            if option == "mo":
                None
            elif option == "ge":
                None
        return self.state

    def reset(self):
        self.map = utils.map_translator(self.map_path)
        self.score = 0
        self.boat = []
        for i in range(0, 10):
            self.boat.append(boat_move.boat_info(self.capacity, -1, 0))
        return self.state

    def render(self, mode='human'):
        return None

    def close(self):
        return None
