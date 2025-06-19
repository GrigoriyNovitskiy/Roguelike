import pygame


class MainMenuDrawer:
    BG_COLOR = (0, 0, 0)
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE = 74
    TEXT_POSITION = (250, 100)

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, self.FONT_SIZE)

    def draw(self):
        self.screen.fill(self.BG_COLOR)
        self._draw_text("Main Menu", self.TEXT_POSITION)
        pygame.display.flip()

    def _draw_text(self, text, position):
        rendered_text = self.font.render(text, True, self.TEXT_COLOR)
        self.screen.blit(rendered_text, position)
