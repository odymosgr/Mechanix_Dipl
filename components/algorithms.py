
from gear import Gear
from position import Position
from graph import Graph
from board import Board

def board_to_chains_graph (board):
  adj_dict = board.graph.adj_dict()
  pos_list = list(adj_dict.keys())
  gear_list = [i for i in pos_list if i.is_occupied()]

  new_edges = []
  for i in gear_list:
    adj_vertices = adj_dict.get(i)
    adj_gears = [i for i in adj_vertices if i.is_occupied()]
    v_edges = [(i, t2) for t2 in adj_gears]
    new_edges = new_edges + v_edges

  return Graph(gear_list, new_edges)

def board_to_chain_list (board):
  chains = board_to_chains_graph (board)
  adj_dict = chains.adj_dict()
  pos_list = list(adj_dict.keys())

  visited = set()
  ccs_v = []
  queue = []


  for i in pos_list:
    if i in visited: continue
    queue.append(i)

    cc_v = set()
    while queue:
      current_node = queue.pop()
      visited.add(current_node)
      cc_v.add(current_node)
      for nbr in adj_dict[current_node]:
        if nbr not in visited: queue.append(nbr)
    ccs_v.append(cc_v)
  
  chain_list = []
  for i in ccs_v :
    cc_edges = []
    for v in i :
      cc_edges = cc_edges + [(v, t2) for t2 in adj_dict[v]]
    chain_list.append(Graph(i,cc_edges))
  
  # for i in chain_list:
  #   print(i.adj_dict())

  return chain_list

def board_to_player_subgraph (board, player):
  adj_dict = board.graph.adj_dict()
  pos_list = list(adj_dict.keys())
  gear_list = [i for i in pos_list if i.is_occupied() and i.occupied_by.type == player]

  new_edges = []
  for i in gear_list:
    adj_vertices = adj_dict.get(i)
    adj_gears = [i for i in adj_vertices if i.is_occupied() and i.occupied_by.type == player]
    v_edges = [(i, t2) for t2 in adj_gears]
    new_edges = new_edges + v_edges

  return Graph(gear_list, new_edges)

def turn_gear_on_pos (board, pos):
  if not pos.is_occupied(): return

  chains = board_to_chains_graph(board)
  adj_list = chains.adj_dict()

  pos.occupied_by.set_rotation(1)
  bfs_queue = [pos]
  visited = set()
  jam = False

  while bfs_queue:
    node = bfs_queue.pop(0)

    for nbr in adj_list[node]:
      if nbr.occupied_by.get_rotation() == node.occupied_by.get_rotation(): jam = True
      if nbr not in visited:
        opp_rot = 1+(2-node.occupied_by.get_rotation())%2
        nbr.occupied_by.set_rotation(opp_rot)
        bfs_queue.append(nbr)
    visited.add(node)

  if jam :
    for gpos in list(adj_list.keys()):
      if gpos.occupied_by.get_rotation() != 0: gpos.occupied_by.set_rotation(-1)


def board_stop_gears(board):
  pos_list = list(board.graph.adj_dict().keys())
  for p in pos_list:
    if p.is_occupied(): p.occupied_by.set_rotation(0)

def is_graph_bipartite(g):
  adjdict = g.adj_dict()
  vertices = list(adjdict.keys())

  set1 = set()
  set2 = set()

  for v in vertices:
    if v not in set2:
      set1.add(v)
      for nbr in adjdict[v]:
        if nbr in set1: return False
        set2.add(nbr)
    else:
      for nbr in adjdict[v]:
        if nbr in set2: return False
        set1.add(nbr)
  return True

def is_board_illigal(board):
  subg1 = board_to_player_subgraph(board, 1)
  subg2 = board_to_player_subgraph(board, 2)
  bsize = board.size

  p01 = board.array[0][1]
  p10 = board.array[1][0]
  p0s = board.array[0][bsize-2]
  p1s = board.array[1][bsize-2]
  ps0 = board.array[bsize-2][0]
  ps1 = board.array[bsize-2][1]

  if p01.is_occupied() and p10.is_occupied() and p01.occupied_by.type == p10.occupied_by.type: 
    return True
  if p0s.is_occupied() and p1s.is_occupied() and p0s.occupied_by.type == p1s.occupied_by.type: 
    return True
  if ps0.is_occupied() and ps1.is_occupied() and ps0.occupied_by.type == ps1.occupied_by.type: 
    return True

  if not is_graph_bipartite(subg1):
    return True
  if not is_graph_bipartite(subg2):
    return True

  return False




if __name__ == "__main__":
  b = Board(5)
  b.array[0][1].place_gear(Gear(1))
  b.array[1][1].place_gear(Gear(1))
  b.array[1][2].place_gear(Gear(2))

  # chains = board_to_chains_graph(b)
  # for i in chains.nbrs(b.array[0][0]): print(i)

  # b.array[0][1].occupied_by.set_rotation(1)
  # b.print_spin_array()

  # board_to_chain_list(b)

  # p1_gears = board_to_player_subgraph(b, 1)
  # print(p1_gears.adj_dict())

  # turn_gear_on_pos(b, b.array[0][0])
  # turn_gear_on_pos(b, b.array[4][0])
  # b.print_spin_array()
  # board_stop_gears(b)
  # b.print_spin_array()

  # b.array[3][0].place_gear(Gear(2))
  # b.array[3][1].place_gear(Gear(2))
  # b.print_board()
  # print("is board illigal? = "+str(is_board_illigal(b)))