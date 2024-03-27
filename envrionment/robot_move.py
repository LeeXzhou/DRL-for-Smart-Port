import berth
import utils
class robot_info():
    def __init__(self,posx :int,posy:int)->None:
        self.goods = 0
        self.pos=[posx,posy]
        self.wait_time=0
    
    def robot_move(self,id :int)->None:
        if(id>self.wait_time):
            return
        if(utils.check_valid(self.pos[0],self.pos[1])):
            None
    
    