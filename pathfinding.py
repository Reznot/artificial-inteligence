import pygame
import numpy as np
from grid import Grid
from grid import Node
from grid import make_grid


def pathfinding(Grid):
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (510, 510)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pathfinding")

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
        for column in range(Grid.width):
            for row in range(Grid.height):
                color = Grid.WHITE
                # set the start and end positions to green and red respectively
                if Grid.grid[row][column] == 1:
                    color = Grid.GREEN
                elif Grid.grid[row][column] == 19:
                    color = Grid.RED
                pygame.draw.rect(screen, color, [(Grid.rect_margin + Grid.rect_width) * column + Grid.rect_margin,
                                                 (Grid.rect_margin + Grid.rect_width) * row + Grid.rect_margin,
                                                 Grid.rect_width, Grid.rect_height])

        start_x = Grid.startX
        start_y = Grid.startY

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


# create new Grid object for testing
input_grid = np.zeros(shape=(20, 20))
Grid = make_grid(input_grid)

pathfinding(Grid)