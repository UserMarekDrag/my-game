import pygame
from monsters import *
from config import *
from sounds import *


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

        if keys_pressed[pygame.K_LEFT] and player.x - VEL_PLAYER > 0:  # LEFT
            player.x -= VEL_PLAYER
        if keys_pressed[pygame.K_RIGHT] and player.x + VEL_PLAYER + player.width < WIDTH:  # RIGHT
            player.x += VEL_PLAYER
        if keys_pressed[pygame.K_UP] and player.y - VEL_PLAYER > 50:  # UP
            player.y -= VEL_PLAYER
        if keys_pressed[pygame.K_DOWN] and player.y + VEL_PLAYER + player.height < HEIGHT:  # DOWN
            player.y += VEL_PLAYER

    def draw_bullets(self, win, player_bullets):

        for bullet in player_bullets:
            pygame.draw.rect(win, YELLOW, bullet)
        self.draw_update()

    def shoot_right(self, event, player):

        if event.key == pygame.K_x and len(self.player_bullets_right) < PLAYER_MAX_BULLETS:
            bullet = pygame.Rect(
                player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
            self.player_bullets_right.append(bullet)
            BULLET_FIRE_SOUND.play()

    def shoot_left(self, event, player):

        if event.key == pygame.K_z and len(self.player_bullets_left) < PLAYER_MAX_BULLETS:
            bullet = pygame.Rect(
                player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
            self.player_bullets_left.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets_right(self, enemy, win, hit):

        for bullet in self.player_bullets_right:
            bullet.x += PLAYER_BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                self.player_bullets_right.remove(bullet)
            elif bullet.x > WIDTH:
                self.player_bullets_right.remove(bullet)
            elif bullet.x < 0:
                self.player_bullets_right.remove(bullet)
        self.draw_bullets(win, self.player_bullets_right)

    def handle_bullets_left(self, enemy, win, hit):

        for bullet in self.player_bullets_left:
            bullet.x -= PLAYER_BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                self.player_bullets_left.remove(bullet)
            elif bullet.x > WIDTH:
                self.player_bullets_left.remove(bullet)
            elif bullet.x < 0:
                self.player_bullets_left.remove(bullet)
        self.draw_bullets(win, self.player_bullets_left)
