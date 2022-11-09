from .constants import SQUARE_SIZE, RED, TRANSPARENT, WHITE, BLUEGEAR, GREENGEAR, TARGETGEAR
import pygame

class Gear(pygame.sprite.Sprite):
    def __init__(self, row, col, color, x, y, image):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.row = row
        self.col = col
        self.color = color
        self.jammed = False
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color
        if self.color == 'transparent':
            pass
        elif self.color == 'green':
            self.image = GREENGEAR
        else:
            self.image = BLUEGEAR


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def calc_pos(self):
        # self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        # self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2
        pass

    def make_jammed(self):
        self.jammed = True

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.x, self.y, SQUARE_SIZE//4, SQUARE_SIZE//4))
        if not self.jammed:
            pass

    def __repr__(self):
        if self.jammed:
            return 'Jammed!'
        else:
            return 'Not Jammed!'
