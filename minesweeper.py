import pygame as pg
from dataclasses import dataclass
import numpy as np

w = 500
h = 500

GREY = ((198,198,198))
DARKGRAY = ((105, 105, 105))
BLACK = ((0,0,0))

bomb = pg.image.load('./assets/bomb.png')
flag = pg.image.load('./assets/flag.png')
screen = pg.display.set_mode((w, h))

pg.display.set_caption('Minesweeper')
pg.init()
pg.font.init()



clock = pg.time.Clock()
blockSize = 25
cornerPos = [[(x,y) for x in range(0, w, blockSize)] for y in range(0, h, blockSize)]

# array = np.zeros((w,h))
choices = [0, 1]
initialState = np.random.choice(choices, (w, h), p=[0.9, 0.1])


@dataclass
class Grid():
    def draw_grid(blockSize, initialState):
        for row, x in zip(initialState, range(0, w, blockSize)):
            for cell, y in zip(row, range(0, h, blockSize)):
                rect = pg.Rect(x, y, blockSize, blockSize)
                pg.draw.rect(screen, BLACK, rect, 1)

    def draw_on_click(button):
        pos = pg.mouse.get_pos()

        for i, cornerList in enumerate(cornerPos):
            for j, corner in enumerate(cornerList):
                if (i < len(cornerPos) and j < len(corner)) and (corner[0] <= pos[0]  <= cornerPos[i][j+1][0]) and (pos[1] <= cornerPos[i][j+1][1]):
                    x = cornerPos[i][j][0]
                    y = cornerPos[i-1][j][1]
                    posX = i
                    posY = j
                    break
                elif (corner[0] < pos[0] < w) and (corner[1] < pos[1] < h):
                    x = corner[0]
                    y = corner[1]
                    posX = i
                    posY = j
            else: continue
            break
        
        if button == 1:
            if initialState[posY][posX] == 0:
                cell = pg.Rect(x,y, blockSize, blockSize)
                pg.draw.rect(screen, GREY, cell)
                pg.display.update()
            else:
                screen.blit(bomb, (x, y))
                pg.display.update()
        elif button == 3:
            screen.blit(flag, (x, y))
            pg.display.update()

def main():
    gameOver = False

    screen.fill(DARKGRAY)
    while not gameOver:
        for e in pg.event.get():
            if e.type == pg.MOUSEBUTTONUP:
                Grid.draw_on_click(e.button)
            # if e.type == pg.MOUSEBUTTONUP and e.button == 3:
            #     Grid.draw_on_click(e.button)

        else:
            Grid.draw_grid(blockSize, initialState)
            pg.display.update()

if __name__ == '__main__':
    main()