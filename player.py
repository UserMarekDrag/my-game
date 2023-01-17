from monsters import *
from config import *
from sounds import *


class Hero(Creature):
    __IMAGE_NAME = 'player.png'
    __HERO_HIT = pygame.USEREVENT + 1

    def __init__(self):
        self.FIRST_POSITION_X = 350
        self.FIRST_POSITION_Y = 150
        super().__init__(
            'Hero', self.__IMAGE_NAME, self.FIRST_POSITION_X, self.FIRST_POSITION_Y)

    def static_handle_movement(self, keys_pressed, hero):
        if keys_pressed[pygame.K_LEFT] and hero.x - self.VEL > 0:  # LEFT
            hero.x -= self.VEL
        if keys_pressed[pygame.K_RIGHT] and hero.x + self.VEL + hero.width < WIDTH:  # RIGHT
            hero.x += self.VEL
        if keys_pressed[pygame.K_UP] and hero.y - self.VEL > 0:  # UP
            hero.y -= self.VEL
        if keys_pressed[pygame.K_DOWN] and hero.y + self.VEL + hero.height < HEIGHT:  # DOWN
            hero.y += self.VEL

    def shoot(self, event, hero, hero_bullets):
        if event.key == pygame.K_z and len(hero_bullets) < self.__MAX_BULLETS:
            bullet = pygame.Rect(
                hero.x + hero.width, hero.y + hero.height // 2 - 2, 10, 5)
            hero_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets(self, hero_bullets, enemy):
        for bullet in hero_bullets:
            bullet.x += self.__BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.__HERO_HIT))
                hero_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                hero_bullets.remove(bullet)
            elif bullet.x < 0:
                hero_bullets.remove(bullet)