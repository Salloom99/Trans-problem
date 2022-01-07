from copy import deepcopy
from timeit import default_timer as timer

# The Solution Class comes to process all things related to the soultion
# as a combination of storages and validat it then computes its values
# so you can access them like attributes
class Solution:
    def __init__(self, comb, map, search_algorithm) -> None:
        self.comb = comb
        self.cost_amplifier = [1 for _ in comb]
        self.is_valid = True
        self.commands = []
        self.actions = []
        self.cost = 0
        self.nodes_number = 0

        self.check_validality()
        
        if self.is_valid:
            # self.cost_amplifier.append(1)
            self.cost_amplifier.insert(0,1)

            # start elapsed time
            start_time = timer() * 1000

            self.setup(map, search_algorithm)

            # stop elapsed time
            end_time = timer() * 1000
            self.time = end_time - start_time


    def setup(self, map, search_algorithm):
        transitions = self.get_transitions(map.start_point)
        for transition in transitions:
            point_a = transition[0]
            point_b = transition[1]
            path, count = search_algorithm(point_a,point_b, map.cells)
            action = self.actions.pop(0) if len(self.actions) > 0 else 'None'
            road_cost = len(path)
            path.append(action)
            self.nodes_number += count
            self.commands += path
            self.cost += self.cost_amplifier.pop(0)*road_cost

    # it works like push down automata
    def check_validality(self):
        check_list = []
        for i, storage in enumerate(self.comb):
            try:
                if storage.is_producer:
                    check_list.append(storage.id)
                    self.cost_amplifier = [cost if j < i else cost+1 for j, cost in enumerate(self.cost_amplifier)]
                    self.actions.append(['load',storage.id])
                else:
                    self.pop_prod(check_list, storage.id)
                    self.cost_amplifier = [cost if j < i else cost-1 for j, cost in enumerate(self.cost_amplifier)]
                    self.actions.append(['unload',storage.id])
            except:
                self.is_valid = False

    # extract points from storages
    def get_transitions(self, start_point):
        transitions = []
        point1 = None
        point2 = start_point
        for i in range(len(self.comb)+1):
            point = (self.comb[i].row, self.comb[i].col) if i < len(self.comb) else start_point
            point1 = point2
            point2 = point
            transitions.append([point1, point2])
        return transitions
            
    # pop a certain producer
    def pop_prod(self,list: list, id):
        if id in list:
            list.remove(id)
        else:
            raise
