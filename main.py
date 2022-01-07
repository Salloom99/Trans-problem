from timeit import default_timer as timer
from algorithms.solution import Solution
from map_stuff.map import Map
from algorithms.a_star import a_star
from algorithms.ucs import ucs
from itertools import permutations
from time import sleep
import os

maps = {
    'training': Map('maps/training_map.txt'),
    'standard': Map('maps/standard_test.txt'),
    'map1': Map('maps/test1.txt'),
    'map2': Map('maps/test2.txt'),
    'map3': Map('maps/test3.txt'),
}

def get_best_solution(map, search_algo):
    best_sol = None
    best_cost = 1000
    
    storages = []
    storages.extend(map.producers)
    storages.extend(map.destinations)
    combs = permutations(storages, len(storages))
    
    for comb in combs:
        sol = Solution(comb, map, search_algo)
        if sol.is_valid and sol.cost < best_cost:
            best_sol = sol
            best_cost = sol.cost
                    
    # print(best_sol.commands)
    # print(f'{best_sol.nodes_number} nodes processed')
    # print(f'{best_sol.cost} cost')
    # print(f'{best_sol.time:.2f} milliseconds')
    return best_sol

def excute_commands(commands, map):
    for command in commands:
        os.system('cls')
        print(map.real_time())
        map.let_truck_do(command)
        sleep(1)

    os.system('cls')
    print(map.real_time())
    sleep(0.5)

def first_hur(truck, point, map, search_algo):
    start_time = timer() * 1000
    path, nodes = search_algo((truck.row, truck.col), point, map.cells)
    cost = len(path)
    end_time = timer() * 1000
    time = end_time - start_time
    return nodes, cost, time

def second_hur(package_id, map, search_algo):
    start_time = timer() * 1000
    producer = map.get_producer(package_id)
    destination = map.get_destination(package_id)
    result1 = search_algo((map.truck.row, map.truck.col), (producer.row, producer.col), map.cells)
    result2 = search_algo((producer.row, producer.col), (destination.row, destination.col), map.cells)
    result3 = search_algo((destination.row, destination.col), (map.truck.row, map.truck.col), map.cells)
    path = result1[0] + result2[0] + result3[0]
    nodes = result1[1] + result2[1] + result3[1]
    cost = len(path) + len(result2[0])
    end_time = timer() * 1000
    time = end_time - start_time
    return nodes, cost, time
    
def third_hur(map, search_algo):
    worst_cost = 0
    worst_nodes = 0
    start_time = timer() * 1000
    for package_id, _ in enumerate(map.producers):
        nodes, cost, time = second_hur(package_id, map, search_algo)
        if cost > worst_cost:
            worst_cost = cost
            worst_nodes = nodes
    end_time = timer() * 1000
    time = end_time - start_time
    return worst_nodes, worst_cost, time


def main():
    map = maps['map3']
        
    # sol = get_best_solution(map, ucs)
    sol = get_best_solution(map, a_star)

    # excute_commands(sol.commands, map)

    # print(sol.cost_amplifier)
    # print(sol.commands)
    # print(f'{sol.nodes_number} nodes processed')
    # print(f'{sol.cost} cost')
    # print(f'{sol.time:.2f} milliseconds')
    
    # nodes, cost, time = first_hur(map.truck, (3,1), map, a_star)
    # nodes, cost, time = second_hur(0, map, ucs)
    nodes, cost, time = third_hur(map, a_star)


    print(f'{nodes} nodes processed')
    print(f'{cost} cost')
    print(f'{time:.2f} milliseconds')

if __name__ == '__main__':
    main()