import pygame
from monsters import *
from config import Config
from sounds import Sounds


config = Config()
sounds = Sounds()


class Player(Creature):

    def __init__(self, image_name):
        self.FIRST_POSITION_X = 350
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 40
        self.SIZE_HEIGHT = 80
        super().__init__(
            'Hero', image_name, self.FIRST_POSITION_X, self.FIRST_POSITION_Y,
            self.SIZE_WIDTH, self.SIZE_HEIGHT)

        self.player_bullets_right = []
        self.player_bullets_left = []

    def static_handle_movement(self, keys_pressed, player):

        if keys_pressed[pygame.K_LEFT] and player.x - config.VEL_PLAYER > 0:  # LEFT
            player.x -= config.VEL_PLAYER
        if keys_pressed[pygame.K_RIGHT] and player.x + config.VEL_PLAYER + player.width < config.WIDTH:  # RIGHT
            player.x += config.VEL_PLAYER
        if keys_pressed[pygame.K_UP] and player.y - config.VEL_PLAYER > 50:  # UP
            player.y -= config.VEL_PLAYER
        if keys_pressed[pygame.K_DOWN] and player.y + config.VEL_PLAYER + player.height < config.HEIGHT:  # DOWN
            player.y += config.VEL_PLAYER

    def draw_bullets(self, win, direction):
        player_bullets = self.player_bullets_right if direction == 1 else self.player_bullets_left
        for bullet in player_bullets:
            pygame.draw.rect(win, config.YELLOW, bullet)
        self.draw_update()

    def shoot(self, event, player, direction):
        if direction == 1:
            bullet_key = pygame.K_x
            player_bullets = self.player_bullets_right
        else:
            bullet_key = pygame.K_z
            player_bullets = self.player_bullets_left

        if event.key == bullet_key and len(player_bullets) < config.PLAYER_MAX_BULLETS:
            bullet = pygame.Rect(
                player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
            player_bullets.append(bullet)
            sounds.BULLET_FIRE_SOUND.play()

    def handle_bullets(self, enemy, win, hit, direction):
        player_bullets = self.player_bullets_right if direction == 1 else self.player_bullets_left
        bullet_vel = config.PLAYER_BULLET_VEL * direction
        for bullet in player_bullets:
            bullet.x += bullet_vel
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                player_bullets.remove(bullet)
            elif bullet.x > config.WIDTH or bullet.x < 0:
                player_bullets.remove(bullet)
        self.draw_bullets(win, direction)

    def handle_bullets_right(self, enemy, win, hit):
        self.handle_bullets(enemy, win, hit, 1)

    def handle_bullets_left(self, enemy, win, hit):
        self.handle_bullets(enemy, win, hit, -1)

