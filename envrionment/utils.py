import matplotlib.pyplot as plt
import numpy as np
map=np.zeros((200,200))

def map_translator(map_path: str) -> np.array:
    '''
    :param map_path: map file path
    :return: map
    '''
    map_dict = {'.': 0, '*': -1, '#': -2, 'A': -3, 'B': -4}
    ret = np.zeros((200, 200))
    with open(map_path, 'r') as file:
        lines = file.readlines()
        row = 0
        column = 0
        for line in lines:
            for char in line:
                ret[row][column] = map_dict[char]
                column += 1
            row += 1
            column = 0
    global map
    map =ret
    return ret


def show_map(map: np.array) -> None:
    '''
    :param map: map information
    '''
    img = np.zeros((600, 600), dtype=np.uint8)
    for i in range(0, 200):
        for j in range(0, 200):
            tp = (0, 0, 0)
            if map[i][j] == 0:
                tp = (100, 240, 100)
            elif map[i][j] == -1:
                tp = (150, 200, 255)
            elif map[i][j] == -2:
                tp = (128, 128, 128)
            elif map[i][j] == -3:
                tp = (255, 255, 255)
            else:
                tp = (0, 0, 0)
            for u in range(0, 3):
                for v in range(0, 3):
                    img[i * 3 + u][j * 3 + v] = tp
    plt.imshow(img)
    plt.show()

def check_valid(x:int,y:int)->bool:
    global map
    if(x>=200 or x<0 or y<0 or y>=200):
        return False
    if(map[x][y]==-1 or map[x][y]==-2):
        return False
    return True