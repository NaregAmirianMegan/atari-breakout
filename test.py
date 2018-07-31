import numpy as np

game_state = np.zeros((20, 10))

for x in range(20):
    for y in range(10):
        game_state[x][y] = x + y

game_state[1] = game_state[0]

print(game_state)
