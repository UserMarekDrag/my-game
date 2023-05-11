import os
import pygame
from config import Config

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
        try:
            self.background_game = pygame.transform.scale(pygame.image.load(
                os.path.join('../Assets', 'background_game.png')), (config.WIDTH, config.HEIGHT))
            self.background_stats = pygame.transform.scale(pygame.image.load(
                os.path.join('../Assets', 'background_stats.png')), (config.WIDTH, config.HEIGHT))
            self.background_menu = pygame.transform.scale(pygame.image.load(
                os.path.join('../Assets', 'background_menu.png')), (config.WIDTH, config.HEIGHT))
            self.logo = pygame.transform.scale(pygame.image.load(
                os.path.join('../Assets', 'logo.png')), (350, 200))
        except pygame.error as error:
            print('Error while loading sounds:', error)
