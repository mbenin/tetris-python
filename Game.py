import pygame
from settings import *
from Tetris import *

class Game:

    def __init__(self, width, height):
        pygame.init()
        self.window = pygame.display.set_mode((BOARD_WIDTH * BLOCK_SIZE, BOARD_HEIGHT * BLOCK_SIZE))
        self.running = True
        self.tetris = Tetris(self)
        self.tetris.new_tetromino()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                break

    def run(self):
        while self.running:
            self.update()
            self.render()

    def render(self):
        self.window.fill(BACKGROUND_COLOR)
        self.tetris.render()
        pygame.display.update()

    def __del__(self):
        pygame.quit()
