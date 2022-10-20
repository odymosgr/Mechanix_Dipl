import numpy as np

BOARD_SIZE = 4

# Initial Board State
# (X,Y) coordinates, where X+Y < BOARD_SIZE (domain)
# because of triangular board
# 0 = empty
# 1 = Player_1 gear
# 1 = Player_2 gear

def initialize_board():
  board = np.zeros((BOARD_SIZE, BOARD_SIZE))
  board[0, 0] = 1
  board[BOARD_SIZE-1, 0] = 2
  board[0, BOARD_SIZE-1] = 3
  return board

board = initialize_board()
print(board)