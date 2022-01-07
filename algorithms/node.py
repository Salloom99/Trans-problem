# The Node Class is for making A* calculations much easier 
# by splitting the values of g (Cost) and h (heuristic)
# then summing the values into f
class Node:
    def __init__(self, point, g=0, h=0) -> None:
        self.point = point
        self.g = g
        self.h = h
        self.f = self.g + self.h