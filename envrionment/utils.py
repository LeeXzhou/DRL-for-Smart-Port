import matplotlib.pyplot as plt
import numpy as np

global Map
Map = np.zeros((200, 200))


def map_translator(map_path: str) -> None:
    '''
    :param map_path: map file path
    '''
    map_dict = {'.': 0, '*': -1, '#': -2, 'A': -3, 'B': -4}
    with open(map_path, 'r') as file:
        lines = file.readlines()
        row = 0
        column = 0
        for line in lines:
            for char in line:
                Map[row][column] = map_dict[char]
                column += 1
            row += 1
            column = 0


def show_map() -> None:
    img = np.zeros((600, 600), dtype=np.uint8)
    for i in range(0, 200):
        for j in range(0, 200):
            tp = (0, 0, 0)
            if Map[i][j] == 0:
                tp = (100, 240, 100)
            elif Map[i][j] == -1:
                tp = (150, 200, 255)
            elif Map[i][j] == -2:
                tp = (128, 128, 128)
            elif Map[i][j] == -3:
                tp = (255, 255, 255)
            else:
                tp = (0, 0, 0)
            for u in range(0, 3):
                for v in range(0, 3):
                    img[i * 3 + u][j * 3 + v] = tp
    plt.imshow(img)
    plt.show()


def check_valid(x: int, y: int) -> bool:
    if (x >= 200 or x < 0 or y < 0 or y >= 200):
        return False
    if (Map[x][y] == -1 or Map[x][y] == -2):
        return False
    return True
