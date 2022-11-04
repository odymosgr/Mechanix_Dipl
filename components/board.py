# Board is the graph the game is played on
# Vertices are the positions where the gears can be placed on
# Edges are the possible gear connections between positions

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




if __name__ == "__main__":
  b = Board(5)

  pos21 = b.array[1][2]
  pos11 = b.array[1][1]
  pos11.place_gear(Gear(1))
  
  b.array[b.size-1][0].display()
  pos21.display()
  print("2, 1 neighbours")
  for i in b.graph.nbrs(pos21): i.display()