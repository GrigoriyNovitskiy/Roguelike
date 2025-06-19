class Cell:
    def __init__(self, type):
        self.type = type


class EmptyCell(Cell):
    def __init__(self):
        super().__init__("empty")


class HealCell(Cell):
    def __init__(self):
        super().__init__("heal")


class ObstacleCell(Cell):
    def __init__(self):
        super().__init__("obstacle")