from model.field import Field
from model.player import Player

class Game:
    def __init__(self):
        self.field = Field()
        self.player = Player()

    def move_player(self, direction):
        self.player.move(direction, self.field)

    def update(self):
        pass

    def get_state(self):
        return {
            "player": self.player,
            "field": self.field
        }