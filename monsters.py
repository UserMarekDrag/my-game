import pygame
import os
from config import *
from sounds import *


class Creature:

    def __init__(self, creature_type, image_name, x, y):
        self.creature_type = creature_type

        self.image_name = image_name
        self.SIZE_WIDTH = 40
        self.SIZE_HEIGHT = 80

        self.rect = pygame.Rect(x, y, self.SIZE_WIDTH, self.SIZE_HEIGHT)
        self.x = x
        self.y = y

        self.CREATURE_IMAGE = pygame.image.load(
            os.path.join('Assets', self.image_name))
        self.CREATURE = pygame.transform.scale(
            self.CREATURE_IMAGE, (self.SIZE_WIDTH, self.SIZE_HEIGHT))

    def hit_enemy(self, enemy_health):
        enemy_health -= 1
        BULLET_HIT_SOUND.play()
        return enemy_health

    def health_draw(self, health, win, height, name):
        health_text = HEALTH_FONT.render(
            f"{str(name)} Heath: " + str(health), True, WHITE)

        win.blit(health_text, (10, height))
        # self.draw_update()

    def draw_update(self):
        pygame.display.update()


class Boss(Creature):
    __IMAGE_NAME = 'enemy.png'
    __BOSS_HIT = pygame.USEREVENT + 2

    def __init__(self):
        self.FIRST_POSITION_X = 700
        self.FIRST_POSITION_Y = 150
        super().__init__(
            'Boss', self.__IMAGE_NAME, self.FIRST_POSITION_X, self.FIRST_POSITION_Y)
        self.boss_bullets = []

    def auto_handle_movement(self, monster, hero):
        if hero.x > monster.x:
            monster.x += VEL_BOSS
        if hero.x < monster.x:
            monster.x -= VEL_BOSS
        if hero.y > monster.y:
            monster.y += VEL_BOSS
        if hero.y < monster.y:
            monster.y -= VEL_BOSS

    def shoot(self, boss):
        if len(self.boss_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                boss.x + boss.width, boss.y + boss.height // 2 - 2, 10, 5)
            self.boss_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets(self, enemy, win):
        for bullet in self.boss_bullets:
            bullet.x -= BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(BOSS_HIT))
                self.boss_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                self.boss_bullets.remove(bullet)
            elif bullet.x < 0:
                self.boss_bullets.remove(bullet)
        self.draw_bullets(win)

    def draw_bullets(self, win):
        for bullet in self.boss_bullets:
            pygame.draw.rect(win, RED, bullet)

        pygame.display.update()


class Monster(Creature):

    def __init__(self, image_name):
        super().__init__('Monster', image_name)

    def auto_handle_movement(self, monster, hero):
        if hero.x > monster.x:
            monster.x += self.VEL_MONSTER
        if hero.x < monster.x:
            monster.x -= self.VEL_MONSTER
        if hero.y > monster.y:
            monster.y += self.VEL_MONSTER
        if hero.y < monster.y:
            monster.y -= self.VEL_MONSTER
