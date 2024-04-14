from src.env.smart_port import SmartPort
from src.utils.logger import log


def test_sample_action():
    env = SmartPort()
    log.info(env.action_spaces['robot_1'].sample())
    log.info(env.action_spaces['boat_1'].sample())
