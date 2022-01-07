from .directions import DIRECTIONS

# The Truck Class which handle the operations on the truck
# from moving to loading and unloading and simplify printing it
# on the screen
class Truck:
    def __init__(self, start_point) -> None:
        self.row = start_point[0]
        self.col = start_point[1]
        self.loads = []

    def move(self, direction):
        vector = DIRECTIONS[direction]
        self.col += vector[0]
        self.row += vector[1]

    def load(self, id):
        self.loads.append(id)
        print('loaded successfully')

    def unload(self, id):
        if id not in self.loads:
            print(f'does not have load {id}..!')
            return
        self.loads.remove(id)
        print('unloaded successfully')
    
    def __str__(self) -> str:
        return 'T' if self.loads == None else f'T{self.loads}'

    def __repr__(self) -> str:
        return f'truck at ({self.row},{self.col})'
