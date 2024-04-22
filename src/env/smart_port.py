import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pettingzoo as pz
import pygame
import tomli

from dataclasses import dataclass
from gymnasium.spaces import Box, Discrete, MultiDiscrete
from matplotlib.colors import ListedColormap
from pathlib import Path
from pettingzoo import AECEnv
from typing import Tuple

from src.consts import (
    MAP_COLOR,
    MAP_ROBOT,
    MAP_OCEAN,
    MAP_OBSTACLE,
    N,
)
from src.utils.logger import log
from src.utils.map_util import map_translator


robot_dtype = np.dtype(
    [
        ('x', int),
        ('y', int),
        ('good', int),
        ('val', int),
        ('status', int),
    ]
)

boat_dtype = np.dtype(
    [
        ('status', int),
        ('target', int),
        ('cnt', int),
        ('val', int),
        ('travel_time_left', int),
    ]
)


class SmartPort(AECEnv):

    def __init__(
        self,
        map_path: str = 'maps/map1.txt',
        num_robots: int = 10,
        num_boats: int = 5,
        num_berths: int = 10,
    ):
        super().__init__()

        self.num_robots = num_robots
        self.num_boats = num_boats
        self.num_berths = num_berths

        robot_action_spaces = {
            f'robot_{i}': MultiDiscrete([5, 2, 2]) for i in range(num_robots)
        }
        """
        the first dimension of the action space is the moving direction (4 dirs and stay) of the robot \n
        the second dimension of the action space is the get action (bool) of the robot \n
        the third dimension of the action space is the pull action (bool) of the robot
        """

        boat_action_spaces = {
            f'boat_{i}': MultiDiscrete(np.array([2, 2, num_berths]))
            for i in range(num_boats)
        }
        """
        the first dimension of the boat action space is the go action (bool) of the boat \n
        the second dimension of the boat action space is the ship action (bool) of the boat \n
        the third dimension of the boat action space is the ship dest of the boat.
        """

        robot_observation_space = {
            f'robot_{i}': gym.spaces.Dict(
                {
                    'position': MultiDiscrete(np.array([N, N])),
                    'good': Discrete(2),
                    'status': Discrete(2),
                    'good_val': Discrete(int(1e3)),
                    'recorevy_time': Discrete(int(1e2)),
                }
            )
            for i in range(num_robots)
        }
        """
        whether the robot has carried goods \n
            `0` - no goods, `1` - with goods. \n
        robot status. \n
            `0` - recovery state, `1` - running state
        """
        # self.robot_goods_value = np.zeros(num_robots, dtype=int)
        # self.robot_recovery_time = np.zeros(num_robots, dtype=int)

        boat_observation_space = {
            # f'boat_{i}': MultiDiscrete(np.array([3, num_berths + 1]))
            f'boat_{i}': gym.spaces.Dict(
                {
                    'target_position': Box(low=-1, high=num_berths, dtype=int),
                    'status': Discrete(3),
                    'good_val': Discrete(int(1e10)),
                    'travel_time_left': Discrete(int(1e5)),
                }
            )
            for i in range(num_boats)
        }
        """
        boat status. \n
            `0` - moving status, `1` - running status, `2` - waiting status. \n
        target position of boat. \n
            `-1` - target is virtual point, `0` - target is berth 0, `1` - target is berth 1, ... \n
        """

        self.action_spaces = {**robot_action_spaces, **boat_action_spaces}
        self.observation_spaces = {**robot_observation_space, **boat_observation_space}

        self._ori_map = map_translator(map_path)
        self._bimap = np.zeros_like(self._ori_map)
        for (i, j), val in np.ndenumerate(self._ori_map):
            self._bimap[i, j] = val not in [MAP_OCEAN, MAP_OBSTACLE]

    def reset(self):
        self._map = self._ori_map.copy()

        # robot initialization
        rows, cols = np.where(self._map == MAP_ROBOT)
        robot_pos_list = list(zip(rows, cols))
        robot_state = {
            f'robot_{i}': {
                'position': np.array(pos),
                'good': 0,  # with no good
                'status': 1,  # running
                'good_val': 0,
                'recorevy_time': 0,
            }
            for i, pos in enumerate(robot_pos_list)
        }

        boat_state = {
            f'boat_{i}': {
                'target_position': -1,  # in virtual point
                'status': 1,  # running
                'good_val': 0,
                'travel_time_left': 0,
            }
            for i in range(self.num_boats)
        }

        path = Path(__file__).parent
        with open(f"{path}/conf.toml", "rb") as f:
            log.warning(
                'The env parameter in file `src/env/conf.toml` needs to be set.'
            )
            self.params = tomli.load(f)

        self.state = {**robot_state, **boat_state}

        return self.state, self.params

    # 1. 机器人恢复。
    # 2. 船舶到达、进入泊位。
    # 3. 货物生成。
    # 4. 生成场面信息，输出给选手。
    # 5. 读取选手指令。
    # 6. 执行机器人指令。
    # 7. 执行船舶指令。
    # 8. 泊位装卸货物。

    def step(self, actions):
        log.info(actions)

        self.__robot_exec()
        self.__berth_exec()
        self.__berth_exec()

        ### prepare for next frame
        self.__robot_reset()
        self.__boat_entrance()
        self.__good_gen()
        # return state to agents.

    def render(self, mode='human', use_pygame=False):
        """
        ## render the env

        Notes:
            set `use_pygame=False` in jupyter notebook (work properly).

            pygame module has not been tested yet. (WIP)
        """

        if use_pygame:
            """use pygame to render the environment"""
            if not hasattr(self, 'screen'):
                pygame.init()
                self.screen = pygame.display.set_mode(
                    (self.grid_size[0] * 50, self.grid_size[1] * 50)
                )
                self.clock = pygame.time.Clock()

            self.screen.fill((255, 255, 255))

            for x in range(0, self.grid_size[0]):
                for y in range(0, self.grid_size[1]):
                    rect = pygame.Rect(x * 50, y * 50, 50, 50)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

            # Update the display
            pygame.display.flip()

            # Control the frame rate
            self.clock.tick(10)

            # Handle events (e.g., quit the game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        else:
            """use matplotlib to render the environment"""
            # log.info(matplotlib.get_backend())

            if not hasattr(self, 'ax') or not hasattr(self, 'fig'):
                self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 10), dpi=300)

            cmap = ListedColormap(MAP_COLOR)

            self.ax.imshow(self._map, cmap=cmap)

            self.ax.set_aspect('equal', adjustable='box')

            self.ax.set_xticks([])
            self.ax.set_yticks([])
            self.ax.set_title("SmartPort")

            plt.show()

    def get_map(self, x_min: int = 0, x_max: int = N, y_min: int = 0, y_max: int = N):
        return self._map[x_min:x_max, y_min:y_max].copy()

    def get_bimap(self, x_min: int = 0, x_max: int = N, y_min: int = 0, y_max: int = N):
        return self._bimap[x_min:x_max, y_min:y_max].copy()

    def __robot_reset(self):
        """robot reset from recovery mode"""
        ...

    def __boat_entrance(self):
        """boat arrival and enter the berth"""
        ...

    def __good_gen(self):
        """generate goods"""
        ...

    def __robot_exec(self):
        """robot execution"""
        ...

    def __boat_exec(self):
        """boat execution"""
        ...

    def __berth_exec(self):
        """berth execution (automatic goods loading for boats)"""
        ...
