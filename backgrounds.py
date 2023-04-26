import pygame
import os
from config import Config


config = Config()


class Backgrounds:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_backgrounds()
        return cls._instance

    def init_backgrounds(self):
        self.BACKGROUND_GAME = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'background_game.png')), (config.WIDTH, config.HEIGHT))
        self.BACKGROUND_STATS = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'background_stats.png')), (config.WIDTH, config.HEIGHT))
        self.BACKGROUND_MENU = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'background_menu.png')), (config.WIDTH, config.HEIGHT))
        self.LOGO = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'logo.png')), (350, 200))
