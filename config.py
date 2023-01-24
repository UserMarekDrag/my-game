import pygame

# basic
GAME_NAME = 'Game'
WIDTH, HEIGHT = 900, 500
FPS = 60

# moving speed
VEL_PLAYER = 5
VEL_MONSTER = 2
VEL_BOSS = 3

# health amount
PLAYER_HEALTH = 5
ENEMY_HEALTH = 5
BAT_HEALTH = 1

# constant for creature
PLAYER_HIT_BOSS = pygame.USEREVENT + 1
PLAYER_HIT_BAT = pygame.USEREVENT + 4
BOSS_HIT_PLAYER = pygame.USEREVENT + 2
BAT_HIT_PLAYER = pygame.USEREVENT + 3

# push
COLLISION_VEL = 20

# shot speed
BULLET_VEL = 5
MAX_BULLETS = 3

# font
pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (112, 112, 112)

# button constant
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 70

FONT_SIZE = 32

INITIAL_FONT = pygame.font.SysFont('comicsans', 32)

BUTTON_FONT_GROUND_COLOR = BLACK
BUTTON_GROUND_COLOR = GREY

BUTTON_POSITION_WIDTH_ON_SCREEN = WIDTH / 2 - BUTTON_WIDTH / 2
BUTTON_POSITION_HEIGHT_ON_SCREEN = 100
