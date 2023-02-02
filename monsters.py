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
        self.FIRST_POSITION_X = 900
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 60
        self.SIZE_HEIGHT = 100
        super().__init__(
            'Boss', BOSS_IMAGE, self.FIRST_POSITION_X,
            self.FIRST_POSITION_Y, self.SIZE_WIDTH, self.SIZE_HEIGHT)

        self.boss_bullets_right = []
        self.boss_bullets_left = []
        self.position = 'center'
        self.time_break = True
        self.time_step = 50

    def waiting(self):
        if self.time_step == 0:
            self.time_break = True
        else:
            self.time_step -= 1

    def auto_handle_movement(self, boss):

        # center
        if self.position == 'center' and self.time_break:
            if boss.x > 400:
                boss.x -= VEL_BOSS
            if boss.y > 150:
                boss.y -= VEL_BOSS
            if boss.x == 400 and boss.y == 150:
                self.position = 'left_up'
                self.time_break = False
                self.time_step = 50

        # wait in center
        elif self.position == 'left_up' and not self.time_break:
            self.waiting()

        #  go to left up
        elif self.position == 'left_up' and self.time_break:
            if boss.x > 100:
                boss.x -= VEL_BOSS
            if boss.y > 80:
                boss.y -= VEL_BOSS
            if boss.x == 100 and boss.y == 80:
                self.position = 'right_up'
                self.time_break = False
                self.time_step = 50

        # wait in left up
        elif self.position == 'right_up' and not self.time_break:
            self.waiting()

        #  go to right up
        elif self.position == 'right_up' and self.time_break:
            if boss.x < 600:
                boss.x += VEL_BOSS
            if boss.x == 600 and boss.y == 80:
                self.position = 'left_down'
                self.time_break = False
                self.time_step = 50

        # wait in right up
        elif self.position == 'left_down' and not self.time_break:
            self.waiting()

        #  go to left_down
        elif self.position == 'left_down' and self.time_break:
            if boss.x > 100:
                boss.x -= VEL_BOSS
            if boss.y < 250:
                boss.y += VEL_BOSS
            if boss.x == 100 and boss.y == 250:
                self.position = 'right_down'
                self.time_break = False
                self.time_step = 50

        # wait in left_down
        elif self.position == 'right_down' and not self.time_break:
            self.waiting()

        #  go to right_down
        elif self.position == 'right_down' and self.time_break:
            if boss.x < 600:
                boss.x += VEL_BOSS
            if boss.x == 600 and boss.y == 250:
                self.position = 'center'
                self.time_break = False
                self.time_step = 50

        # wait in right_down
        elif self.position == 'center' and not self.time_break:
            self.waiting()

    def shoot_right(self, boss, player):
        if boss.x < player.x and len(self.boss_bullets_right) < BOSS_MAX_BULLETS:
            bullet = pygame.Rect(
                boss.x - 10, boss.y + 50, 30, 10)
            self.boss_bullets_right.append(bullet)
            BULLET_FIRE_SOUND.play()

    def shoot_left(self, boss, player):
        if boss.x > player.x and len(self.boss_bullets_left) < BOSS_MAX_BULLETS:
            bullet = pygame.Rect(
                boss.x - 10, boss.y + 50, 30, 10)
            self.boss_bullets_left.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets_right(self, enemy, win, hit):
        for bullet in self.boss_bullets_right:
            bullet.x += BOSS_BULLET_VEL
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
            bullet.x -= BOSS_BULLET_VEL
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

    def __init__(self, first_position_x, first_position_y):
        self.FIRST_POSITION_X = first_position_x
        self.FIRST_POSITION_Y = first_position_y
        self.SIZE_WIDTH = 80
        self.SIZE_HEIGHT = 60
        super().__init__(
            'Monster', MONSTER_IMAGE, self.FIRST_POSITION_X,
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
