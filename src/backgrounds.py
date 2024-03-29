from pathlib import Path

import pygame
from src.config import Config

config = Config()


class Backgrounds:
    """
    A singleton class to manage the backgrounds used in the game.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of Backgrounds class if it does not exist, otherwise return the existing one.

        Returns:
        --------
        cls._instance : Backgrounds
            The instance of the Backgrounds class
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Check if the instance has been initialized
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.init_backgrounds()

    def init_backgrounds(self):
        base_dir = Path(__file__).resolve().parent.parent.parent
        try:
            background_game_file = base_dir / 'game' / 'Assets' / 'background_game.png'
            self.background_game = pygame.transform.scale(pygame.image.load(
                str(background_game_file)), (config.WIDTH, config.HEIGHT))

            background_stats_file = base_dir / 'game' / 'Assets' / 'background_stats.png'
            self.background_stats = pygame.transform.scale(pygame.image.load(
                str(background_stats_file)), (config.WIDTH, config.HEIGHT))

            background_menu_file = base_dir / 'game' / 'Assets' / 'background_menu.png'
            self.background_menu = pygame.transform.scale(pygame.image.load(
                str(background_menu_file)), (config.WIDTH, config.HEIGHT))

            logo_file = base_dir / 'game' / 'Assets' / 'logo.png'
            self.logo = pygame.transform.scale(pygame.image.load(
                str(logo_file)), (350, 200))
        except pygame.error as error:
            print('Error while loading sounds:', error)
