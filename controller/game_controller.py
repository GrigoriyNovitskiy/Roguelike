import pygame
from model.game import Game


class GameController:
    def __init__(self):
        self.game = Game()
        self.direction_map = {
            pygame.K_w: "up",
            pygame.K_s: "down",
            pygame.K_a: "left",
            pygame.K_d: "right"
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            direction = self.direction_map.get(event.key)
            if direction:
                self.game.move_player(direction)

    def update(self):
        self.game.update()

    def get_game_state(self):
        return self.game.get_state()
