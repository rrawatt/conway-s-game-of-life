'''
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
'''

import random
import pygame
from pygame.locals import *

pygame.init()

ivory = (255, 255, 240)
spaceblue = (31, 40, 45)

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("conway's game")

class Cell:
    width = 20
    height = 20

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_cell(self):
        color = ivory if self.state == 1 else spaceblue
        pygame.draw.rect(WIN, color, self.rect, border_radius=10)

def neighcount(dict, tup):
    count = 0
    for i in range(-20, 40, 20):
        for j in range(-20, 40, 20):
            if dict.get((tup[0] + i, tup[1] + j), None) and dict[(tup[0] + i, tup[1] + j)].state == 1:
                count += 1
    return count

def aliveornot(dict, tup):
    count = neighcount(dict, tup)
    if dict[tup].state == 1 and (count < 2 or count > 3):
        dict[tup].state = 0
    elif dict[tup].state == 0 and count == 3:
        dict[tup].state = 1

cell_dict = {}  # Dictionary to store Cell instances

for i in range(0, 801, 20):
    for j in range(0, 801, 20):
        state = random.choices([0, 1], [15, 1])[0]
        cell_dict[(i, j)] = Cell(i, j, state)

def main():
    run = True
    clock = pygame.time.Clock()
    fps = 10  # Set the desired frame rate

    while run:
        WIN.fill(spaceblue)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break

        updated_dict = dict(cell_dict)  # Create a copy of the dictionary to avoid modifying it while iterating
        for cell in cell_dict.keys():
            if cell[0] == 0 or cell[1] == 0 or cell[0] == 800 or cell[1] == 800:
                pass
            else:
                aliveornot(updated_dict, cell)

        # Update the original dictionary with the changes
        cell_dict.update(updated_dict)

        # Draw the updated cells
        for cell in cell_dict.values():
            cell.draw_cell()

        pygame.display.update()
        clock.tick(fps)  # Control the frame rate

    pygame.quit()

if __name__ == '__main__':
    main()
