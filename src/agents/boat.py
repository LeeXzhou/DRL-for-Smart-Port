from collections import deque


class Boat:

    capacity = 0

    @classmethod
    def set_capacity(cls, capacity):
        cls.capacity = capacity

    def __init__(self, init_pos: int = -1) -> None:
        self.pos = init_pos

        self.goodlist = deque()  # save good value in the goodlist
        """goods on the boat (len = current goods number, sum = goods value on the boat)"""
        # self.score = 0

        self.status = 0
        """
        `0`: moving \n
        `1` at the berth or discharging port (virtual point) \n
        `2` waiting outside the berth (in berth waiting list)
        """

        self.waiting_list = deque()
        """berth waiting list (if needed)"""

        self.target = -1
        """target: berth to arrive"""
        self.reach_time = -1

    def act(self):
        """output all actions of boat include ship and go"""
        pass
