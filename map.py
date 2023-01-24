import pygame, os
from config import *

BACKGROUND_GAME = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))

BACKGROUND_MENU = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background_menu.png')), (WIDTH, HEIGHT))
