import random

#Function that will create a board in a list manner
def new_board(board_size):
    return[['.' for i in range(board_size)] for i in range(board_size)]

#Function that will print the board without brackets
def display_board(board):
    for i in board:
        print(*i)

#Function that will create battleship and keep them hidden 
def create_battleship(board_size):

    #If board is 2 or smaller legnth of ship is 1
    if board_size < 2:
        ship_len = 1
    #If board is 4 or smaller legnth of ship is 2
    elif board_size < 4:
        ship_len = 2
    #If board is 6 or smaller, legnth of ship is either 2 or 3
    elif board_size < 6:
        ship_len = random.randint(2,3)
    #If board is 8 or smaller, legnth of ship is either 2,3, or 4
    elif board_size < 8:
        ship_len = random.randint(2,4)
    #If board greater than 9, legnth of ship is either 2,3,4 or 5
    else:
        ship_len = random.randint(2,5)

    ship_pattern = random.randint(0, 1)

    #If orientation is 0, make the battleship horizontal, else make it verticle
    if ship_pattern == 0:
        ship_row = [random.randint(0, board_size - 1)] * ship_len
        cols = random.randint(0, board_size - ship_len)
        ship_col = list(range(cols, cols + ship_len))
        coordinates = tuple(zip(ship_row, ship_col))
    else:
        ship_col = [random.randint(0, board_size - 1)] * ship_len
        row = random.randint(0, board_size - ship_len)
        ship_row = list(range(row, row + ship_len))
        coordinates = tuple(zip(ship_row, ship_col))

    return list(coordinates)

def verify_coords(board_size):
    temp = False
    col, row = [int(i) for i in input("Pick a coordinate (x, y) to launch a missile (input space input) : \n>>").split()]

    #Loops all variable until the coordinates (x,y) are valid and can be on the board
    while temp == False:

        if row < 0 or row > board_size - 1:
            row = int(input("Please (re)enter your row (y) value that is not greater or less than the board:\n>>"))
            row = row - 1
            temp = False
        elif col < 0 or col > board_size - 1:
            col = int(input("Please (re)enter your column (x) value that is not greater or less than the board:\n>>"))
            col = col - 1
            temp = False
        else:
            temp = True
        
    return(row, col)

def update_board(given_coords, board, ship, coords):
    
    if given_coords in coords:
        print("You already made that given_coords! Try again...")
        return board
    coords.append(given_coords)
    board[given_coords[0]] [given_coords[1]] = 'O'
    if given_coords in ship:
        print("You hit a battleship!")
        board[given_coords[0]] [given_coords[1]] = 'X'
        ship.remove(given_coords)
        return board
    print("You miss! Try again...")
    return board

#Print Victory and exit Program
def victory_point():
    print("Congrats! You have sunk my battleship!")
    exit()


#Main function (For full points, less than 10 pieces of code in main, [can be done in 6])
if __name__ == '__main__':
    board_size = int(input("Enter a board size greater than 1: "))
    board = new_board(board_size)
    ships = create_battleship(board_size)
    coords = []
    display_board(board)
    while(len(ships) > 0):
        valid_coords = verify_coords(board_size)
        board = update_board(valid_coords, board, ships, coords)
        display_board(board)
    victory_point()