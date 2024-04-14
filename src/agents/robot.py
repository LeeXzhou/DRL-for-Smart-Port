import numpy as np


class Robot:
    """robot move can be controlled by rl but get and pull action cannot???"""

    def __init__(self, id: int, init_x: int, init_y: int) -> None:
        self.id = id
        self.goods = 0
        self.pos = [init_x, init_y]
        # self.wait_time = 0

    def act(self):
        """output all actions of robot including move, get, and pull"""
        pass
