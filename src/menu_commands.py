import sys
from abc import ABC, abstractmethod

import pygame
from src.backgrounds import Backgrounds

backgrounds = Backgrounds()


class MenuCommand(ABC):
    """
    Abstract base class for menu commands.
    """
    def __init__(self, menu):
        self.menu = menu

    @abstractmethod
    def execute(self):
        """
        Execute the menu command.
        """
        pass


class StartGameCommand(MenuCommand):
    """
    Command to start the game.
    """
    def execute(self):
        return False


class RestartGameCommand(MenuCommand):
    """
    Command to restart the game.
    """
    def execute(self):
        self.menu.game.new_game()


class OptionsCommand(MenuCommand):
    """
    Command to open the character selection menu.
    """
    def execute(self):
        self.menu.game.window.blit(backgrounds.background_menu, (0, 0))
        pygame.display.update()
        pygame.time.wait(100)
        return self.menu.menu_choice_char()


class QuitGameCommand(MenuCommand):
    """
    Command to quit the game.
    """
    def execute(self):
        self.menu.game.run = False
        pygame.quit()
        sys.exit()


class ChooseMaleCharacterCommand(MenuCommand):
    """
    Command to choose the male character.
    """
    def execute(self):
        self.menu.character_choice = "male"
        self.menu.character_update()
        return False


class ChooseFemaleCharacterCommand(MenuCommand):
    """
    Command to choose the female character.
    """
    def execute(self):
        self.menu.character_choice = "female"
        self.menu.character_update()
        return False
