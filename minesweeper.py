import pygame as pg
from dataclasses import dataclass
import numpy as np

w = 500
h = 500
screen = pg.display.set_mode((w, h))

pg.display.set_caption('Minesweeper')
pg.init()
pg.font.init()

clock = pg.time.Clock()
blockSize = 25

initialState = np.zeros((w,h))

@dataclass
class Grid():
    def draw_grid(blockSize, initialState):
        for row, x in zip(initialState, range(0, w, blockSize)):
            for col, y in zip(row, range(0, h, blockSize)):
                rect = pg.Rect(x, y, blockSize, blockSize)
                pg.draw.rect(screen, (( 100,100,100 )), rect, 5)
def main():
    # print('just a test')

    gameOver = False

    while not gameOver:
        for e in pg.event.get():
            print('asdf')
        else:
            Grid.draw_grid(blockSize, initialState)
            pg.display.update()

if __name__ == '__main__':
    main()