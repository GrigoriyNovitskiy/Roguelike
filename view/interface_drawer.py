import pygame


class InterfaceDrawer:
    CELL_SIZE = 32
    COLOR_BG = (0, 0, 0)
    COLOR_CELL = (255, 255, 255)
    COLOR_PLAYER = (0, 255, 0)

    def __init__(self, screen):
        self.screen = screen

    def draw(self, game_state):
        self.screen.fill(self.COLOR_BG)

        field = game_state.get("field")
        if field:
            for y, row in enumerate(field.cells):
                for x, cell in enumerate(row):
                    color = self.COLOR_CELL if cell else self.COLOR_BG
                    self._draw_cell(x, y, color)

        player = game_state.get("player")
        if player:
            self._draw_cell(player.position.x, player.position.y, self.COLOR_PLAYER)

        pygame.display.flip()

    def _draw_cell(self, x, y, color):
        rect = pygame.Rect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)
