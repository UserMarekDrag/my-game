import sys
import pygame
from config import *
from sounds import *
from player import *
from monsters import *
from animation import *
from map import *
from menu import *

pygame.display.set_caption(GAME_NAME)


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.boss = Boss()
        self.bat = Monster()
        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH
        self.bat_health = BAT_HEALTH
        self.stop = False

    def events(self, player, boss):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot_left(event, player)
                self.player.shoot_right(event, player)
                self.boss.shoot_right(boss, player)
                self.boss.shoot_left(boss, player)
            if event.type == BOSS_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == PLAYER_HIT_BOSS:
                self.enemy_health = self.boss.hit_enemy(self.enemy_health)
            if event.type == BAT_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == PLAYER_HIT_BAT:
                self.bat_health = self.bat.hit_enemy(self.bat_health)

    def draw(self, player, boss, bat):
        self.win.blit(BACKGROUND_GAME, (0, 0))
        self.clock.tick(FPS)

        self.player.health_draw(self.player_health, self.win, 5, 'Player')
        self.boss.health_draw(self.enemy_health, self.win, 30, 'Boss')

        self.win.blit(self.player.CREATURE, (player.x, player.y))
        self.win.blit(self.boss.CREATURE, (boss.x, boss.y))
        if self.bat_health > 0:
            self.win.blit(self.bat.CREATURE, (bat.x, bat.y))

        pygame.display.update()

    def character_movement(self, player, boss, bat):
        keys_pressed = pygame.key.get_pressed()
        self.player.static_handle_movement(keys_pressed, player)
        self.boss.auto_handle_movement(boss, player)
        self.bat.auto_handle_movement(bat, player)

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

    def update(self, player, boss, bat):
        self.player_health, self.enemy_health = self.player.collision_with_enemy(
            player, boss, self.player_health, self.enemy_health)
        if self.bat_health > 0:
            self.player_health, self.bat_health = self.player.collision_with_enemy(
                player, bat, self.player_health, self.bat_health)
        self.health_count()
        self.character_movement(player, boss, bat)
        self.player.handle_bullets_right(boss, self.win, PLAYER_HIT_BOSS)
        self.player.handle_bullets_left(boss, self.win, PLAYER_HIT_BOSS)
        self.player.handle_bullets_right(bat, self.win, PLAYER_HIT_BAT)
        self.player.handle_bullets_left(bat, self.win, PLAYER_HIT_BAT)
        self.boss.handle_bullets_right(player, self.win, BOSS_HIT_PLAYER)
        self.boss.handle_bullets_left(player, self.win, BOSS_HIT_PLAYER)

    def intro_screen(self):
        intro = True

        title = INITIAL_FONT.render("MAIN MENU", True, GREY)

        play_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 200, "Start Game")
        exit_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 400, "Exit Game")

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = True
                    self.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_position, mouse_pressed):
                intro = False
            elif exit_button.is_pressed(mouse_position, mouse_pressed):
                self.run = False
                pygame.quit()
                sys.exit()

            self.win.blit(BACKGROUND_MENU, (0, 0))
            self.win.blit(title, (340, 100))
            self.win.blit(play_button.image, play_button.rect)
            self.win.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def main(self):
        player = self.player.rect
        boss = self.boss.rect
        bat = self.bat.rect
        while self.run:
            self.events(player, boss)

            if not self.stop:
                self.update(player, boss, bat)
            else:
                break

            self.draw(player, boss, bat)


game = Game()
game.intro_screen()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
