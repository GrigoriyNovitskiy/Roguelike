class Monster:
    def __init__(self, position, strategy):
        self.position = position
        self.strategy = strategy

    def move(self, field):
        self.strategy.move(self, field)