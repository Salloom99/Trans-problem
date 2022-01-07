from map_stuff.directions import DIRECTIONS
from map_stuff.truck import Truck

# The Terrain Class isolate the things related to the availability of
# navigating within the map from the Map Class so you can use it
# in the search space without adding those functions to the Map Class 
class Terrain:
    def __init__(self, cells) -> None:
        self.cells = cells
        self.buildings = []

        for row, actual_row in enumerate(cells):
            for col, cell in enumerate(actual_row):
                if cell == '#': self.buildings.append((row, col))

    def is_building(self, point) -> bool:
        if point in self.buildings:
            return True
        return False
    
    def out_of_city(self, point) -> bool:
        row = point[0]
        col = point[1]
        if row >= len(self.cells) or row >= len(self.cells) or row < 0 or col < 0:
            return True
        return False

    def get_all_available_moves(self, point):
        moves = []
        for direction in DIRECTIONS.keys():
            truck = Truck(point)
            truck.move(direction)
            tmp_point = (truck.row, truck.col)
            if  not (self.is_building(tmp_point) or self.out_of_city(tmp_point)):
                moves.append([tmp_point, direction])

        return moves

    def get_manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])