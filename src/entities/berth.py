from collections import deque


class Berth:

    def __init__(self, loading_speed: int, transport_time: int) -> None:
        self.free = True
        self.loading_speed = loading_speed
        self.transport_time = transport_time
        self.goods = deque()
