import pygame
from monsters import *
from config import Config
from sounds import Sounds
from player_bullet import PlayerBullet
from drawable import Drawable
from collidable import Collidable


config = Config()
sounds = Sounds()


class Player(Creature, Drawable, Collidable):

    def __init__(self, image_name):
        self.FIRST_POSITION_X = 350
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 40
        self.SIZE_HEIGHT = 80
        super().__init__(
            'Hero', image_name, self.FIRST_POSITION_X, self.FIRST_POSITION_Y,
            self.SIZE_WIDTH, self.SIZE_HEIGHT)

        self.bullets = []

    def shoot(self, event, position):
        """Handle shooting event."""
        if event.key in (pygame.K_x, pygame.K_z):
            direction = 1 if event.key == pygame.K_x else -1
            if len(self.bullets) < config.PLAYER_MAX_BULLETS:
                bullet = PlayerBullet(direction, position.x + self.SIZE_WIDTH, position.y + self.SIZE_HEIGHT // 2 - 2)
                self.bullets.append(bullet)
                sounds.BULLET_FIRE_SOUND.play()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self, win):
        for bullet in self.bullets:
            bullet.draw(win)

    def handle_bullets(self, enemy, win, hit):
        self.update_bullets()
        self.draw(win)
        for bullet in self.bullets[:]:
            if bullet.collides_with(enemy):
                pygame.event.post(pygame.event.Event(hit))
                self.bullets.remove(bullet)
            elif bullet.is_out_of_screen():
                self.bullets.remove(bullet)

    def check_collision(self, other):
        """Check if the player collides with another object."""
        if self.colliderect(other):
            return True
        return False

