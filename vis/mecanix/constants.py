import pygame
import os

#Game
WIDTH, HEIGHT = 1400, 1000
ROWS, COLS = 10,10
SQUARE_SIZE = 80
MOUNT_SIZE = SQUARE_SIZE//4

#RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

#Images
BLUEGEAR = pygame.image.load(os.path.join('vis', 'assets', 'blue-gear-md.png'))
GREENGEAR = pygame.image.load(os.path.join('vis', 'assets', 'imagination-movers-gears-md.png'))
TARGETGEAR = pygame.image.load(os.path.join('vis', 'assets', 'green-gear.svg.med.png'))
TRANSPARENT = pygame.image.load(os.path.join('vis', 'assets', 'block.png'))
