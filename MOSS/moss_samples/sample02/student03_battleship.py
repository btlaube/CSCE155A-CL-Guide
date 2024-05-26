# Battleship game

import random
import numpy as np
import os
import time

# Variable Definition
num_ships = 0
size = int(input("Enter a board size: "))
ocean = np.full((size,size),' ')

# Make the map
def makeMap_function(size, num_ships, ocean):
    for x in range(0,size):
        for y in range(0,size):
            dice = random.randint(1,5)
            if (dice == 1):
                if num_ships < (1/5 * size * size):
                    ocean[x][y] = "🛳"
                    num_ships += 1
                else:
                    ocean[x][y] = '🌊'
            else:
                ocean[x][y] = '🌊'
    print("There are", num_ships, "ships in the ocean.")
    return num_ships

# Print the map
def print_array(arr):
    os.system('clear')
    for x in range(0,size):
        for y in range(0,size):
            print("\033[0;40;33m" + str(arr[y][x]),end=' ')
        print()

# Shooting function
def shooting_function(num_ships):
    while True:
        coord_x = int(input("\033[0;34;37mPick an x coordinate: "))
        coord_y = int(input("\033[0;34;37mPick a y coordinate: "))
        if coord_x < 0 or coord_x > size - 1 or coord_y < 0 or coord_y > size - 1:
            print("\033[0;34;31mNot a valid coordinate.")
            continue
        if ocean [coord_x][coord_y] == "🛳":
            ocean [coord_x][coord_y] = "X"
            print_array(ocean)
            print("\033[0;34;32mConfirmed hit!")
            num_ships -= 1
            if num_ships == 1:
                print(num_ships, "ship remaining")
            else:
                print(num_ships, "ships remaining")
        elif ocean [coord_x][coord_y] == "🌊":
            ocean [coord_x][coord_y] = "O"
            print_array(ocean)
            print("\033[0;34;32mHow could you miss? The ships are right in front of you!")
            if num_ships == 1:
                print(num_ships, "ship remaining")
            else:
                print(num_ships, "ships remaining")
        if num_ships == 0:
            print("Congrats! You destroyed all enemy ships. You are our savior!")
            exit()

# Main Code
num_ships = makeMap_function(size, num_ships, ocean)
print_array(ocean)
shooting_function(num_ships)
