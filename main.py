import grid
import numpy as np
import pathfinding as PF

input_grid = np.zeros(shape=(20, 20))
_grid = grid.Grid(input_grid)
PF.pathfinding(_grid)

start = _grid.table_nodes[0][0]
target = _grid.table_nodes[19][19]

start.set_start_node(target)

class Astar:
    def __init__(self, start_node, target_node):
        self.start = start_node
        self.target = target_node


    closedSet = []
    current_node = None
    checked = False

