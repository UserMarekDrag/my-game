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
        self.character_choice = "male"
        self.character_dictionary = {
            "male": MALE_CHARACTER,
            "female": FEMALE_CHARACTER,
        }
        self.player = Player(self.character_dictionary[self.character_choice])
        self.boss = Boss()
        self.bat = Monster()
        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH
        self.bat_health = BAT_HEALTH
        self.stop = False

    def character_update(self):
        self.character_dictionary = {
            "male": MALE_CHARACTER,
            "female": FEMALE_CHARACTER,
        }
        self.player = Player(self.character_dictionary[self.character_choice])

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
            winner_text = 'You Win!'

        if self.player_health <= 0:
            winner_text = 'You died'

        if winner_text != "":
            self.draw_winner(winner_text)
            self.stop = True

    def draw_winner(self, winner_text):
        draw_text = WINNER_FONT.render(winner_text, True, WHITE)
        self.win.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                                  HEIGHT / 2 - draw_text.get_height()))
        pygame.display.update()
        pygame.time.wait(2000)
        self.menu_end(draw_text)

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

    def menu_screen(self):
        main_menu = True

        play_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 260, "Start Game")
        choose_char_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 330, "Character")
        exit_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 400, "Exit Game")

        while main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_position, mouse_pressed):
                main_menu = False

            elif choose_char_button.is_pressed(mouse_position, mouse_pressed):
                self.win.blit(BACKGROUND_MENU, (0, 0))
                pygame.display.update()
                pygame.time.wait(100)
                main_menu = self.menu_choice_char()

            elif exit_button.is_pressed(mouse_position, mouse_pressed):
                self.run = False
                pygame.quit()
                sys.exit()

            self.win.blit(BACKGROUND_MENU, (0, 0))
            self.win.blit(LOGO, (270, 50))
            self.win.blit(play_button.image, play_button.rect)
            self.win.blit(choose_char_button.image, choose_char_button.rect)
            self.win.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def menu_choice_char(self):
        menu_char = True

        male_player = Player(MALE_CHARACTER)
        female_player = Player(FEMALE_CHARACTER)

        char_male_button = Button(190, 400, "MALE")
        char_female_button = Button(470, 400, "FEMALE")

        while menu_char:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_char = False
                    self.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if char_male_button.is_pressed(mouse_position, mouse_pressed):
                self.character_choice = "male"
                self.character_update()
                return False

            elif char_female_button.is_pressed(mouse_position, mouse_pressed):
                self.character_choice = "female"
                self.character_update()
                return False

            self.win.blit(male_player.CREATURE_IMAGE, (310, 150))
            self.win.blit(female_player.CREATURE_IMAGE, (500, 150))
            self.win.blit(char_male_button.image, char_male_button.rect)
            self.win.blit(char_female_button.image, char_female_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def menu_end(self, draw_text):
        menu_end = True

        play_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 330, "Start Again")
        exit_button = Button(WIDTH / 2 - BUTTON_WIDTH / 2, 400, "Exit Game")

        while menu_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_end = False
                    self.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_position, mouse_pressed):
                menu_end = False
                self.new_game()

            elif exit_button.is_pressed(mouse_position, mouse_pressed):
                self.run = False
                pygame.quit()
                sys.exit()

            self.win.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                                      HEIGHT / 2 - draw_text.get_height()))
            self.win.blit(play_button.image, play_button.rect)
            self.win.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def new_game(self):
        self.run = True
        self.player = Player(self.character_dictionary[self.character_choice])
        self.boss = Boss()
        self.bat = Monster()
        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH
        self.bat_health = BAT_HEALTH
        self.stop = False

        self.main()

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
game.menu_screen()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
