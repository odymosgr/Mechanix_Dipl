import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(ROWS - row - 1):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_window(BOARD):
    BOARD.draw_squares(WIN)
    pygame.display.update()



def main():
    BOARD = Board()
    CLOCK = pygame.time.Clock()

    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == event.QUIT:
                run = False
        draw_window(BOARD)


