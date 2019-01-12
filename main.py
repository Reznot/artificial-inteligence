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


def Astar(start_node, target_node, given_grid):
    start_node = start_node
    target_node = target_node
    A_grid = given_grid
    open_set = priorityQueue.PriorityQueue()
    closed_set = []
    current_node = None
    checked = False

    open_set.push(start_node, start_node.f_cost)

    while not open_set.isEmpty() and not current_node == target_node:
        current_node = open_set.pop()
        closed_set.append(current_node)

        neighbors = current_node.get_neighbors(A_grid)
        print(neighbors['e'].x)

            #TODO check_if_better


Astar(start, target, _grid)