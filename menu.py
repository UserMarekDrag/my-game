import sys
import pygame
from button import ButtonBuilder
from config import Config
from backgrounds import Backgrounds
from player import Player

config = Config()
backgrounds = Backgrounds()


class Menu:
    def __init__(self, game):
        self.game = game

        self.character_choice = "male"
        self.character_dictionary = {
            "male": config.MALE_CHARACTER,
            "female": config.FEMALE_CHARACTER,
        }
        self.buttons = {}

    def character_update(self):
        return self.character_dictionary[self.character_choice]

    def create_buttons(self):
        button_builder = ButtonBuilder()
        self.buttons["start"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 260)
                                 .set_content("Start Game")
                                 .build())

        self.buttons["options"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 330)
                                   .set_content("Character")
                                   .build())

        self.buttons["quit"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 400)
                                .set_content("Exit Game")
                                .build())
        self.buttons["char_male"] = (button_builder.set_position(190, 400)
                                     .set_content("Male")
                                     .build())
        self.buttons["char_female"] = (button_builder.set_position(470, 400)
                                       .set_content("Female")
                                       .build())

    def menu_screen(self):
        main_menu = True

        self.create_buttons()

        while main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.run = False
                    pygame.quit()
                    sys.exit()

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.buttons["start"].is_pressed(mouse_position, mouse_pressed):
                main_menu = False

            elif self.buttons["options"].is_pressed(mouse_position, mouse_pressed):
                self.game.win.blit(backgrounds.BACKGROUND_MENU, (0, 0))
                pygame.display.update()
                pygame.time.wait(100)
                main_menu = self.menu_choice_char()

            elif self.buttons["quit"].is_pressed(mouse_position, mouse_pressed):
                self.game.run = False
                pygame.quit()
                sys.exit()

            self.game.win.blit(backgrounds.BACKGROUND_MENU, (0, 0))
            self.game.win.blit(backgrounds.LOGO, (270, 50))

            self.buttons["start"].draw_on_screen(self.game.win)
            self.buttons["options"].draw_on_screen(self.game.win)
            self.buttons["quit"].draw_on_screen(self.game.win)

            self.game.clock.tick(config.FPS)
            pygame.display.update()

    def menu_choice_char(self):
        menu_char = True

        male_player = Player(config.MALE_CHARACTER)
        female_player = Player(config.FEMALE_CHARACTER)

        while menu_char:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_char = False
                    self.game.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.buttons["char_male"].is_pressed(mouse_position, mouse_pressed):
                self.character_choice = "male"
                self.character_update()
                return False

            elif self.buttons["char_female"].is_pressed(mouse_position, mouse_pressed):
                self.character_choice = "female"
                self.character_update()
                return False

            self.game.win.blit(male_player.CREATURE_IMAGE, (310, 150))
            self.game.win.blit(female_player.CREATURE_IMAGE, (500, 150))

            self.buttons["char_male"].draw_on_screen(self.game.win)
            self.buttons["char_female"].draw_on_screen(self.game.win)

            self.game.clock.tick(config.FPS)
            pygame.display.update()

    def menu_end(self, draw_text):
        menu_end = True

        while menu_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_end = False
                    self.game.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.buttons["start"].is_pressed(mouse_position, mouse_pressed):
                menu_end = False
                self.game.new_game()

            elif self.buttons["quit"].is_pressed(mouse_position, mouse_pressed):
                self.game.run = False
                pygame.quit()
                sys.exit()

            self.game.win.blit(draw_text, (config.WIDTH / 2 - draw_text.get_width() / 2,
                                           config.HEIGHT / 2 - draw_text.get_height()))

            self.buttons["start"].draw_on_screen(self.game.win)
            self.buttons["quit"].draw_on_screen(self.game.win)

            self.game.clock.tick(config.FPS)
            pygame.display.update()
