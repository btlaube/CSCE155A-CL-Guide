# student01 - CSCE155A

from random import randint

# define a list for storing the board configuration
board = []


# function to create board
def create_board(size):
    for x in range(size):
        board.append(["~"] * size)


def random_row(size):
    return randint(0, size - 1)


def random_col(size):
    return randint(0, size - 1)


# function that places ship # in the random x,y coordinates
def place_ship():
    x = random_row(size)
    y = random_col(size)
    board[x][y] = "X"


# function that displays board configuration
def display_board(brd):
    for r in brd:
        print(" ".join(r))


# function that places X if there is ship in specified loc.
# Otherwise, it places O
def launch_missile(board, row, col):
    if board[row][col] == "X":
        print("Boom! You hit a ship!")
        board[row][col] = "!"
    else:
        print("You missed! Try again.")
        board[row][col] = "O"
    return board


print("Let's play Battleship!")
# prompt and accept board size
size = int(input("Enter board size: "))
create_board(size)
total_tiles = size * size
# number of ships must be less than one-fifth of number of titles
numShips = int((1 / 5) * total_tiles)
for i in range(numShips + 1):
    place_ship()
display_board(board)

# prompt and accept location of missile
for turn in range(size * size):
    coord_x, coord_y = [int(i) for i in input("Pick a coordinate to launch missile: ").split()]

    col = coord_x
    row = coord_y

    if (row < 0) or (row > (size - 1)) or (col < 0) or (col > size - 1):
        print("oops! That's not part of board")
        continue
    else:
        # launch missile in the specified loc
        board = launch_missile(board, row, col)
        display_board(board)
