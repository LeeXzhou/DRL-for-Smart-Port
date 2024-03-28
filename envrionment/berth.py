import queue

global berth_info


class Berth():
    def __init__(self, loading_speed: int, transport_time: int) -> None:
        """
        :param loading loading_speed: how many goods the berth can load to ship per frame
        :param transport_time: the time travel to the discharging port
        """
        self.free = True
        self.loading_speed = loading_speed
        self.transport_time = transport_time
        self.goods_info = queue.Queue()


berth_info: list[Berth] = [Berth(0, 0)] * 10
for i in range(0, 10):
    berth_info.append(Berth(0, 0))


def init_berth(loading_speeds: list, transport_times: list) -> None:
    for i in range(0, 10):
        berth_info[i].loading_speed = loading_speeds[i]
        berth_info[i].transport_time = transport_times[i]
    return
