import pygame
from config import Config
from sounds import Sounds
from drawable import Drawable
from collidable import Collidable
from updatable import Updatable

config = Config()
sounds = Sounds()


class PlayerBullet(Drawable, Collidable, Updatable):

    def __init__(self, direction, x, y):
        self.direction = direction
        self.bullet = pygame.Rect(x, y, 10, 5)

    def draw(self, win):
        pygame.draw.rect(win, config.YELLOW, self.bullet)

    def is_out_of_screen(self):
        return self.bullet.x > config.WIDTH or self.bullet.x < 0

    def collides_with(self, enemy):
        return self.bullet.colliderect(enemy)

    def check_collision(self, other):
        if self.colliderect(other):
            return True
        return False

    def update(self):
        if self.direction == 1:
            self.bullet.x += config.PLAYER_BULLET_VEL
        else:
            self.bullet.x -= config.PLAYER_BULLET_VEL
