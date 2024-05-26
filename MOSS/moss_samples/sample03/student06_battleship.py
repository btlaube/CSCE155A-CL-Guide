
import random

#Function that will create a board in a list manner
def create_board(grid_size):
    return[['.' for count in range(grid_size)] for count in range(grid_size)]

#Function that will print the board without brackets
def print_board(board):
    for b in board:
        print(*b)

#Function that will create battleship and keep them hidden 
def create_battleship(grid_size):

    #If board is 2 or smaller legnth of ship is 1
    if grid_size < 2:
        battleship_length = 1
    #If board is 4 or smaller legnth of ship is 2
    elif grid_size < 4:
        battleship_length = 2
    #If board is 6 or smaller, legnth of ship is either 2 or 3
    elif grid_size < 6:
        battleship_length = random.randint(2,3)
    #If board is 8 or smaller, legnth of ship is either 2,3, or 4
    elif grid_size < 8:
        battleship_length = random.randint(2,4)
    #If board greater than 9, legnth of ship is either 2,3,4 or 5
    else:
        battleship_length = random.randint(2,5)

    battleship_orientation = random.randint(0, 1)

    #If orientation is 0, make the battleship horizontal, else make it verticle
    if battleship_orientation == 0:
        battleship_row = [random.randint(0, grid_size - 1)] * battleship_length
        cols = random.randint(0, grid_size - battleship_length)
        battleship_col = list(range(cols, cols + battleship_length))
        coordinates = tuple(zip(battleship_row, battleship_col))
    else:
        battleship_col = [random.randint(0, grid_size - 1)] * battleship_length
        row = random.randint(0, grid_size - battleship_length)
        battleship_row = list(range(row, row + battleship_length))
        coordinates = tuple(zip(battleship_row, battleship_col))

    return list(coordinates)

def user_guess(grid_size):
    valid = 'False'
    print("***Keep in mind that there is no 0 index in this program***")

    col, row = [int(i) for i in input("Pick a coordinate (x, y) to launch a missile (input *space* input) : \n>>").split()]

    #Removes 0 index
    row = row - 1
    col = col - 1

    #Loops all variable until the coordinates (x,y) are valid and can be on the board
    while valid == 'False':

        if row < 0 or row > grid_size - 1:
            row = int(input("Please (re)enter your row (y) value that is not greater or less than the board:\n>>"))
            row = row - 1
            valid = 'False'
        elif col < 0 or col > grid_size - 1:
            col = int(input("Please (re)enter your column (x) value that is not greater or less than the board:\n>>"))
            col = col - 1
            valid = 'False'
        else:
            valid = "True"
        
    return(row, col)

def board_update(guess, board, ship, guesses):
    
    if guess in guesses:
        print("You already made that guess! Try again...")
        return board
    guesses.append(guess)
    board[guess[0]] [guess[1]] = 'O'
    if guess in ship:
        print("You hit a battleship!")
        board[guess[0]] [guess[1]] = 'X'
        ship.remove(guess)
        return board
    print("You miss! Try again...")
    return board

#Print Victory and exit Program
def win():
    print("Congrats! You have sunk my battleship!")
    exit()


#Main function (For full points, less than 10 pieces of code in main, [can be done in 6])
if __name__ == '__main__':
    board_area = int(input("Enter a board size greater than 1: "))
    board = create_board(board_area)
    ship = create_battleship(board_area)
    guesses = []
    print_board(board)
    while(len(ship) > 0):
        attempt_guess = user_guess(board_area)
        board = board_update(attempt_guess, board, ship, guesses)
        print_board(board)
    win()
        


