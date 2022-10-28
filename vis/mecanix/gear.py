from .constants import *

class Gear:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.jammed = False
        self.x = 0
        self.y = 0

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def make_jammed(self):
        self.jammed = True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE//2, SQUARE_SIZE//2))
        if not self.jammed:
            pass
