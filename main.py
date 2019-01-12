import grid
import numpy as np
import pathfinding as PF
import priorityQueue

# initialize grid
input_grid = np.zeros(shape=(20, 20))
_grid = grid.Grid(input_grid)
# start and destination nodes
start = _grid.table_nodes[0][0]
target = _grid.table_nodes[19][19]
# set properties of a start node/ parent and costs functions
start.set_start_node(target)


def Astar(start_node, target_node, given_grid):
    start_node = start_node
    target_node = target_node
    A_grid = given_grid
    open_set = priorityQueue.PriorityQueue()
    closed_set = []
    current_node = None
    checked = False

    open_set.push(start_node, start_node.f_cost)  # push start node into PQ

    while not open_set.isEmpty() and not current_node == target_node:
        current_node = open_set.pop()  # take node with lowest f_cost
        closed_set.append(current_node)  # push this node to closed list as it's expanded

        neighbors = current_node.get_neighbors(A_grid)

        for key in neighbors:
            print(neighbors[key].x)

            #TODO check_if_better


Astar(start, target, _grid)
PF.pathfinding(_grid)