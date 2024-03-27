import re

import berth


class boat_info():
    capacity = 0
    berth_info: list[berth.berth] = berth.berth_info  # 10 berth information

    def __init__(self, max_capacity: int, cur_pos: int = -1, cur_num: int = 0) -> None:
        '''
        :param max_capacity: all boats share a max_capacity, so capacity is a class variable
        :param cur_pos: boat current berth
        :param cur_num: boat current goods num, if num = capacity, it's incapable of loading any goods
        status :0 -> moving, 1 -> at the berth or discharging port 2 -> waiting outside the berth
        reach_time : ->time the boat reach its aim
        '''
        self.cur_pos = cur_pos
        self.cur_num = cur_num
        self.status = 0
        self.score = 0
        self.aim_berth = -1
        self.reach_time = -1

        boat_info.capacity = max_capacity

    def boat_move(self, option: str, goal: int = -1):
        '''
        control the boat to go to target berth
        :param goal: target berth or discharging port
        :return:
        '''

        if re.match("ship", option):
            if (self.cur_pos == -1):
                self.status = 0
                boat_info.berth_info[self.aim_berth].free = True
                self.aim_berth = option
                self.reach_time = boat_info.berth_info[self.aim_berth].transport_time + 1
            else:
                self.status = 0
                boat_info.berth_info[self.aim_berth].free = True
                self.aim_berth = option
                self.reach_time = 500 + 1
        elif re.match("go", option):
            self.status = 0
            boat_info.berth_info[self.aim_berth].free = True
            self.reach_time = boat_info.berth_info[self.aim_berth].transport_time + 1
            # +1 means the frame we get the order "ship" or "go" , the boat not move at once ,so we need an extra frame to minus
            self.aim_berth = option
        else:
            return

    def update(self) -> int:
        if (self.status == 0):
            self.reach_time -= 1
            if (self.reach_time == 0):
                if (self.aim_berth == -1):
                    # reach the discharging port and reset the boat status, cargo numbers, position, score
                    ret = self.score
                    self.score = 0
                    self.status = 1
                    self.cur_pos = -1
                    self.cur_num = 0
                    return ret
                else:
                    if (boat_info.berth_info[self.aim_berth].free):
                        self.status = 1
                        boat_info.berth_info[self.aim_berth].free = False
                        self.cur_pos = self.aim_berth
                    else:
                        self.status = 2
            return 0
        elif (self.status == 1):
            if (self.cur_pos == -1):
                # just waiting at the discharging port
                return 0
            else:
                # automatically loading cargos from the port
                for i in range(boat_info.berth_info[self.cur_pos].loading_speed):
                    if(boat_info.berth_info[self.cur_pos].goods_info.empty()):
                        break
                    temp_value = boat_info.berth_info[self.cur_pos].goods_info.get()
                    self.cur_num += 1
                    self.score += temp_value
                return 0
        else:
            # if status==2 just do nothing
            return 0

    def boat_load(self):
        return
