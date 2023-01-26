import pygame

# basic
GAME_NAME = 'Game'
WIDTH, HEIGHT = 900, 500
FPS = 60

# character image
MALE_CHARACTER = "male_player.PNG"
FEMALE_CHARACTER = "female_player.PNG"

# enemy image
BOSS_IMAGE = 'boss.png'
MONSTRER_IMAGE = 'bat.png'

# moving speed
VEL_PLAYER = 5
VEL_MONSTER = 3
VEL_BOSS = 4

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
BULLET_VEL = 7
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
ORANGE = (227, 158, 79)

# button constant
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 60

FONT_SIZE = 32

INITIAL_FONT = pygame.font.SysFont('comicsans', 32)

BUTTON_FONT_GROUND_COLOR = BLACK
BUTTON_GROUND_COLOR = ORANGE

BUTTON_POSITION_WIDTH_ON_SCREEN = WIDTH / 2 - BUTTON_WIDTH / 2
BUTTON_POSITION_HEIGHT_ON_SCREEN = 100
