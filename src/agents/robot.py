import numpy as np


class Robot:
    """robot move can be controlled by rl but get and pull action cannot???"""

    def __init__(self, id: int, init_x: int, init_y: int) -> None:
        self.id = id
        self.goods = 0
        self.pos = [init_x, init_y]
        # self.wait_time = 0

        self._val = 0

    def sample_action(self):
        """output all actions of robot including move, get, and pull"""
        pass

    def load(self, good_val: float):
        """
        load goods to robot, execute only if the get action succeed. \n
        set self.goods to 1 and set self._val to good_val
        """
        self.goods = 1
        self._val = good_val

    def unload(self) -> float:
        """
        unload goods to a berth. Execute only if the pull action succeed. \n
        reset self.goods to 0 and reset self._val to 0
        """
        self.goods = 0
        self._val = 0
