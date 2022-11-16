# Board is the graph the game is played on
# Vertices are the positions where the gears can be placed on
# Edges are the possible gear connections between positions

import random

from gear import Gear
from position import Position
from graph import Graph

class Board:
  
  def __init__ (self, size = 10, type = 'triangular'):
    if type != 'triangular': return None

    self.size = size
    self.type = type

    # array[y][x]
    self.array = []

    for y in range(size):
      row = []
      for x in range(size-y):
        #print(f"iteration x={x} y={y}")
        row.append(Position(x,y))
      self.array.append(row)
    
    self.array[0][0].place_gear(Gear(1, False))
    self.array[0][size-1].place_gear(Gear(2, False))
    self.array[size-1][0].place_gear(Gear(3, False))

    vertices = [pos for row in self.array for pos in row]
    connections = set()
    
    for y in range(size):
      for x in range(size-y):
        # top left
        if x != 0:
          connections.add((self.array[y][x], self.array[y+1][x-1]))
        # left
          connections.add((self.array[y][x], self.array[y][x-1]))
        # top right
        if x != size-y-1:
          connections.add((self.array[y][x], self.array[y+1][x]))
        # right
          connections.add((self.array[y][x], self.array[y][x+1]))
        # bottom left
        if y != 0:
          connections.add((self.array[y][x], self.array[y-1][x]))
        # bottom right
          connections.add((self.array[y][x], self.array[y-1][x+1]))

    self.graph = Graph(vertices, connections)

  def player_subgraph(self, player):
    adj_dict = self.graph.adj_dict()
    pos_list = list(adj_dict.keys())
    gear_list = [i for i in pos_list if i.is_occupied() and i.occupied_by.type == player]

    new_edges = []
    for i in gear_list:
      adj_vertices = adj_dict.get(i)
      adj_gears = [i for i in adj_vertices if i.is_occupied() and i.occupied_by.type == player]
      v_edges = [(i, t2) for t2 in adj_gears]
      new_edges = new_edges + v_edges

    return Graph(gear_list, new_edges)

  def is_illigal(self):
    subg1 = self.player_subgraph(1)
    subg2 = self.player_subgraph(2)
    bsize = self.size

    p01 = self.array[0][1]
    p10 = self.array[1][0]
    p0s = self.array[0][bsize-2]
    p1s = self.array[1][bsize-2]
    ps0 = self.array[bsize-2][0]
    ps1 = self.array[bsize-2][1]

    if p01.is_occupied() and p10.is_occupied() and p01.occupied_by.type == p10.occupied_by.type: 
      return True
    if p0s.is_occupied() and p1s.is_occupied() and p0s.occupied_by.type == p1s.occupied_by.type: 
      return True
    if ps0.is_occupied() and ps1.is_occupied() and ps0.occupied_by.type == ps1.occupied_by.type: 
      return True

    if not subg1.is_bipartite():
      return True
    if not subg2.is_bipartite():
      return True

    return False
  
  def print_spin_array(self):
    spin_array = []
    for y in range(len(self.array)):
      spin_array.append([])
      for x in range(len(self.array[y])):
        if not self.array[y][x].is_occupied(): spin_array[y].append(0)
        else : spin_array[y].append(self.array[y][x].occupied_by.get_rotation())
    
    for y in range(len(self.array)):
      print(spin_array[self.size - y -1])

  def print_board(self):
    print_array = []
    for y in range(len(self.array)):
      print_array.append([])
      for x in range(len(self.array[y])):
        if not self.array[y][x].is_occupied(): print_array[y].append(0)
        else : print_array[y].append(self.array[y][x].occupied_by.type)
    
    for y in range(len(self.array)):
      print(print_array[self.size - y -1])

  def random_population(self):
    poslist = list(self.graph.adj_dict().keys())
    for pos in poslist:
      if pos.is_occupied(): continue
      num = random.randrange(0, 3)
      if num == 0: continue
      pos.place_gear(Gear(num))
      


if __name__ == "__main__":
  # b = Board(5)
  # b.array[0][1].place_gear(Gear(1))
  # b.array[1][1].place_gear(Gear(1))
  # b.array[1][2].place_gear(Gear(2))

  # b.array[3][0].place_gear(Gear(2))
  # b.array[3][1].place_gear(Gear(2))
  # b.array[0][2].place_gear(Gear(1))
  # b.print_board()
  # print("is board illigal? = "+str(b.is_illigal()))

  for i in range(10):
    print(random.randrange(0, 3))