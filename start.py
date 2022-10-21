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


# returns true, if gear exists at position (x,y) of board
def gear_exists_at(pos, board):
  if pos[0] in range(BOARD_SIZE) and pos[1] in range(BOARD_SIZE-pos[0]) and board[pos[0],pos[1]] != 0: return True
  return False



# Returns a dictionary which maps 
# gear positions with connections (represented by tuples)
# to list of connected gear positions 
#
def board_to_adj_list(board):
  adj_list = {}
  #check every gear position
  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE-i):
      #print(str((i,j)) + " -> " + str(board[i,j]))
      temp = []

      #if no gear, no connections
      if board[i,j] == 0: continue
      # Up Left connection check
      x=i-1
      y=j+1
      if gear_exists_at((x,y), board): temp.append((x,y))
      # Up Right connection check
      x=i
      y=j+1
      if gear_exists_at((x,y), board): temp.append((x,y))
      # Left connection check
      x=i-1
      y=j
      if gear_exists_at((x,y), board): temp.append((x,y))
      # Right connection check
      x=i+1
      y=j
      if gear_exists_at((x,y), board): temp.append((x,y))
      # Down Left connection check
      x=i
      y=j-1
      if gear_exists_at((x,y), board): temp.append((x,y))
      # Down Right connection check
      x=i+1
      y=j-1
      if gear_exists_at((x,y), board): temp.append((x,y))
      
      if temp: adj_list[(i,j)] = temp
  return adj_list




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



# Given a board and a gear position to turn clockwise
# return a matrix representing the board with rotational directions of gears
# 0 = no gear or no motion
# 1 = clockwise
# 2 = counterclockwise
# -1 = jammed
# --------
# BFS implementation
# same as Graph Coloring with 2 colors
def turn_gear_clockwise(board, pos):
  bfs_queue = []
  visited = []
  board_rotations = np.zeros((BOARD_SIZE, BOARD_SIZE))
  jam = False

  adj_l = board_to_adj_list(board)
  
  if not gear_exists_at(pos, board): return board_rotations
  board_rotations[pos[0],pos[1]] = 1
  bfs_queue.append((pos, 1))

  while bfs_queue:
    node = bfs_queue.pop(0)
    #print("checking queue item: " + str(node))

    for neighbour in adj_l[node[0]]:
      # check neighbours with same rotations
      if board_rotations[neighbour[0], neighbour[1]] == node[1]: jam = True
      # add unvisited neighbour with opposite rotation to rotations matrix, and to queue
      if neighbour not in visited:
        opp_rot = 1+(2-node[1])%2
        board_rotations[neighbour[0], neighbour[1]] = opp_rot
        bfs_queue.append((neighbour, opp_rot))
    # after all neighbours are checked mark node as visited
    visited.append(node[0])

  #print(jam)
  # if jammed, all non zero numbers become -1
  if jam:
    for x in range(BOARD_SIZE):
      for y in range(BOARD_SIZE-x):
        if  board_rotations[x, y] != 0 : board_rotations[x, y] = -1

  return board_rotations

  

board = initialize_board()
board[1, 0] = 1
board[1, 1] = 1
board[2, 1] = 2
board[0, 2] = 2
board[0, 1] = 2
print(board)
#print(board_to_adj_list(board))
rotations = turn_gear_clockwise(board, (0,0))
print(rotations)



###################
# GAME LOOP
###################
game_over = False
player_to_play = 1

while not game_over:

  # Player 1 turn
  if player_to_play == 1:
    #move = get_move_from_user(player_to_play)
    #print(move)
    player_to_play = 2

  game_over = True