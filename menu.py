import pygame
from config import *


class Button:
    def __init__(self, x, y, content):
        self.font_size = FONT_SIZE
        self.font = pygame.font.SysFont('comicsans', self.font_size)
        self.content = content

        self.x, self.y = x, y
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT

        self.fg = BUTTON_FONT_GROUND_COLOR
        self.bg = BUTTON_GROUND_COLOR
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.x, self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, position, pressed):
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            return False
        return False
