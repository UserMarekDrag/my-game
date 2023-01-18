import sys
import pygame
from config import *
from sounds import *
from player import *
from monsters import *
from animation import *
from map import *

pygame.display.set_caption(GAME_NAME)


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.boss = Boss()
        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH
        self.stop = False

    def events(self, player, boss):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot(event, player)
                self.boss.shoot(boss)
            if event.type == BOSS_HIT:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == PLAYER_HIT:
                self.enemy_health = self.boss.hit_enemy(self.enemy_health)

    def draw(self, player, boss):
        self.win.blit(BACKGROUND, (0, 0))
        self.clock.tick(FPS)

        self.player.health_draw(self.player_health, self.win, 5, 'Player')
        self.boss.health_draw(self.enemy_health, self.win, 30, 'Boss')

        self.win.blit(self.player.CREATURE, (player.x, player.y))
        self.win.blit(self.boss.CREATURE, (boss.x, boss.y))

        pygame.display.update()

    def character_movement(self, player, boss):
        keys_pressed = pygame.key.get_pressed()
        self.player.static_handle_movement(keys_pressed, player)
        self.boss.auto_handle_movement(boss, player)

    def health_count(self):
        winner_text = ""
        if self.enemy_health <= 0:
            winner_text = 'Player Wins!'

        if self.player_health <= 0:
            winner_text = 'Enemy Wins!'

        if winner_text != "":
            self.draw_winner(winner_text)
            self.stop = True

    def draw_winner(self, winner_text):
        draw_text = WINNER_FONT.render(winner_text, True, WHITE)
        self.win.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                                  HEIGHT / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(2000)

    def main(self):
        player = self.player.rect
        boss = self.boss.rect
        while self.run:
            self.events(player, boss)
            self.health_count()
            if self.stop: break
            self.character_movement(player, boss)
            self.player.handle_bullets(boss, self.win)
            self.boss.handle_bullets(player, self.win)
            self.draw(player, boss)


game = Game()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
