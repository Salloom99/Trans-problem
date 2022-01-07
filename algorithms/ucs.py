from copy import deepcopy
from algorithms.terrain import Terrain


def ucs(start_point, end_point, cells):
    # initialize requirements
    terrain = Terrain(cells)

    best_path = {start_point: []} # where the best path get stored as directions
    costs = {start_point: 0}
    queue = [(0, start_point)]

    counter = 0 # counting the number of nodes that poped out of the q

    # start while loop
    while len(queue) != 0:
        node = queue.pop()
        counter += 1
        point = node[1]
        if point != end_point:
            for move in terrain.get_all_available_moves(point):
                next_point = move[0]
                direction = move[1]
                if next_point not in costs or costs[next_point] > costs[point] + 1:
                    queue.append((costs[point] + 1, next_point))
                    costs[next_point] = costs[point] + 1
                    current_path = deepcopy(best_path[point])
                    current_path.append(direction)
                    best_path[next_point] = current_path
            queue.sort(key=lambda a: a[0], reverse=True)
        else:
            break

    return best_path[end_point], counter


