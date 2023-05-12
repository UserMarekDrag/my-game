from src.config import Config


config = Config()


class DisplayText:
    """
    A class for displaying text on a Pygame window.
    """

    def __init__(self, window):
        self.window = window
        self.text = None

    def txt_draw(self, number, width, height, name, content, font):
        """
        Render and display text on the window at the specified width and height.
        The text is composed of a name, content, and number, and is rendered using the provided font.
        """
        self.text = font.render(
            f"{str(name)} {str(content)}: " + str(number), True, config.BLUE)

        self.display_text(width, height)

    def display_text(self, width, height):
        """
        Draw the rendered text on the window at the given (width, height) position.
        """
        self.window.blit(self.text, (width, height))
