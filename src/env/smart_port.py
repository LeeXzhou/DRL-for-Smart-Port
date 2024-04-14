import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pettingzoo as pz
import pygame

from gymnasium.spaces import MultiDiscrete
from matplotlib.colors import ListedColormap
from pettingzoo import AECEnv
from typing import Tuple

from src.consts import MAP_COLOR, N, MAP_GROUND, MAP_ROBOT, MAP_BERTH
from src.utils.logger import log
from src.utils.map_util import map_translator


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
        the first dimension of the boat action space is the go action (bool) of the boat
        the second dimension of the boat action space is the ship action (bool) of the boat
        the third dimension of the boat action space is the ship dest of the boat.
        """

        self.action_spaces = {**robot_action_spaces, **boat_action_spaces}

        self._map = map_translator(map_path)

    def reset(self): ...

    def step(self): ...

    def observe(self): ...

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
        map_ = self.get_map(x_min, x_max, y_min, y_max)
        res = np.zeros_like(map_)
        for (i, j), val in np.ndenumerate(map_):
            res[i, j] = val in [MAP_GROUND, MAP_ROBOT, MAP_BERTH]
        return res
