import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 80, 160
VEL_PLAYER = 5
VEL_ENEMY = 2
BULLET_VEL = 5
MAX_BULLETS = 3

PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2

PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
ENEMY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'enemy.png'))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))


def draw_windows(player, enemy, enemy_bullets, player_bullets):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(PLAYER, (player.x, player.y))
    WIN.blit(ENEMY, (enemy.x, enemy.y))

    for bullet in enemy_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in player_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def player_handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL_PLAYER > 0:  # LEFT
        player.x -= VEL_PLAYER
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL_PLAYER + player.width < WIDTH:  # RIGHT
        player.x += VEL_PLAYER
    if keys_pressed[pygame.K_UP] and player.y - VEL_PLAYER > 0:  # UP
        player.y -= VEL_PLAYER
    if keys_pressed[pygame.K_DOWN] and player.y + VEL_PLAYER + player.height < HEIGHT:  # DOWN
        player.y += VEL_PLAYER


def enemy_handle_movement(enemy, player):
    if player.x > enemy.x:
        enemy.x += VEL_ENEMY
    if player.x < enemy.x:
        enemy.x -= VEL_ENEMY
    if player.y > enemy.y:
        enemy.y += VEL_ENEMY
    if player.y < enemy.y:
        enemy.y -= VEL_ENEMY


def handle_bullets(player_bullets, player, enemy_bullets, enemy):
    for bullet in player_bullets:
        bullet.x += BULLET_VEL
        if enemy.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ENEMY_HIT))
            player_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            player_bullets.remove(bullet)
        elif bullet.x < 0:
            player_bullets.remove(bullet)

    for bullet in enemy_bullets:
        bullet.x -= BULLET_VEL
        if player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            enemy_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            enemy_bullets.remove(bullet)
        elif bullet.x < 0:
            enemy_bullets.remove(bullet)


def main():
    player = pygame.Rect(300, 150, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy = pygame.Rect(700, 150, PLAYER_WIDTH, PLAYER_HEIGHT)

    player_bullets = []
    enemy_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and len(player_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        player.x + player.width, player.y + player.height//2 - 2, 10, 5)
                    player_bullets.append(bullet)

                if (player.x, player.y) != (enemy.x, enemy.y) and len(enemy_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        enemy.x, enemy.y + enemy.height//2 - 2, 10, 5)
                    enemy_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()

        enemy_handle_movement(enemy, player)
        player_handle_movement(keys_pressed, player)

        handle_bullets(player_bullets, player, enemy_bullets, enemy)

        draw_windows(player, enemy, enemy_bullets, player_bullets)

    pygame.quit()


if __name__ == '__main__':
    main()
