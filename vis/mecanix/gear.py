from .constants import SQUARE_SIZE, TRANSPARENT, BLUEGEAR, GREENGEAR
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
        self.previous = 'transparent'
        self.occupied = False
        self.jammed = False
        self.fixed = False
        self.x = x
        self.y = y

    def __repr__(self):
        out = ''
        if self.jammed:
            out += 'Jammed!'
        else:
            out += 'Not Jammed!'
        if self.fixed:
            out += 'and Fixed!'
        else:
            out += 'and Not Fixed!'
        return out

    def set_color(self, color):
        self.color = color
        if self.color == 'transparent':
            self.image = TRANSPARENT
            self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.make_jammed()
            self.make_occupied()
        elif self.color == 'green':
            self.image = GREENGEAR
            self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.make_occupied()
        elif self.color == 'blue':
            self.image = BLUEGEAR
            self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.make_occupied()

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def make_jammed(self):
        if self.jammed:
            self.jammed = True
        else:
            self.jammed = False

    def make_fixed(self):
            self.fixed = True

    def make_occupied(self):
        if self.occupied:
            self.occupied = False
        else:
            self.occupied = True

    def draw(self, win):
        # pygame.draw.rect(win, RED, (self.x, self.y, SQUARE_SIZE//4, SQUARE_SIZE//4))
        win.blit(self.image, (self.x, self.y))
        # if not self.jammed:
        #     pass


