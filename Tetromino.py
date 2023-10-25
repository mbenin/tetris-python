import pygame
from settings import *


class Tetromino:
    def __init__(self, shape, color):
        self.shape = TETROMINOS[shape]
        self.color = color
        self.rotation = 0
        self.w = len(self.shape[0])
        self.h = len(self.shape)

        self.blocks = []




        self.__create_blocks()

    def __create_blocks(self):
        for (line, row) in enumerate(self.shape):
            for (column, value) in enumerate(row):
                if value:
                    self.coords.append((line, column))

