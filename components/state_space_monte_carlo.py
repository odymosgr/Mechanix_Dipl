from board import Board

def test(boardsize, iterations):
  illigal_positions = 0

  for i in range(iterations):
    b = Board(boardsize)
    b.random_population()
    if b.is_illigal(): illigal_positions += 1

  return illigal_positions/iterations



if __name__ == "__main__":
  for i in range(3):
    print(test(14, 20000))