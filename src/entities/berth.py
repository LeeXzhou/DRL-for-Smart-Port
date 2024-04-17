from collections import deque
from typing import List


class Berth:

    def __init__(self, loading_speed: int, transport_time: int) -> None:
        self.free = True
        self.loading_speed = loading_speed
        self.transport_time = transport_time
        self.goods = deque()

    @property
    def cnt(self):
        """number of goods on the berth"""
        return len(self.goods)

    @property
    def val(self):
        """value of goods on the berth"""
        return sum(self.goods)

    def load(self, good_val: float):
        """
        load good FROM ROBOT to a berth. \n
        Only executed after robot.unload is executed
        """
        self.goods.append(good_val)

    def try_unload(self) -> List[float]:
        """
        try to unload goods to a BOAT. \n
        get elements from self.goods without removing it

        Note:
            Run try_unload before boat.safe_load.
        """
        to_unload = min(self.loading_speed, self.cnt)
        return list(self.goods)[:to_unload]

    def unload(self, num: int):
        """
        unload goods to a BOAT. \n
        Only executed after boat.safe_load is executed
        """
        for _ in range(num):
            self.goods.popleft()
