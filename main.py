import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")

WHITE = (255, 255, 255)
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 80, 160
VEL = 5
BULLET_VEL = 7

PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))


def draw_windows(player):
    WIN.fill(WHITE)
    WIN.blit(PLAYER, (player.x, player.y))
    pygame.display.update()


def player_handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:  # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH:  # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_UP] and player.y - VEL > 0:  # UP
        player.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player.y + VEL + player.height < HEIGHT:  # DOWN
        player.y += VEL


def main():
    player = pygame.Rect(300, 100, PLAYER_WIDTH, PLAYER_HEIGHT)

    bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                pass

        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)
        draw_windows(player)

    pygame.quit()


if __name__ == '__main__':
    main()
