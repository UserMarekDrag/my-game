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
        FIRST_POSITION_X (int): the initial x position of the player.
        FIRST_POSITION_Y (int): the initial y position of the player.
        SIZE_WIDTH (int): the width of the player sprite.
        SIZE_HEIGHT (int): the height of the player sprite.
        HEALTH (int): the initial health of the player.
    """
    def __init__(self, image_name):
        self.FIRST_POSITION_X = 350
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 40
        self.SIZE_HEIGHT = 80
        self.HEALTH = config.PLAYER_HEALTH
        super().__init__(
            'Hero', image_name, self.FIRST_POSITION_X, self.FIRST_POSITION_Y,
            self.SIZE_WIDTH, self.SIZE_HEIGHT, self.HEALTH)
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
                    direction, self.rect.x + self.SIZE_WIDTH,
                    self.rect.y + self.SIZE_HEIGHT // 2 - 2,
                    config.PLAYER_BULLET_VEL, config.YELLOW
                )
                self.bullets.append(bullet)
                sounds.BULLET_FIRE_SOUND.play()

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

    def check_collision(self, other, enemy):
        """Check for collision between the player and the enemy."""
        if isinstance(other, enemy) and self.rect.colliderect(other.rect) and other.is_alive:
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

    def collision(self, other):
        """
        Handles collision between the player and another game object. If a collision occurs,
        the player's position is adjusted to avoid overlapping with the other object.

        Args:
        other: The other game object to check for collision with the player.
        """
        if other.rect.x > self.rect.x > 10:
            self.rect.x -= config.COLLISION_VEL
            pygame.time.wait(100)
        elif other.rect.x < self.rect.x < (config.WIDTH - 40):
            self.rect.x += config.COLLISION_VEL
            pygame.time.wait(100)
        elif other.rect.y > self.rect.y > 20:
            self.rect.y -= config.COLLISION_VEL
            pygame.time.wait(100)
        elif other.rect.y < self.rect.y < config.HEIGHT - 80:
            self.rect.y += config.COLLISION_VEL
            pygame.time.wait(100)
