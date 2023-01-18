import pygame


GAME_NAME = 'Game'
WIDTH, HEIGHT = 900, 500
FPS = 60

VEL_PLAYER = 5
VEL_MONSTER = 2
VEL_BOSS = 3

PLAYER_HEALTH = 5
ENEMY_HEALTH = 5

PLAYER_HIT = pygame.USEREVENT + 1
BOSS_HIT = pygame.USEREVENT + 2

BULLET_VEL = 5
MAX_BULLETS = 3


pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
