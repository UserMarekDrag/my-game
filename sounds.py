import os
import pygame

pygame.mixer.init()

BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join('Assets', 'Gun+Silencer.mp3'))
