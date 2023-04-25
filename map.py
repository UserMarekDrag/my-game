import pygame, os
from config import Config


config = Config()

BACKGROUND_GAME = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_game.png')), (config.WIDTH, config.HEIGHT))
BACKGROUND_STATS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_stats.png')), (config.WIDTH, config.HEIGHT))

BACKGROUND_MENU = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_menu.png')), (config.WIDTH, config.HEIGHT))

LOGO = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'logo.png')), (350, 200))
