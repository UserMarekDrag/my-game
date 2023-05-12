import pygame
from src.config import Config

config = Config()


class ButtonBuilder:
    """
    ButtonBuilder class for creating Button instances with customizable properties.
    """
    def __init__(self):
        self._button = Button()

    def reset(self):
        """
        Reset the builder state to create a new button.
        """
        self._button = Button()

    def set_position(self, position_x, position_y):
        """
        Set the position of the button and its rectangle.
        """
        self._button.position_x, self._button.position_y = position_x, position_y
        self._button.rect.x, self._button.rect.y = position_x, position_y
        return self

    def set_content(self, content):
        """
        Set the content (text) of the button and render it on the button surface.
        """
        self._button.content = content
        self._button.text = self._button.font.render(content, True, self._button.font_ground_color)
        self._button.text_rect = self._button.text.get_rect(center=(self._button.width / 2, self._button.height / 2))
        self._button.image.blit(self._button.text, self._button.text_rect)
        return self

    def set_action(self, action):
        """
        Set the action (Command) associated with the button.
        """
        self._button.action = action
        return self

    def build(self):
        """
        Build the Button instance and reset the builder for future use.
        """
        button = self._button
        self.reset()
        return button


class Button:
    """
    Button class representing a button with text, position, size, and associated action.
    """
    def __init__(self):
        self.font_size = config.FONT_SIZE
        self.font = pygame.font.SysFont('comicsans', self.font_size)

        self.position_x, self.position_y = 0, 0
        self.width = config.BUTTON_WIDTH
        self.height = config.BUTTON_HEIGHT

        self.font_ground_color = config.BUTTON_FONT_GROUND_COLOR
        self.background_color = config.BUTTON_GROUND_COLOR
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.background_color)
        self.rect = self.image.get_rect()

    def is_pressed(self, position, pressed):
        """
        Check if the button is pressed based on the mouse position and button state.
        """
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            return False
        return False

    def draw_on_screen(self, window):
        """
        Draw the button on the given surface (win).
        """
        window.blit(self.image, self.rect)
