from collections import deque
from queue import Queue

from src.env.smart_port import SmartPort
from src.utils.logger import log


def test_sample_action():
    env = SmartPort()
    log.info(env.action_spaces['robot_1'].sample())
    log.info(env.action_spaces['boat_1'].sample())
    log.info(env.observation_spaces['boat_1'].sample())
    env.reset()


def test_queue():
    deq = deque()
    q = Queue()
    deq.append(1)
    deq.extend([2, 3, 4])
    q.put(1)
    q.put([2, 3, 4])

    log.info(deq)
    log.info(q)
