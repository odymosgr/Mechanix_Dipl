import pygame
from mecanix.constants import WIDTH, HEIGHT
from mecanix.board import Board

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.draw_squares(WIN)
    board.draw_gear_mounts(WIN)
    board.create_board(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.update()
        pygame.display.update()


    pygame.quit()

main()


