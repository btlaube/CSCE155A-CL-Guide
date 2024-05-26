import numpy as np
import random
import math

board_size = int(input('What would you like the size of your board to be?'))
board = np.full((board_size,board_size),'~')
total_slots = board_size * board_size
ship_slots = int(total_slots/5)
ships_per_row = ship_slots/board_size
ships_remaining = int(total_slots/5)
end_flag = 0
def ships(ship_slots,board_size,ships_per_row):
    global board
    for i in range(ship_slots):
            x = random.randint(0,board_size - 1)
            y = random.randint(0, board_size - 1)
            board[x][y] = '#'

def missle_launch(ship_slots,total_slots):
    global end_flag
    global ships_remaining
    global board
    while (ships_remaining > 0):
        x = int(input('What is the Y coordinate of your missile strike')) - 1
        y = int(input('What is the X coordinate of your missile strike')) - 1
        if board[x][y] == '#':
            board[x][y] = 'X'
            print('Direct Hit!!')
            ships_remaining -= 1
        else:
            board[x][y] = 'O'
            print('You missed')
        for n in range(board_size):
            print()
            for m in range(board_size):
                print(board[n][m],end='')
        print()
        print('Ships remaining', ships_remaining)


while True:
    if ships_remaining > 0:
        ships(ship_slots,board_size,ships_per_row)
        end_flag = missle_launch (ship_slots,total_slots)
    else:
        break

print('Nice work sailor, you defeated all the enemy ships')

