class Field:
    def __init__(self):
        self.cells = [[None for _ in range(10)] for _ in range(10)]

    def get_cell(self, x, y):
        return self.cells[y][x]
    
    def clear(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x] = None