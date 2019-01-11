import grid
import numpy as np
import pathfinding as PF
import priorityQueue

input_grid = np.zeros(shape=(20, 20))
_grid = grid.Grid(input_grid)
PF.pathfinding(_grid)

start = _grid.table_nodes[0][0]
target = _grid.table_nodes[19][19]

start.set_start_node(target)

class Astar:
    def __init__(self, start_node, target_node, grid):
        self.start_node = start_node
        self.target_node = target_node
        self.A_grid = grid
        self.openSet = priorityQueue.PriorityQueue()
        self.closedSet = []
        self.current_node = None
        self.checked = False

        self.openSet.push(start_node, start_node.f_cost)


        while not self.openSet.isEmpty() and not self.current_node == target_node:
            self.current_node = self.openSet.pop()
            self.closedSet.append(self.current_node)

            neighbors = self.current_node.get_neighbors(self.A_grid)
            print(neighbors['e'].x)

Astar(start, target, _grid)