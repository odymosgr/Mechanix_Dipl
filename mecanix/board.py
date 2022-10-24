import pygame
from .constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.blue_left = 12

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     for row in range(ROWS):
    #         for col in range(row % 2, ROWS, 2):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     k = ROWS - 1
    #     for row in range(ROWS):
    #         for col in range(k):
    #             pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    #
    #         k = k - 1
    #
    #         for col in range(0, row + 1):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_squares(self, win):
        win.fill(BLACK)
        k = COLS - 1
        n = 1
        for row in range(ROWS):
            for col in range(k//2):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            for col in range(n):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            for col in range(k//2):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
