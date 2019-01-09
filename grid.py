import pygame
import numpy as np
import random


class Grid:
    rect_width = 20
    rect_height = 20
    rect_margin = 5

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BROWN = (165, 42, 42)
    RED = (255, 0, 0)

    def __init__(self, grid):
        Grid.cells = []
        Grid.width = len(grid)
        Grid.height = len(grid)

        Grid.startX = 0
        Grid.startY = 0
        Grid.endX = self.width - 1
        Grid.endY = self.height - 1

        # domki = (())

        #for i in range(Grid.width):
        #   for j in range(Grid.height):
        #        if (i, j) in domki:
        #            reachable = False
        #        else:
        #            reachable = True
        #            Grid.n = random.randint(1, 3)
        #            Grid.e = random.randint(1, 3)
        #            Grid.w = random.randint(1, 3)
        #            Grid.s = random.randint(1, 3)
        #            Grid.cost = random.randint(1, 3)
        #        Grid.cells.append((Node(i, j, reachable, n, e, w, s, cost)))

        Grid.grid = np.zeros(shape=(self.width, self.height))
        # Start postion
        Grid.grid[0][0] = 1
        Grid.grid[self.width - 1][self.height - 1] = 19


class Node:
    def __init__(self, x, y, reachable, n, e, w, s, moveCost):
        Node.reachable = reachable
        Node.x = x
        Node.y = y
        # costs of going in particular direction
        Node.n = n
        Node.e = e
        Node.w = w
        Node.s = s
        # finalMoveCost = direction * penalty
        Node.carMoveCost = moveCost
        Node.visited = np.zeros(shape=(Grid.width, Grid.height), dtype=bool)
        # Position.Neighbors = [None,None,None,None]

        def get_neighbors(Node):
            neighbors = []
            if Node.x < Grid.width - 1:
                neighbors.append(Node.x + 1, Node.y)
            if Node.x > 0:
                neighbors.append(Node.x - 1, Node.y)
            if Node.y < Grid.height - 1:
                neighbors.append(Node.x, Node.y + 1)
            if Node.y > 0:
                neighbors.append(Node.x, Node.y - 1)
            return neighbors

        def is_visited(Node):
            if Node.visited[Node.x][Node.y] is True:
                return True
            return False

        def visit(Node):
            Node.visited[Node.x][Node.y] = True


        # controls the size of the grid
input_grid = np.zeros(shape=(20, 20))


def make_grid(input_grid):
    grid = Grid(input_grid)
    return grid


make_grid(input_grid)