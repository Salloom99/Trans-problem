from map_stuff.directions import DIRECTIONS
from .truck import Truck
from .storage import Storage

# The Map Class where you can access any piece of information about the map
# it reads a text file and convert it to map object and control the commands
# of the truck, the producers and the destinations
class Map:
    def __init__(self,txt_file) -> None:
        self.cells = []
        self.start_point = None
        self.producers = []
        self.destinations = []

        self.read_from_text(txt_file)
        self.truck = Truck(self.start_point)
    
    def read_from_text(self, txt_file):
        state_file = open(txt_file)
        for line in state_file:
            self.cells.append(line[:-1].split(' '))
        for row,actual_row in enumerate(self.cells):
            for col in range(len(actual_row)):
                if self.cells[row][col] == 'T':
                    self.start_point = (row, col)
                elif self.cells[row][col][0] == 'P':
                    id = int(self.cells[row][col][1])
                    producer = Storage(id, row, col, True)
                    self.producers.append(producer)
                elif self.cells[row][col][0] == 'D':
                    id = int(self.cells[row][col][1])
                    destination = Storage(id, row, col, False)
                    self.destinations.append(destination)
                if self.cells[row][col] != '#':
                    self.cells[row][col] = '.'

    def get_producer(self, id):
        for producer in self.producers:
            if producer.id == id:
                return producer

    def get_destination(self, id):
        for destination in self.destinations:
            if destination.id == id:
                return destination

    def has_storage(self, row, col):
        for producer in self.producers:
            if producer.row == row and producer.col == col:
                return producer
        
        for destination in self.destinations:
            if destination.row == row and destination.col == col:
                return destination
    
    def let_truck_do(self, command):
        if command[0] == 'load':
            id = int(command[1])
            prod = self.get_producer(id)
            self.truck.load(id)
            prod.load()
        elif command[0] == 'unload':
            id = int(command[1])
            dest = self.get_destination(id)
            self.truck.unload(id)
            dest.unload()
        elif command in DIRECTIONS:
            self.truck.move(command)
        else:
            print("We're back home")

    def real_time(self):
        string = str(self).split('\n')
        string[3] += '\tT[0] means that the trunck has the package from the P0'
        string[6] += '\tCapital letters means the storage has its package'
        string[9] += '\tSmall letters means its package not here'
        return '\n'.join(string)

    def __str__(self) -> str:
        string = ''
        for i,row in enumerate(self.cells):
            string += "\n"*3 + '\t'
            for j,cell in enumerate(row):
                storage = self.has_storage(i, j)
                if self.truck.row == i and self.truck.col == j:
                    cell = self.truck
                elif storage:
                    cell = storage
                string += f'{cell}\t'
        return string+'\n'

    def __repr__(self) -> str:
        string = str(self) + '\n'
        string += repr(self.truck) + '\n'
        string += 'producers are :\n'
        for producer in self.producers:
            string += repr(producer) + '\n'
        string += 'destinations are :\n'
        for destination in self.destinations:
            string += repr(destination) + '\n'
        return string