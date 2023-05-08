import pygame
from config import Config
from sounds import Sounds
from creature import Creature
from bullet import Bullet
from interfaces import Drawable, Collidable, Updatable


config = Config()
sounds = Sounds()


class Monster(Creature, Drawable, Collidable, Updatable):
    """
    A class representing a monster.

    Attributes:
        monster_bullets (list): A list of bullet instances shot by the monster.
    """
    def __init__(self, image_name, x, y, width, height, health):
        super().__init__('Monster', image_name, x, y, width, height, health)
        self.monster_bullets = []

    def reset(self, position_x, position_y):
        """
        Resets the monster instance to its initial position and state.

        Args:
            position_x (int): The initial x-coordinate of the monster.
            position_y (int): The initial y-coordinate of the monster.
        """
        pass

    def update(self):
        """
        Updates the state of bullets the monster.
        """
        for bullet in self.monster_bullets:
            bullet.update()

    def draw(self, win):
        """
        Draws the monster bullets instance on the screen.

        Args:
            win (pygame.Surface): The surface to draw the monster on.
        """
        for bullet in self.monster_bullets:
            bullet.draw(win)

    def move(self, keys=None, target=None):
        """
        Moves the monster on the screen.

        Args:
            keys (pygame.key): The keys pressed by the player.
            target (pygame.Rect): The target to move towards.
        """
        pass

    def check_collision(self, other, player):
        """
        Checks if the monster collided with another object.

        Args:
            other: The object to check collision with.
            player: The player instance.

        Returns:
            None
        """
        if isinstance(other, player) and self.rect.colliderect(other.rect):
            other.take_damage()

    def shoot(self, player):
        """
        Shoots a bullet from the monster.

        Args:
            player: The player instance.
        """
        direction = self.check_direction(player)

        if len(self.monster_bullets) < config.BOSS_MAX_BULLETS:
            bullet = Bullet(
                direction, self.rect.x + self.width // 2, self.rect.y + self.height // 2, config.BOSS_BULLET_VEL, config.RED)
            self.monster_bullets.append(bullet)
            sounds.BULLET_FIRE_SOUND.play()

    def check_direction(self, player):
        """
        Checks the direction of the player from the monster.

        Args:
            player: The player instance.

        Returns:
            int: -1 if the player is on the left, 1 if the player is on the right.
        """
        if self.rect.x > player.rect.x:
            return -1
        return 1

    def handle_monster_bullets(self, player, win):
        """
        Handles the monster's bullets.

        Args:
            player: The player instance.
            win (pygame.Surface): The surface to draw the bullets on.
        """
        self.update()
        self.draw(win)
        for bullet in self.monster_bullets:
            if bullet.collides_with(player.rect):
                player.take_damage()
                self.monster_bullets.remove(bullet)
            elif bullet.is_out_of_screen():
                self.monster_bullets.remove(bullet)
