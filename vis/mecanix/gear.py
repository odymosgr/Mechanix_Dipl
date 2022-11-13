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
        elif self.color == 'green':
            self.image = GREENGEAR
            self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
        elif self.color == 'blue':
            self.image = BLUEGEAR
            self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def make_jammed(self):
        self.jammed = True

    def make_fixed(self):
        self.fixed = True

    def draw(self, win):
        # pygame.draw.rect(win, RED, (self.x, self.y, SQUARE_SIZE//4, SQUARE_SIZE//4))
        win.blit(self.image, (self.x, self.y))
        # if not self.jammed:
        #     pass


