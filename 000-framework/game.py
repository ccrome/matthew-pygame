import sys
import pygame
from pygame.locals import QUIT
import numpy as np

# We'll define a few colors for later
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#  Use parameters to control the dimensions
#  make cols different from rows, so we're sure to catch
#  any errors with accidentially swapping.  Can always change later.
nrows = 4
ncols = 3

# How many pixels across will each grid be?
gridsize = 100

grid = np.zeros((nrows, ncols), dtype=int)
grid[0, 0]             = 1
grid[0, ncols-1]       = 2
grid[nrows-1, 0]       = 3
grid[nrows-1, ncols-1] = 4

# print(grid)
# When you print this out, it looks like:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
# So, yes, we got rows and columsn correct.


def grid_rect(row, col):
    """Return the x and y coordinates of a rectangle at
    location (row, col)"""
    return (gridsize*col, gridsize*row, gridsize, gridsize)


def draw_square(surface, row, col, value):
    rect = grid_rect(row, col)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f'{value}', True, BLUE)
    text_rect = text.get_rect()
    text_rect.center = (rect[0]+gridsize//2, rect[1]+gridsize//2)
    surface.blit(text, text_rect)


def draw_grid():
    global surface
    global grid
    for row in range(nrows):
        for col in range(ncols):
            pygame.draw.rect(
                surface,   # Draw onto the surface returned by set_mode
                YELLOW,    # Make it yellow
                grid_rect(row, col),  # get pixel locaiton
                1)  # don't fill
            draw_square(surface, row, col, grid[row, col])


def main_loop():
    global grid
    quitting = False
    while not quitting:  # main game loop.  It runs forever
        for event in pygame.event.get():
            do_game_logic(grid)
            surface.fill(BLACK)
            draw_grid()
            pygame.display.update()
            if event.type == QUIT:
                quitting = True
                print("Bye Bye")


def init_game():
    global surface
    pygame.init()  # you need to initialize pygame with this call
    # Set the window size.  right now it will be exactly big enough to
    # fit our grid.
    surface = pygame.display.set_mode((ncols*gridsize, nrows*gridsize))
    # Set the window title
    pygame.display.set_caption("Hello World")


def do_game_logic(grid):
    # This is where we'll fill in somethign to make the game happen.
    # you just have to modify the grid object so that numbers move
    # around.
    pass  # Pass is for when you don't have anything to do yet.  without it would be a syntax error


def main():
    init_game()
    main_loop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
