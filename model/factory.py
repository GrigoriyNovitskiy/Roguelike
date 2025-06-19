from model.monster import Monster
from model.player import Player
from model.strategy import AggressiveStrategy

class MonsterFactory:
    def create_monster(self, position, strategy):
        return Monster(position, strategy)


class HumanFactory:
    def create_human(self, position):
        return Player(position)


class BossFactory:
    def create_boss(self, position):
        return Monster(position, AggressiveStrategy())