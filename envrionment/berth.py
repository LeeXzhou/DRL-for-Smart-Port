import queue
class berth():
    def __init__(self, loading_speed: int, transport_time: int) -> None:
        '''
        :param loading speed: how many goods the berth can load to ship per frame
        :param transport_time: the time travel to the discharging port 
        '''
        self.free = True
        self.loading_speed = loading_speed
        self.transport_time = transport_time
        self.goods_info = queue.Queue()
berth_info = []
def init_berth(loading_speeds : list, transport_times : list) -> None:
    global berth_info
    berth_info = []
    for i in range(0, 10):
        berth_info.append(berth(loading_speeds[i], transport_times[i]))
    return
