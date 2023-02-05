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
MONSTER_IMAGE = 'bat.png'
MAGE_IMAGE = 'mage.png'

# moving speed
VEL_PLAYER = 5
VEL_MONSTER = 4
VEL_BOSS = 5

# health amount
PLAYER_HEALTH = 3
BOSS_HEALTH = 10
BAT_HEALTH = 1
MAGE_HEALTH = 2

# constant for creature
PLAYER_HIT_BOSS = pygame.USEREVENT + 1
PLAYER_HIT_BAT = pygame.USEREVENT + 4
PLAYER_HIT_BAT_1 = pygame.USEREVENT + 7
PLAYER_HIT_BAT_2 = pygame.USEREVENT + 8
PLAYER_HIT_MAGE_1 = pygame.USEREVENT + 10
PLAYER_HIT_MAGE_2 = pygame.USEREVENT + 12

BOSS_HIT_PLAYER = pygame.USEREVENT + 2

BAT_HIT_PLAYER = pygame.USEREVENT + 3
BAT_1_HIT_PLAYER = pygame.USEREVENT + 5
BAT_2_HIT_PLAYER = pygame.USEREVENT + 6

MAGE_1_HIT_PLAYER = pygame.USEREVENT + 9
MAGE_2_HIT_PLAYER = pygame.USEREVENT + 11

# push
COLLISION_VEL = 20

# shot speed
BOSS_BULLET_VEL = 10
PLAYER_BULLET_VEL = 7

# number of shots
PLAYER_MAX_BULLETS = 3
BOSS_MAX_BULLETS = 5
MAGE_MAX_BULLETS = 3

# font
pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
STAGE_NUMB_FONT = pygame.font.SysFont('comicsans', 100)

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (112, 112, 112)
ORANGE = (227, 158, 79)
BLUE = (240, 248, 255)

# button constant
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 60
FONT_SIZE = 32
INITIAL_FONT = pygame.font.SysFont('comicsans', 32)
BUTTON_FONT_GROUND_COLOR = BLACK
BUTTON_GROUND_COLOR = ORANGE
BUTTON_POSITION_WIDTH_ON_SCREEN = WIDTH / 2 - BUTTON_WIDTH / 2
BUTTON_POSITION_HEIGHT_ON_SCREEN = 100
