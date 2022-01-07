# The Storage Class which is the parent of the producer and
# the destinaion so you can treat them as one type
class Storage:
    def __init__(self, id, row, col, is_producer) -> None:
        self.id = id
        self.row = row
        self.col = col
        self.is_producer = is_producer
        self.loaded = is_producer

    def load(self):
        self.loaded = False
    
    def unload(self):
        self.loaded = True

    def __str__(self) -> str:
        string = 'P' if self.is_producer else 'D'
        string = string.lower() if not self.loaded else string
        return string + str(self.id)

    def __repr__(self) -> str:
        return f'storage {"full" if self.loaded else "empty"} at ({self.row},{self.col})'