import pygame
from config import Config

config = Config()


class EventHandler:

    @staticmethod
    def handle_movement(keys_pressed, player):
        if keys_pressed[pygame.K_LEFT] and player.x - config.VEL_PLAYER > 0:  # LEFT
            player.x -= config.VEL_PLAYER
        if keys_pressed[pygame.K_RIGHT] and player.x + config.VEL_PLAYER + player.width < config.WIDTH:  # RIGHT
            player.x += config.VEL_PLAYER
        if keys_pressed[pygame.K_UP] and player.y - config.VEL_PLAYER > 50:  # UP
            player.y -= config.VEL_PLAYER
        if keys_pressed[pygame.K_DOWN] and player.y + config.VEL_PLAYER + player.height < config.HEIGHT:  # DOWN
            player.y += config.VEL_PLAYER
