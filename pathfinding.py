import pygame
import numpy as np
from grid import Grid
from grid import Node
from grid import make_grid
import time


def pathfinding(Grid, path):
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (510, 510)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TESLA MODEL G: GARBAGE TRUCK")

    # Loop until the user clicks the close button.
    done = False

    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(Grid.BLACK)

        # Draw the initial grid
        for node in path:
            pygame.time.delay(150)
            if node.x + node.y != 38 and Grid.grid[node.x][node.y] != 3 and Grid.grid[node.x][node.y] != 5 and Grid.grid[node.x][node.y] != 99:
                Grid.grid[node.x][node.y] = 10  #  Truck  (previously 10 for light blue
            if Grid.grid[node.x][node.y] == 3:
                    Grid.grid[node.x][node.y] = 5
            for column in range(Grid.width):
                for row in range(Grid.height):
                    color = Grid.WHITE

                    # # color the path
                    # for node in path:
                    #     if node.x + node.y != 38:
                    #         Grid.grid[node.x][node.y] = 10
                    # set the start and end positions to green and red respectively
                    if Grid.grid[row][column] == 1:
                        color = Grid.GREEN
                    elif Grid.grid[row][column] == 19:
                        color = Grid.RED
                    elif Grid.grid[row][column] == 2:  # Obstacle
                        color = Grid.PURPLE
                    elif Grid.grid[row][column] == 10:  # Path
                        color = Grid.LIGHT_BLUE
                    elif Grid.grid[row][column] == 3:  # House
                        color = Grid.YELLOW
                    elif Grid.grid[row][column] == 5:  # Visited House
                        color = Grid.PINK
                    elif Grid.grid[row][column] == 15:
                        color = Grid.ORANGE
                    elif Grid.grid[row][column] == 99:
                        color = Grid.BLUE
                    elif Grid.grid[row][column] == 100:
                        color = Grid.BLACK
                    pygame.draw.rect(screen, color, [(Grid.rect_margin + Grid.rect_width) * column + Grid.rect_margin,
                                                     (Grid.rect_margin + Grid.rect_width) * row + Grid.rect_margin,
                                                     Grid.rect_width, Grid.rect_height])
                    pygame.display.flip()


#TODO animowanie przechodzacej smieciarki i otwieranie tych obrazkow ze smieciami
        start_x = Grid.startX
        start_y = Grid.startY

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


# # create new Grid object for testing
# input_grid = np.zeros(shape=(20, 20))
# Grid = make_grid(input_grid)
#
# pathfinding(Grid)