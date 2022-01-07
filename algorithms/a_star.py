from copy import deepcopy
from .terrain import Terrain
from .node import Node

def a_star(start_point, end_point, cells):
    # initialize requirements
    terrain = Terrain(cells)

    start_dist = terrain.get_manhattan_distance(start_point, end_point)
    queue = [Node(start_point,0,start_dist)] # open list
    visited = {} # closed list
    best_path = {start_point: []} # where the best path get stored as directions

    counter = 0 # counting the number of nodes that poped out of the q
    
    # start while loop
    while len(queue) != 0:
        node = queue.pop()
        counter += 1
        point = node.point
        visited[point] = node.g + node.h
        if point != end_point:
            for move in terrain.get_all_available_moves(point):
                next_point = move[0]
                direction = move[1]
                next_dist = terrain.get_manhattan_distance(next_point, end_point)
                next_point_not_exists = len([node for node in queue if node.point == next_point]) == 0
                if next_point not in visited and next_point_not_exists:
                    queue.append(Node(next_point, node.g + 1, next_dist))
                    current_path = deepcopy(best_path[point])
                    current_path.append(direction)
                    best_path[next_point] = current_path
            queue.sort(key=lambda node: node.f, reverse=True)
        else:
            break
    return best_path[end_point], counter