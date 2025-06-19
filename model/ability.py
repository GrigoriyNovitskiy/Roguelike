class Ability:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, target):
        self.effect(target)