import pygame
from creature import Creature
from config import Config
from sounds import Sounds
from bullet import Bullet
from interfaces import Collidable, Drawable, Updatable

config = Config()
sounds = Sounds()


class Player(Creature, Drawable, Collidable, Updatable):
    """A class representing the player character in the game.

    Attributes:
        first_position_x (int): the initial x position of the player.
        first_position_y (int): the initial y position of the player.
        size_width (int): the width of the player sprite.
        size_height (int): the height of the player sprite.
        health (int): the initial health of the player.
    """

    def __init__(self, image_name):
        self.first_position_x = 350
        self.first_position_y = 150
        self.size_width = 40
        self.size_height = 80
        self.health = config.PLAYER_HEALTH
        super().__init__(
            'Hero', image_name, self.first_position_x, self.first_position_y,
            self.size_width, self.size_height, self.health)
        self.bullets = []

    def reset(self, position_x=350, position_y=150):
        """Reset the player to its initial state at the given position."""
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_alive = True
        self.health = config.PLAYER_HEALTH
        self.bullets = []

    def shoot(self, event):
        """Handle shooting event when the x or z key is pressed."""
        if event.key in (pygame.K_x, pygame.K_z):
            direction = 1 if event.key == pygame.K_x else -1
            if len(self.bullets) < config.PLAYER_MAX_BULLETS:
                bullet = Bullet(
                    direction, self.rect.x + self.size_width,
                               self.rect.y + self.size_height // 2 - 2,
                    config.PLAYER_BULLET_VEL, config.YELLOW
                )
                self.bullets.append(bullet)
                sounds.bullet_fire_sound.play()

    def update(self):
        """Update the player's bullets."""
        for bullet in self.bullets:
            bullet.update()

    def draw(self, win):
        """Draw the player's bullets."""
        for bullet in self.bullets:
            bullet.draw(win)

    def handle_bullets(self, enemy, win):
        """Handle collision between the player's bullets and the enemy."""
        self.update()
        self.draw(win)
        for bullet in self.bullets[:]:
            if bullet.collides_with(enemy.rect) and enemy.is_alive:
                enemy.take_damage()
                self.bullets.remove(bullet)
            elif bullet.is_out_of_screen():
                self.bullets.remove(bullet)

    def check_collision(self, other, type_other):
        """Check for collision between the player and the enemy."""
        if isinstance(other, type_other) and self.rect.colliderect(other.rect) and other.is_alive:
            self.collision(other)
            self.take_damage()
            other.take_damage()

    def move(self, keys=None, target=None):
        """Move the player character based on keyboard input."""
        if keys[pygame.K_LEFT] and self.rect.x - config.VEL_PLAYER > 0:  # LEFT
            self.rect.x -= config.VEL_PLAYER
        if keys[pygame.K_RIGHT] and self.rect.x + config.VEL_PLAYER + self.rect.width < config.WIDTH:  # RIGHT
            self.rect.x += config.VEL_PLAYER
        if keys[pygame.K_UP] and self.rect.y - config.VEL_PLAYER > 50:  # UP
            self.rect.y -= config.VEL_PLAYER
        if keys[pygame.K_DOWN] and self.rect.y + config.VEL_PLAYER + self.rect.height < config.HEIGHT:  # DOWN
            self.rect.y += config.VEL_PLAYER

    def collision(self, enemy):
        """
        Handles collision between the player and another game object. If a collision occurs,
        the player's position is adjusted to avoid overlapping with the enemy object.

        Args:
        enemy: The enemy game object to check for collision with the player.
        """
        if enemy.rect.x > self.rect.x > 10:
            self.rect.x -= config.COLLISION_VEL
            pygame.time.wait(100)
        elif enemy.rect.x < self.rect.x < (config.WIDTH - 40):
            self.rect.x += config.COLLISION_VEL
            pygame.time.wait(100)
        elif enemy.rect.y > self.rect.y > 20:
            self.rect.y -= config.COLLISION_VEL
            pygame.time.wait(100)
        elif enemy.rect.y < self.rect.y < config.HEIGHT - 80:
            self.rect.y += config.COLLISION_VEL
            pygame.time.wait(100)
