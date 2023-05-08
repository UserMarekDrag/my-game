import pygame
from config import Config


config = Config()


class ButtonBuilder:
    def __init__(self):
        self._button = Button()

    def reset(self):
        self._button = Button()

    def set_position(self, x, y):
        self._button.x, self._button.y = x, y
        self._button.rect.x, self._button.rect.y = x, y
        return self

    def set_content(self, content):
        self._button.content = content
        self._button.text = self._button.font.render(content, True, self._button.fg)
        self._button.text_rect = self._button.text.get_rect(center=(self._button.width / 2, self._button.height / 2))
        self._button.image.blit(self._button.text, self._button.text_rect)
        return self

    def build(self):
        button = self._button
        self.reset()
        return button


class Button:
    def __init__(self):
        self.font_size = config.FONT_SIZE
        self.font = pygame.font.SysFont('comicsans', self.font_size)

        self.x, self.y = 0, 0
        self.width = config.BUTTON_WIDTH
        self.height = config.BUTTON_HEIGHT

        self.fg = config.BUTTON_FONT_GROUND_COLOR
        self.bg = config.BUTTON_GROUND_COLOR
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

    def is_pressed(self, position, pressed):
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            return False
        return False

    def draw_on_screen(self, win):
        win.blit(self.image, self.rect)
