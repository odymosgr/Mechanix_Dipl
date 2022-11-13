import pygame
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

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

    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            gear = self.board.get_gear(row, col)
            if gear != None and gear.color == self.turn:
                self.selected = gear
                self.valid_moves = self.board.get_valid_moves(gear)
                return True
        return False


    def move(self, row, col):
        pass

    def change_turn(self):
        if self.turn == 'blue':
            self.turn = 'green'
        else:
            self.turn = 'blue'
