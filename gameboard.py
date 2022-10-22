import pygame
from .pygameconstants import BLACK, ROWS, SQUARE_SIZE, FPS, WIN

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(ROWS - row - 1):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    BOARD = Board()
    CLOCK = pygame.time.Clock()

    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == event.QUIT:
                run = False

        BOARD.draw_squares(WIN)


