import grid
import numpy as np
import pathfinding as PF
import priorityQueue
import math

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
    is_better = False
    path = []

    open_set.push(start_node)  # push start node into PQ

    while not open_set.isEmpty():  # and not current_node == target_node:
        current_node = open_set.pop()  # take node with lowest f_cost
        if current_node == target_node:
            break

        closed_set.append(current_node)  # push this node to closed list as it's expanded
        neighbors = current_node.get_neighbors(A_grid)

        for key in neighbors:
            if neighbors[key] not in closed_set:
                is_better = neighbors[key].check_if_better(current_node, target_node, key)
                if is_better:
                    open_set.push(neighbors[key])

    last = current_node
    print(last.x, last.y)
    if open_set.isEmpty():
        print("pusty")
    while current_node.parent != current_node:
        path.insert(0, current_node)
        current_node = current_node.parent

    return path


def convert_list_to_pq(list):
    pq = priorityQueue.PriorityQueue()
    for item in list:
        item.f_cost = item.manhattan_distance(target)
        pq.push(item)
    return pq


_grid.houses.append(target)
houses_set = _grid.houses  # previously it was PQ with houses
astar_path = []
node_from = start
while len(houses_set) != 0:  # not houses_set.isEmpty():  bo mialo byc lepiej; I CRY EVERYTIME
    node_to = houses_set.pop(0)
    node_to_temp = _grid.table_nodes[node_to.x][node_to.y]
    astar_path += Astar(node_from, node_to_temp, _grid)

    node_to_temp.h_cost = node_to_temp.manhattan_distance(target)
    node_to_temp.g_cost = 0
    node_to_temp.f_cost = node_to_temp.g_cost + node_to_temp.h_cost
    node_to_temp.parent = node_to_temp
    node_from = node_to_temp

# astar_path = Astar(start, target, _grid)
PF.pathfinding(_grid, astar_path)


# TODO losuj rodzaj materialu zbierany danego dnia;
# TODO podawaj obrazki z node z path; sprawdzaj czy zwrocony material jest taki jak zbierany danego dnia; jak tak to zbierz i dodaj fote do "zebrany_smieci"