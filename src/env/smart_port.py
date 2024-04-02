import gymnasium as gym
import matplotlib.pyplot as plt
import pygame

from matplotlib.colors import ListedColormap
from pettingzoo import AECEnv
from typing import Tuple

from src.consts import MAP_COLOR
from src.utils.logger import log
from src.utils.map_util import map_translator



class SmartPort(AECEnv):

    TEST = 100
    
    def __init__(
        self,
        map_path: str = 'maps/map1.txt',
        num_robots: int = 10,
        num_boats: int = 5,
        num_berths: int = 10,
    ):
        super().__init__()
        
        self._map = map_translator(map_path)
        
        self.num_robots = num_robots
        self.num_boats = num_boats
        self.num_berths = num_berths

    def reset(self): ...

    def step(self): ...

    def observe(self): ...

    def render(self, mode='human', use_pygame=False):
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
