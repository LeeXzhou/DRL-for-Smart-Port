N = 200

MAP_GROUND = 1  # `.`
MAP_OCEAN = 2  # `*`
MAP_OBSTACLE = 3  # `#`
MAP_ROBOT = 4  # `A`
MAP_BERTH = 5  # `B`

MAP_DICT = {'.': MAP_GROUND, '*': MAP_OCEAN, '#': MAP_OBSTACLE, 'A': MAP_ROBOT, 'B': MAP_BERTH}
MAP_SIZE = (N, N)

MAP_COLOR = [
    '#c5daac',    # map ground
    '#dbe3f4',    # map ocean
    '#b2a79d',    # map obstacle
    '#191919',    # map robot
    '#b8c2c5',    # map berth
]