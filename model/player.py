from model.position import Position

class Player:
    def __init__(self):
        self.position = Position(0, 0)

    def move(self, direction, field):
        if direction == "up":
            self.position.y -= 1
        elif direction == "down":
            self.position.y += 1
        elif direction == "left":
            self.position.x -= 1
        elif direction == "right":
            self.position.x += 1