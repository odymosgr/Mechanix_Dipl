# Position of a board has coordinates X Y
# and can have a gear occuping it

from gear import Gear

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.occupied_by = None

  def is_occupied(self):
    if self.occupied_by == None: return False
    return True

  def place_gear(self, gear):
    self.occupied_by = gear

  def take_gear(self):
    if not self.occupied_by.is_transportable(): return None
    t = self.occupied_by
    self.occupied_by = None
    return t
  
  def display(self):
    text = "empty"
    if self.is_occupied(): text = f"occupied by a {self.occupied_by.color} gear"

    print(f"Position [{self.x},{self.y}] is {text}")

if __name__ == "__main__":
  g = Gear(2)
  pos = Position(0,0)
  pos.place_gear(g)
  pos.display()
  removed_g = pos.take_gear()
  removed_g.print_info()