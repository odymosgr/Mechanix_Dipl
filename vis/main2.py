import pygame
from mecanix.constants import WIDTH, HEIGHT, ROWS
from mecanix.game import Game

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = game.convert_pos(ROWS)
                game.move(row, col)

        game.update()


    game.quit()

main()


