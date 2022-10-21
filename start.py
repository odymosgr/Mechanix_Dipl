import numpy as np

BOARD_SIZE = 4

# Initial Board State
# (X,Y) coordinates, where X+Y < BOARD_SIZE (domain)
# because of triangular board
# 0 = empty
# 1 = Player_1 gear
# 2 = Player_2 gear
# 3 = Goal gear

def initialize_board():
  board = np.zeros((BOARD_SIZE, BOARD_SIZE))
  board[0, 0] = 1
  board[BOARD_SIZE-1, 0] = 2
  board[0, BOARD_SIZE-1] = 3
  return board

board = initialize_board()
#print(board)
game_over = False
player_to_play = 1



# Get move from terminal user input
# Move is a tuple: (Type, X_origin, Y_origin, X_destination, Y_destination)
# Type = 'P' for PLACE a gear, or 'T' to TRANSPORT a gear
# if a move is TRANSPORT X_origin, Y_origin are required
#
def get_move_from_user(player_to_move):
  
  # Type
  message = "Player " + str(player_to_move) + ":\ntype 1 to PLACE\ntype 2 to TRANSPORT a gear \n"
  type_of_move = int(input(message))
  if type_of_move == 1:
    type = 'P'
  elif type_of_move == 2:
    type = 'T'
  else :
    print("Try again")
    return get_move_from_user(player_to_move)

  # X_origin, Y_origin
  # defaults
  x_origin = -1
  y_origin = -1

  if type == 'T':
    
    message = "select X_origin from 0 to " + str(BOARD_SIZE-1) + "\n"
    x_origin = int(input(message))
    if x_origin < 0 or x_origin >= BOARD_SIZE:
      print("Try again")
      return get_move_from_user(player_to_move)
    
    message = "select Y_origin from 0 to " + str(BOARD_SIZE-1) + "\n"
    y_origin = int(input(message))
    if y_origin < 0 or y_origin >= BOARD_SIZE:
      print("Try again")
      return get_move_from_user(player_to_move)
    
  message = "select X_destination from 0 to " + str(BOARD_SIZE-1) + "\n"
  x_destination = int(input(message))
  if x_destination < 0 or x_destination >= BOARD_SIZE:
    print("Try again")
    return get_move_from_user(player_to_move)
  
  message = "select Y_destination from 0 to " + str(BOARD_SIZE-1) + "\n"
  y_destination = int(input(message))
  if y_destination < 0 or y_destination >= BOARD_SIZE:
    print("Try again")
    return get_move_from_user(player_to_move)
  

  return (type, x_origin, y_origin, x_destination, y_destination)



###################
# GAME LOOP
###################
while not game_over:

  # Player 1 turn
  if player_to_play == 1:
    move = get_move_from_user(player_to_play)
    print(move)