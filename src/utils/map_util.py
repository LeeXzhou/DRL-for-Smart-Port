import numpy as np

from pathlib import Path

from src.consts import MAP_BERTH, MAP_GROUND, MAP_OBSTACLE, MAP_OCEAN, MAP_ROBOT, MAP_DICT, MAP_SIZE
from src.utils.logger import log

def map_translator(map_path: str) -> np.ndarray:
    '''
    :param map_path: map file path
    '''
        
    path = Path(__file__).parent.parent.parent / map_path
    
    map_ = np.zeros(MAP_SIZE, dtype=int)
    
    with open(path, 'r') as file:
        lines = file.readlines()
        row = 0
        column = 0
        for line in lines:
            line = line.rstrip('\n')  # strip newline character
            for char in line:
                map_[row][column] = MAP_DICT[char]
                column += 1
            row += 1
            column = 0
            
    return map_.copy()