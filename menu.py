import sys
import pygame
from button import ButtonBuilder
from config import Config
from backgrounds import Backgrounds
from player import Player
from menu_commands import StartGameCommand, OptionsCommand, QuitGameCommand, \
    ChooseMaleCharacterCommand, ChooseFemaleCharacterCommand, RestartGameCommand

config = Config()
backgrounds = Backgrounds()


class Menu:
    """
    A class representing the game menu.
    """
    def __init__(self, game):
        self.game = game

        self.character_choice = "male"
        self.character_dictionary = {
            "male": config.MALE_CHARACTER,
            "female": config.FEMALE_CHARACTER,
        }
        self.buttons = {}

    def character_update(self):
        """
        Update the chosen character based on the user's selection.
        """
        return self.character_dictionary[self.character_choice]

    def create_buttons(self):
        """
        Create buttons for the menu.
        """
        button_builder = ButtonBuilder()
        self.buttons["start"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 260)
                                 .set_content("Start Game")
                                 .set_action(StartGameCommand(self))
                                 .build())

        self.buttons["restart"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 330)
                                   .set_content("Restart game")
                                   .set_action(RestartGameCommand(self))
                                   .build())

        self.buttons["options"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 330)
                                   .set_content("Character")
                                   .set_action(OptionsCommand(self))
                                   .build())

        self.buttons["quit"] = (button_builder.set_position(config.WIDTH / 2 - config.BUTTON_WIDTH / 2, 400)
                                .set_content("Exit Game")
                                .set_action(QuitGameCommand(self))
                                .build())

        self.buttons["char_male"] = (button_builder.set_position(190, 400)
                                     .set_content("Male")
                                     .set_action(ChooseMaleCharacterCommand(self))
                                     .build())

        self.buttons["char_female"] = (button_builder.set_position(470, 400)
                                       .set_content("Female")
                                       .set_action(ChooseFemaleCharacterCommand(self))
                                       .build())

    def handle_button_click(self, button, mouse_position, mouse_pressed):
        """
        Handle the button click event.
        """
        if button.is_pressed(mouse_position, mouse_pressed):
            return button.action.execute()
        return None

    def menu_screen(self):
        """
        Display the main menu screen.
        """
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

            result = self.handle_button_click(self.buttons["start"], mouse_position, mouse_pressed)
            if result is not None:
                main_menu = result

            result = self.handle_button_click(self.buttons["options"], mouse_position, mouse_pressed)
            if result is not None:
                main_menu = result

            result = self.handle_button_click(self.buttons["quit"], mouse_position, mouse_pressed)
            if result is not None:
                main_menu = result

            self.game.window.blit(backgrounds.BACKGROUND_MENU, (0, 0))
            self.game.window.blit(backgrounds.LOGO, (270, 50))

            self.buttons["start"].draw_on_screen(self.game.window)
            self.buttons["options"].draw_on_screen(self.game.window)
            self.buttons["quit"].draw_on_screen(self.game.window)

            self.game.clock.tick(config.FPS)
            pygame.display.update()

    def menu_choice_char(self):
        """
        Display the character selection menu.
        """
        menu_char = True
        self.create_buttons()

        male_player = Player(config.MALE_CHARACTER)
        female_player = Player(config.FEMALE_CHARACTER)

        while menu_char:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_char = False
                    self.game.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            result = self.handle_button_click(self.buttons["char_male"], mouse_position, mouse_pressed)
            if result is not None:
                return result

            result = self.handle_button_click(self.buttons["char_female"], mouse_position, mouse_pressed)
            if result is not None:
                return result

            self.game.window.blit(male_player.CREATURE_IMAGE, (310, 150))
            self.game.window.blit(female_player.CREATURE_IMAGE, (500, 150))

            self.buttons["char_male"].draw_on_screen(self.game.window)
            self.buttons["char_female"].draw_on_screen(self.game.window)

            self.game.clock.tick(config.FPS)
            pygame.display.update()

    def menu_end(self, draw_text):
        """
        Display the end menu screen.
        """
        menu_end = True

        while menu_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_end = False
                    self.game.run = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            result = self.handle_button_click(self.buttons["restart"], mouse_position, mouse_pressed)
            if result is not None:
                menu_end = result

            result = self.handle_button_click(self.buttons["quit"], mouse_position, mouse_pressed)
            if result is not None:
                menu_end = result

            self.game.window.blit(draw_text, (config.WIDTH / 2 - draw_text.get_width() / 2,
                                              config.HEIGHT / 2 - draw_text.get_height()))

            self.buttons["restart"].draw_on_screen(self.game.window)
            self.buttons["quit"].draw_on_screen(self.game.window)

            self.game.clock.tick(config.FPS)
            pygame.display.update()
