import pygame, os
from config import *

BACKGROUND_GAME = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_game.png')), (WIDTH, HEIGHT))
BACKGROUND_STATS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_stats.png')), (WIDTH, HEIGHT))

BACKGROUND_MENU = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_menu.png')), (WIDTH, HEIGHT))

LOGO = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'logo.png')), (350, 200))
