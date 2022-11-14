import pygame
import math
from .board import Board
from .constants import SQUARE_SIZE

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.board.create_board(self.win)
        self.turn = 'blue'
        self.valid_moves = {}

    def update(self):
        self.board.update_board(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def quit(self):
        pygame.quit()

    def move(self, row, col):
        gear = self.board.get_gear(row, col)
        if gear.fixed:
            print('oopsie daisy this gear is fixed to the board')
        elif gear.occupied:
            if self.turn == gear.color:
                self.board.move(gear, 'transparent', self.win)
            else:
                print("you can\'t place this here")
        else:
            self.board.move(gear, self.turn, self.win)
            print(self.turn, 'is playing')
            self.change_turn()

    def _move(self, row, col):
        gear = self.board.get_gear(row, col)
        if self.selected and gear == 'transparent':
            self.board.move(gear, self.turn, self.win)
        elif self.selected and gear.color == self.turn:
            self.board.move(gear, 'transparent', self.win)

    def change_turn(self):
        if self.turn == 'blue':
            self.turn = 'green'
        else:
            self.turn = 'blue'

    def convert_pos(self, ROWS):
        ROW, COL = 0,0
        m_x, m_y = pygame.mouse.get_pos()
        for row in range(ROWS):
            for col in range(row + 1):
                center_x, center_y = self.board.get_gear(row, col).x, self.board.get_gear(row, col).y
                dis = math.sqrt((center_x - m_x)**2 + (center_y - m_y)**2)
                if dis < SQUARE_SIZE//2:
                    ROW, COL = row, col
        print(ROW, COL)
        return ROW, COL
