import pygame
import os
from config import *
from sounds import *


class Creature:

    def __init__(self, creature_type, image_name, x, y, size_width, size_height):
        self.creature_type = creature_type
        self.image_name = image_name
        self.size_width = size_width
        self.size_height = size_height
        self.rect = pygame.Rect(x, y, size_width, size_height)
        self.x = x
        self.y = y

        self.CREATURE_IMAGE = pygame.image.load(
            os.path.join('Assets', self.image_name))
        self.CREATURE = pygame.transform.scale(
            self.CREATURE_IMAGE, (self.size_width, self.size_height))

    def hit_enemy(self, enemy_health):
        enemy_health -= 1
        BULLET_HIT_SOUND.play()
        return enemy_health

    def health_draw(self, health, win, height, name):
        health_text = HEALTH_FONT.render(
            f"{str(name)} Heath: " + str(health), True, WHITE)

        win.blit(health_text, (10, height))

    def draw_update(self):
        pygame.display.update()

    def collision_with_enemy(self, player, enemy, player_health, enemy_health):
        collide = pygame.Rect.colliderect(player, enemy)

        if collide:
            if player.x < enemy.x and player.x > 10:
                player.x -= COLLISION_VEL
                pygame.time.wait(100)
            elif player.x > enemy.x and player.x < (WIDTH - 40):
                player.x += COLLISION_VEL
                pygame.time.wait(100)
            elif player.y < enemy.y and player.y > 20:
                player.y -= COLLISION_VEL
                pygame.time.wait(100)
            elif player.y > enemy.y and player.y < HEIGHT - 80:
                player.y += COLLISION_VEL
                pygame.time.wait(100)

            player_health = self.hit_enemy(player_health)
            enemy_health = self.hit_enemy(enemy_health)

        self.draw_update()
        return player_health, enemy_health


class Boss(Creature):

    def __init__(self):
        self.FIRST_POSITION_X = 700
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 150
        self.SIZE_HEIGHT = 190
        super().__init__(
            'Boss', BOSS_IMAGE, self.FIRST_POSITION_X,
            self.FIRST_POSITION_Y, self.SIZE_WIDTH, self.SIZE_HEIGHT)

        self.boss_bullets_right = []
        self.boss_bullets_left = []

    def auto_handle_movement(self, boss, player):

        if boss.x > player.x and boss.x > 50:
            if boss.x > player.x + 150:
                boss.x -= VEL_BOSS
            elif boss.x > player.x:
                boss.x += VEL_BOSS

        if boss.x < player.x and boss.x < WIDTH - 50:
            if boss.x < player.x - 150:
                boss.x += VEL_BOSS
            elif boss.x < player.x:
                boss.x -= VEL_BOSS

        if boss.y > player.y and boss.y > 50:
            if boss.y > player.y + 100:
                boss.y -= VEL_BOSS
            elif boss.y > player.y:
                boss.y += VEL_BOSS

        if boss.y < player.y and boss.y < HEIGHT - 50:
            if boss.y > player.y - 150:
                boss.y += VEL_BOSS
            elif boss.y < player.y:
                boss.y -= VEL_BOSS

    def shoot_right(self, boss, player):
        if boss.x < player.x and len(self.boss_bullets_right) < MAX_BULLETS:
            bullet = pygame.Rect(
                boss.x + boss.width, boss.y + boss.height // 2 - 2, 10, 5)
            self.boss_bullets_right.append(bullet)
            BULLET_FIRE_SOUND.play()

    def shoot_left(self, boss, player):
        if boss.x > player.x and len(self.boss_bullets_left) < MAX_BULLETS:
            bullet = pygame.Rect(
                boss.x + boss.width, boss.y + boss.height // 2 - 2, 10, 5)
            self.boss_bullets_left.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets_right(self, enemy, win, hit):
        for bullet in self.boss_bullets_right:
            bullet.x += BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                self.boss_bullets_right.remove(bullet)
            elif bullet.x > WIDTH:
                self.boss_bullets_right.remove(bullet)
            elif bullet.x < 0:
                self.boss_bullets_right.remove(bullet)
        self.draw_bullets(win, self.boss_bullets_right)

    def handle_bullets_left(self, enemy, win, hit):
        for bullet in self.boss_bullets_left:
            bullet.x -= BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                self.boss_bullets_left.remove(bullet)
            elif bullet.x > WIDTH:
                self.boss_bullets_left.remove(bullet)
            elif bullet.x < 0:
                self.boss_bullets_left.remove(bullet)
        self.draw_bullets(win, self.boss_bullets_left)

    def draw_bullets(self, win, boss_bullets):
        for bullet in boss_bullets:
            pygame.draw.rect(win, RED, bullet)

        pygame.display.update()


class Monster(Creature):

    def __init__(self):
        self.FIRST_POSITION_X = 900
        self.FIRST_POSITION_Y = 0
        self.SIZE_WIDTH = 80
        self.SIZE_HEIGHT = 60
        super().__init__(
            'Monster', MONSTRER_IMAGE, self.FIRST_POSITION_X,
            self.FIRST_POSITION_Y, self.SIZE_WIDTH, self.SIZE_HEIGHT)

    def auto_handle_movement(self, monster, player):
        if player.x > monster.x:
            monster.x += VEL_MONSTER
        if player.x < monster.x:
            monster.x -= VEL_MONSTER
        if player.y > monster.y:
            monster.y += VEL_MONSTER
        if player.y < monster.y:
            monster.y -= VEL_MONSTER
