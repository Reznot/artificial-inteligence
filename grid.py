import pygame
import numpy as np
import random
import math
import time


class Grid:
    rect_width = 20
    rect_height = 20
    rect_margin = 5

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BROWN = (165, 42, 42)
    YELLOW = (255, 191, 0)
    RED = (255, 0, 0)
    PURPLE = (191, 0, 255)

    def __init__(self, grid):
        self.table_nodes = []
        self.width = len(grid)
        self.height = len(grid)

        self.startX = 0
        self.startY = 0
        self.endX = self.width - 1
        self.endY = self.height - 1

        self.grid = np.zeros(shape=(self.width, self.height))

        for i in range(self.width):
          for j in range(self.height):
               if (i != 0 and j != 0) or (i != 19 and j != 19):
                isHouse = random.randint(0,20)
               if isHouse == 1:
                   self.grid[i][j] = 2
                   reachable = False

               else:
                   reachable = True
               n = random.randint(1, 3)
               e = random.randint(1, 3)
               w = random.randint(1, 3)
               s = random.randint(1, 3)
               self.table_nodes.append((Node(i, j, reachable, n, e, w, s)))

        # Start postion
        self.grid[0][0] = 1
        # time.sleep(5)  testing
        # self.grid[13][13] = 1

        self.grid[self.width - 1][self.height - 1] = 19


class Node:
    def __init__(self, x, y, reachable, n, e, w, s):
        self.reachable = reachable
        self.x = x
        self.y = y
        # costs of going in particular direction
        self.n = n
        self.e = e
        self.w = w
        self.s = s
        self.parent = None
        # cost function for Astar; Initially are infinite
        self.g_cost = math.inf
        self.h_cost = math.inf
        self.f = math.inf
        #self.garbage TODO add garbage picture to every node

        #Node.visited = np.zeros(shape=(Grid.width, Grid.height), dtype=bool)
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

        def manhattan_distance(start, target):
            return abs(start.x - target.x) + abs(start.y - target.y)

        #def check_node(self, current_node, target_node, direction):



# controls the size of the grid
input_grid = np.zeros(shape=(20, 20))


def make_grid(input_grid):
    grid = Grid(input_grid)
    return grid

#TODO wpierdol do grid od razu
make_grid(input_grid)