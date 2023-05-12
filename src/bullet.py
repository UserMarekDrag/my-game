import pygame
from src.config import Config
from src.sounds import Sounds
from src.interfaces import Collidable, Drawable, Updatable

config = Config()
sounds = Sounds()


class Bullet(Drawable, Collidable, Updatable):

    def __init__(self, direction, x, y, bullet_vel, color):
        """
        Initialize a bullet with a given direction, x and y coordinates, bullet velocity, and color.

        Args:
            direction (int): The direction the bullet is moving.
            x (int): The x coordinate of the bullet's starting position.
            y (int): The y coordinate of the bullet's starting position.
            bullet_vel (int): The speed at which the bullet travels.
            color (tuple): The color of the bullet.
        """
        self.direction = direction
        self.bullet_vel = bullet_vel
        self.color = color
        self.bullet = pygame.Rect(x, y, 10, 5)

    def draw(self, win):
        """
        Draw the bullet on the given window.

        Args:
            win (pygame.Surface): The game window on which to draw the bullet.
        """
        pygame.draw.rect(win, self.color, self.bullet)

    def is_out_of_screen(self):
        """
        Check if the bullet has moved out of the game window.

        Returns:
            bool: True if the bullet is out of the screen, False otherwise.
        """
        return self.bullet.x > config.WIDTH or self.bullet.x < 0

    def collides_with(self, enemy):
        """
        Check if the bullet has collided with the given enemy.

        Args:
            enemy (Enemy): The enemy with which to check for collision.

        Returns:
            bool: True if the bullet has collided with the enemy, False otherwise.
        """
        return self.bullet.colliderect(enemy)

    def check_collision(self, other, type_other):
        """
        Check if the bullet has collided with the given collidable object of the specified type.

        Args:
            other (Collidable): The collidable object with which to check for collision.
            type_other (str): The type of the collidable object.

        Returns:
            bool: True if the bullet has collided with the collidable object, False otherwise.
        """
        if self.colliderect(other, type_other) and other.is_alive:
            return True
        return False

    def update(self):
        """
        Update the bullet's position according to its velocity and direction.
        """
        if self.direction == 1:
            self.bullet.x += self.bullet_vel
        else:
            self.bullet.x -= self.bullet_vel
