import pygame
from Tetromino import *


class Tetris:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def render(self):
        self.draw_grid()

    def draw_grid(self):
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.game.window, (255, 255, 255), rect, 1)

    def new_tetromino(self):
        tetromino = Tetromino('I', (255, 0, 0))
