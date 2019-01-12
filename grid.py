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
        self.table_nodes = [[0 for x in range(20)] for y in range(20)]
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
                isHouse = random.randint(0,12)
               if isHouse == 1:
                   self.grid[i][j] = 2
                   reachable = False

               else:
                   reachable = True
               n = random.randint(1, 3)
               e = random.randint(1, 3)
               w = random.randint(1, 3)
               s = random.randint(1, 3)
               #self.table_nodes.append((Node(i, j, reachable, n, e, w, s)))
               self.table_nodes[i][j] = Node(i, j, reachable, n, e, w, s)

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
        self.f_cost = math.inf
        #self.garbage TODO add garbage picture to every node

        #Node.visited = np.zeros(shape=(Grid.width, Grid.height), dtype=bool)
        # Position.Neighbors = [None,None,None,None]


        def is_visited(Node):
            if Node.visited[Node.x][Node.y] is True:
                return True
            return False

        def visit(Node):
            Node.visited[Node.x][Node.y] = True

    def manhattan_distance(self, target):
        return abs(self.x - target.x) + abs(self.y - target.y)

    def set_start_node(self, target):
        self.g_cost = 0
        self.h_cost = self.manhattan_distance(target)
        self.f_cost = self.g_cost + self.h_cost
        self.parent = self

    def get_neighbors(current_node, grid):
        neighbors = dict()
        # Go west
        if current_node.x > 0:
            neighbors['w'] = grid.table_nodes[current_node.x-1][current_node.y]
        # Go north
        if current_node.y > 0:
            neighbors['n'] = grid.table_nodes[current_node.x][current_node.y-1]
        # Go east
        if current_node.x < 19:
            neighbors['e'] = grid.table_nodes[current_node.x+1][current_node.y]
        # Go south
        if current_node.y < 19:
            neighbors['s'] = grid.table_nodes[current_node.x][current_node.y+1]
        return neighbors

    def check_if_better(self, current_node, target_node, direction):
        if direction == 'w':
            g = current_node.g_cost + current_node.w
        elif direction == 'n':
            g = current_node.g_cost + current_node.n
        elif direction == 'e':
            g = current_node.g_cost + current_node.e
        elif direction == 's':
            g = current_node.g_cost + current_node.s

        h = self.manhattan_distance(target_node)
        if (g + h) <= current_node.f_cost:
            self.g_cost = g
            self.h_cost = h
            self.f_cost = g + h
            self.parent = current_node
            return True
        return False


# controls the size of the grid
input_grid = np.zeros(shape=(20, 20))


def make_grid(input_grid):
    grid = Grid(input_grid)
    return grid

#TODO wpierdol do grid od razu
make_grid(input_grid)