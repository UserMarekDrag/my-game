from pathlib import Path
from abc import ABC, abstractmethod

import pygame
from config import Config


config = Config()


class Creature(ABC):
    """
    Abstract class for creating creatures
    """
    def __init__(self, name, image_name, x, y, width, height, health):
        self.move_strategy = None
        self.name = name
        self.image_name = image_name
        self.width = width
        self.height = height
        self.health = health

        # Loading and scaling the image of the creature
        base_dir = Path(__file__).resolve().parent.parent.parent
        creature_file = base_dir / 'game' / 'Assets' / self.image_name
        self.creature_image = pygame.image.load(
            str(creature_file))
        self.CREATURE = pygame.transform.scale(
            self.creature_image, (self.width, self.height))

        self.rect = self.CREATURE.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_alive = True

    @abstractmethod
    def move(self, keys=None, target=None):
        """
        Abstract method to move the creature
        """
        pass

    @abstractmethod
    def reset(self, position_x, position_y):
        """
        Abstract method to reset the position of the creature
        """
        pass

    def draw_on_screen(self, win):
        """
        Method to draw the creature on the screen
        """
        win.blit(self.CREATURE, (self.rect.x, self.rect.y))

    def take_damage(self):
        """
        Method to decrease the health of the creature by a constant damage amount
        """
        self.health -= config.DAMAGE
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
