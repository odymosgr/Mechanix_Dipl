# A gear has a type {1, 2, 3} for {players1, players2, goal}
# has a color {blue, red, yellow} 
# has property transportable denoting its ability to change positions on the board
# has property rotation_of_motion {0, 1, 2, -1} denoting {not_rotating, clockwise, anticlockwise, jammed}

class Gear:

  # type = {1, 2, 3}
  def __init__(self, type, transportable = True):
    self.type = type
    if type == 1: self.color = 'blue'
    elif type == 2: self.color = 'red'
    elif type == 3: self.color = 'yellow'
    else : print('Error: gear initialization with wrong type: ' + str(type))
    
    self.transportable = transportable
    self.rotation_of_motion = 0

  def is_transportable(self):
    return self.transportable
  
  def print_info(self):
    print('Gear info :')
    if self.type == 1: print("- player's 1 gear")
    elif self.type == 2: print("- player's 2 gear")
    elif self.type == 3: print("- goal gear")
    print('- type = '+str(self.type))
    print('- color = '+str(self.color))
    print('- transportable = '+str(self.transportable))
    print('- rotation_of_motion = '+str(self.rotation_of_motion))