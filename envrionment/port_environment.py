import gym
import torch
import numpy as np
import utils
import boat_move
import re
import berth
class Port(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self, map_path: str, loading_speeds : list, transport_times : list, boat_capacity : int = 70, seed: int = 0) -> None:
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
        self.loading_speeds = loading_speeds
        self.transport_times = transport_times
        self.reset()
        pass

    def step(self, actions):
        for action in actions:
            numbers=re.findall(r'-?\d+',action) # collect the integers in "action" to judge the action is legal or not
            if re.match("move",action) and len(numbers)==2:
                None
            elif re.match("get",action) and len(numbers)==1:
                None
            elif re.match("pull",action) and len(numbers)==1:
                None
            elif re.match("go",action) and len(numbers)==1:
                None
            elif re.match("ship",action) and len(numbers)==2:
                None
        return self.state

    def reset(self):
        self.map = utils.map_translator(self.map_path)
        self.score = 0
        berth.init_berth(self.loading_speeds, self.transport_times)
        self.boat = []
        for i in range(0, 10):
            self.boat.append(boat_move.boat_info(self.capacity, -1, 0))
        return self.state 

    def render(self, mode='human'):
        return None

    def close(self):
        return None
