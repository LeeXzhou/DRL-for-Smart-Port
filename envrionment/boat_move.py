import torch
import numpy as np
import berth
class boat_info():
    capacity = 0
    def __init__(self, max_capacity : int, cur_pos : int = -1, cur_num : int = 0) -> None:
        '''
        :param max_capacity: all boats share a max_capacity, so capacity is a class variable
        :param cur_pos: boat current berth
        :param cur_num: boat current goods num, if num = capacity, it's incapable of loading any goods
        state :0 -> moving, 1 -> at the berth or discharging cargo 2 -> waiting outside the berth
        '''
        self.cur_pos = cur_pos
        self.cur_num = cur_num
        self.state = 0
        self.score = 0
        boat_info.capacity = max_capacity
    def boat_move(self, option : str, goal : int = -1):
        '''
        control the boat to go to target berth
        :param goal: target berth or discharging cargo
        :return:
        '''

    def boat_load(self):
        return
