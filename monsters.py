import pygame
import os
from config import *
from sounds import *


class Creature(pygame.sprite.Sprite):
    # __SIZE_WIDTH = 20
    # __SIZE_HEIGHT = 40
    __VEL = 4
    __BULLET_VEL = 5
    __MAX_BULLETS = 3
    __CREATURE_HIT = pygame.USEREVENT + 1
    __ENEMY_HIT = pygame.USEREVENT + 2

    def __init__(self, creature_type, image_name, x, y):
        self.creature_type = creature_type
        self.VEL = 4

        self.image_name = image_name
        self.SIZE_WIDTH = 20
        self.SIZE_HEIGHT = 40

        self.rect = pygame.Rect(x, y, self.SIZE_WIDTH, self.SIZE_HEIGHT)
        self.x = x
        self.y = y

        self.CREATURE_IMAGE = pygame.image.load(
            os.path.join('Assets', self.image_name))
        self.CREATURE = pygame.transform.scale(
            self.CREATURE_IMAGE, (self.SIZE_WIDTH, self.SIZE_HEIGHT))

    def shoot(self, creature, creature_bullets):
        if len(creature_bullets) < self.__MAX_BULLETS:
            bullet = pygame.Rect(
                creature.x + creature.width, creature.y + creature.height // 2 - 2, 10, 5)
            creature_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets(self, creature_bullets, enemy):
        for bullet in creature_bullets:
            bullet.x -= self.__BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.__ENEMY_HIT))
                creature_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                creature_bullets.remove(bullet)
            elif bullet.x < 0:
                creature_bullets.remove(bullet)


class Boss(Creature):
    __IMAGE_NAME = 'enemy.png'
    __BOSS_HIT = pygame.USEREVENT + 2

    def __init__(self):
        super().__init__('Boss', self.__IMAGE_NAME)

    def auto_handle_movement(self, monster, hero):
        if hero.x > monster.x:
            monster.x += self.__VEL
        if hero.x < monster.x:
            monster.x -= self.__VEL
        if hero.y > monster.y:
            monster.y += self.__VEL
        if hero.y < monster.y:
            monster.y -= self.__VEL


class Monster(Creature):

    def __init__(self, image_name):
        super().__init__('Monster', image_name)

    def auto_handle_movement(self, monster, hero):
        if hero.x > monster.x:
            monster.x += self.__VEL
        if hero.x < monster.x:
            monster.x -= self.__VEL
        if hero.y > monster.y:
            monster.y += self.__VEL
        if hero.y < monster.y:
            monster.y -= self.__VEL
