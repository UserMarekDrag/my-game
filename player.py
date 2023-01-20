from monsters import *
from config import *
from sounds import *


class Player(Creature):
    __IMAGE_NAME = 'player.png'

    def __init__(self):
        self.FIRST_POSITION_X = 350
        self.FIRST_POSITION_Y = 150
        self.SIZE_WIDTH = 40
        self.SIZE_HEIGHT = 80
        super().__init__(
            'Hero', self.__IMAGE_NAME, self.FIRST_POSITION_X, self.FIRST_POSITION_Y,
            self.SIZE_WIDTH, self.SIZE_HEIGHT)
        self.player_bullets = []

    def static_handle_movement(self, keys_pressed, player):
        if keys_pressed[pygame.K_LEFT] and player.x - VEL_PLAYER > 0:  # LEFT
            player.x -= VEL_PLAYER
        if keys_pressed[pygame.K_RIGHT] and player.x + VEL_PLAYER + player.width < WIDTH:  # RIGHT
            player.x += VEL_PLAYER
        if keys_pressed[pygame.K_UP] and player.y - VEL_PLAYER > 0:  # UP
            player.y -= VEL_PLAYER
        if keys_pressed[pygame.K_DOWN] and player.y + VEL_PLAYER + player.height < HEIGHT:  # DOWN
            player.y += VEL_PLAYER

    def shoot(self, event, player):
        if event.key == pygame.K_z and len(self.player_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
            self.player_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

    def handle_bullets(self, enemy, win, hit):
        for bullet in self.player_bullets:
            bullet.x += BULLET_VEL
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(hit))
                self.player_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                self.player_bullets.remove(bullet)
            elif bullet.x < 0:
                self.player_bullets.remove(bullet)
        self.draw_bullets(win)

    def draw_bullets(self, win):
        for bullet in self.player_bullets:
            pygame.draw.rect(win, YELLOW, bullet)
        self.draw_update()
