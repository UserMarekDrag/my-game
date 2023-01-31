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
        self.stage = 0
        self.character_choice = "male"
        self.character_dictionary = {
            "male": MALE_CHARACTER,
            "female": FEMALE_CHARACTER,
        }
        self.player = Player(self.character_dictionary[self.character_choice])
        self.boss = Boss()

        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH
        self.bat_health = BAT_HEALTH

        self.stop = False

        self.boss_position = self.boss.rect
        self.player_position = self.player.rect

        self.bat = Monster(0, 0)
        self.bat_1 = Monster(900, 150)
        self.bat_2 = Monster(900, 500)

        self.bat_health = BAT_HEALTH
        self.bat_1_health = BAT_HEALTH
        self.bat_2_health = BAT_HEALTH

        self.bat_position = self.bat.rect
        self.bat_1_position = self.bat.rect
        self.bat_2_position = self.bat.rect

        self.bat_is_alive = False
        self.bat_1_is_alive = False
        self.bat_2_is_alive = False

    def character_update(self):
        self.character_dictionary = {
            "male": MALE_CHARACTER,
            "female": FEMALE_CHARACTER,
        }
        self.player = Player(self.character_dictionary[self.character_choice])

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot_left(event, self.player_position)
                self.player.shoot_right(event, self.player_position)

            if self.stage == 5:
                self.boss.shoot_right(self.boss_position, self.player_position)
                self.boss.shoot_left(self.boss_position, self.player_position)

            if event.type == BOSS_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == PLAYER_HIT_BOSS:
                self.enemy_health = self.boss.hit_enemy(self.enemy_health)
            if event.type == BAT_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == BAT_1_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == BAT_2_HIT_PLAYER:
                self.player_health = self.player.hit_enemy(self.player_health)
            if event.type == PLAYER_HIT_BAT:
                self.bat_health = self.bat.hit_enemy(self.bat_health)
            if event.type == PLAYER_HIT_BAT_1:
                self.bat_1_health = self.bat_1.hit_enemy(self.bat_1_health)
            if event.type == PLAYER_HIT_BAT_2:
                self.bat_2_health = self.bat_2.hit_enemy(self.bat_2_health)

    def draw(self, *bats):
        self.win.blit(BACKGROUND_GAME, (0, 0))
        self.clock.tick(FPS)

        self.player.health_draw(self.player_health, self.win, 5, 'Player')
        self.boss.health_draw(self.enemy_health, self.win, 30, 'Boss')

        self.win.blit(self.player.CREATURE, (self.player_position.x, self.player_position.y))

        if self.stage == 5:
            self.win.blit(self.boss.CREATURE, (self.boss_position.x, self.boss_position.y))

        print(self.stage)

        for bat in bats:
            if self.bat_health > 0 and self.stage > 0 and bat == self.bat_position:
                self.win.blit(self.bat.CREATURE, (bat.x, bat.y))
            elif self.bat_1_health > 0 and self.stage > 1 and bat == self.bat_1_position:
                self.win.blit(self.bat_1.CREATURE, (bat.x, bat.y))
            elif self.bat_2_health > 0 and self.stage > 2 and bat == self.bat_2_position:
                self.win.blit(self.bat_2.CREATURE, (bat.x, bat.y))
            else:
                pass

        pygame.display.update()

    def character_movement(self, bat, bat_1, bat_2):
        keys_pressed = pygame.key.get_pressed()
        self.player.static_handle_movement(keys_pressed, self.player_position)

        if self.stage == 5:
            self.boss.auto_handle_movement(self.boss_position, self.player_position)

        if self.bat_health > 0:
            self.bat.auto_handle_movement(bat, self.player_position)
        elif self.bat_health == 0 and self.stage == 5:
            bat.x = 950
            bat.y = 0
        else:
            pass

        if self.bat_1_health > 0:
            self.bat.auto_handle_movement(bat_1, self.player_position)
        elif self.bat_1_health == 0 and self.stage == 5:
            bat_1.x = 950
            bat_1.y = 0
        else:
            pass

        if self.bat_2_health > 0:
            self.bat.auto_handle_movement(bat_2, self.player_position)
        elif self.bat_2_health == 0 and self.stage == 5:
            bat_2.x = 950
            bat_2.y = 0
        else:
            pass

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

    def update(self, bat, bat_1, bat_2):
        self.player_health, self.enemy_health = self.player.collision_with_enemy(
            self.player_position, self.boss_position, self.player_health, self.enemy_health)
        if self.bat_health > 0:
            self.player_health, self.bat_health = self.player.collision_with_enemy(
                self.player_position, bat, self.player_health, self.bat_health)
        if self.bat_1_health > 0:
            self.player_health, self.bat_1_health = self.player.collision_with_enemy(
                self.player_position, bat_1, self.player_health, self.bat_1_health)
        if self.bat_2_health > 0:
            self.player_health, self.bat_2_health = self.player.collision_with_enemy(
                self.player_position, bat_2, self.player_health, self.bat_2_health)
        self.health_count()
        self.character_movement(bat, bat_1, bat_2)
        self.player.handle_bullets_right(self.boss_position, self.win, PLAYER_HIT_BOSS)
        self.player.handle_bullets_left(self.boss_position, self.win, PLAYER_HIT_BOSS)
        self.player.handle_bullets_right(bat, self.win, PLAYER_HIT_BAT)
        self.player.handle_bullets_left(bat, self.win, PLAYER_HIT_BAT)
        self.player.handle_bullets_right(bat_1, self.win, PLAYER_HIT_BAT_1)
        self.player.handle_bullets_left(bat_1, self.win, PLAYER_HIT_BAT_1)
        self.player.handle_bullets_right(bat_2, self.win, PLAYER_HIT_BAT_2)
        self.player.handle_bullets_left(bat_2, self.win, PLAYER_HIT_BAT_2)
        self.boss.handle_bullets_right(self.player_position, self.win, BOSS_HIT_PLAYER)
        self.boss.handle_bullets_left(self.player_position, self.win, BOSS_HIT_PLAYER)

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
        self.player_position.x = 350
        self.player_position.y = 150

        self.boss = Boss()
        self.boss_position.x = 900
        self.boss_position.y = 600

        self.player_health = PLAYER_HEALTH
        self.enemy_health = ENEMY_HEALTH

        self.stop = False
        self.stage = 0

        self.bat = Monster(0, 0)
        self.bat_1 = Monster(900, 150)
        self.bat_2 = Monster(900, 500)

        self.bat_health = BAT_HEALTH
        self.bat_1_health = BAT_HEALTH
        self.bat_2_health = BAT_HEALTH

        self.bat_position = self.bat.rect
        self.bat_1_position = self.bat.rect
        self.bat_2_position = self.bat.rect

        self.bat_is_alive = False
        self.bat_1_is_alive = False
        self.bat_2_is_alive = False

        self.main()

    def next_stage_values(self):
        if self.stage < 5:

            self.bat_is_alive = False
            self.bat_1_is_alive = False
            self.bat_2_is_alive = False

            self.bat = Monster(0, 0)
            self.bat_1 = Monster(900, 150)
            self.bat_2 = Monster(900, 500)

            self.bat_position = self.bat.rect
            self.bat_1_position = self.bat_1.rect
            self.bat_2_position = self.bat_2.rect

            self.bat_health = BAT_HEALTH
            self.bat_1_health = BAT_HEALTH
            self.bat_2_health = BAT_HEALTH

            if self.stage == 5:
                pass
        else:
            pass

    def next_stage(self):

        if self.bat_health < 1:
            self.bat_is_alive = True

        if self.bat_1_health < 1:
            self.bat_1_is_alive = True

        if self.bat_2_health < 1:
            self.bat_2_is_alive = True

        stage_1 = [self.bat_is_alive]
        stage_2 = [self.bat_is_alive, self.bat_1_is_alive]
        stage_3 = [self.bat_is_alive, self.bat_1_is_alive, self.bat_2_is_alive]

        print('Stage 1:', stage_1)
        print('Stage 2:', stage_2)
        print('Stage 3:', stage_3)

        if self.stage == 0:
            print('warunek 1 spełniony')
            self.next_stage_values()
            return self.stage + 1

        elif all(stage_1) is True and self.stage == 1:
            print('warunek 1 spełniony')
            self.next_stage_values()
            return self.stage + 1
        elif all(stage_2) is True and self.stage == 2:
            print('warunek 2 spełniony')
            self.next_stage_values()
            return self.stage + 1
        elif all(stage_3) is True and self.stage == 3:
            print('warunek 3 spełniony')
            self.next_stage_values()
            return self.stage + 1
        elif all(stage_3) is True and self.stage == 4:
            print('warunek 3 spełniony')
            self.next_stage_values()
            return self.stage + 1
        else:
            return self.stage

    def main(self):

        while self.run:
            self.stage = self.next_stage()
            self.events()
            if not self.stop:
                self.update(self.bat_position, self.bat_1_position, self.bat_2_position)
            else:
                break
            self.draw(self.bat_position, self.bat_1_position, self.bat_2_position)


game = Game()
game.menu_screen()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
