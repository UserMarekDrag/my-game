import pygame
from config import Config
from player import Player
from backgrounds import Backgrounds
from level_manager import LevelManager
from display_manager import DisplayManager
from events_manager import EventsManager

backgrounds = Backgrounds()
config = Config()

pygame.display.set_caption(config.GAME_NAME)


class Game:
    """
    Main Game class responsible for the game loop, checking the game state and controlling the game flow.
    """

    def __init__(self, menu):
        self.window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.display_manager = DisplayManager(self.window)
        self.events_manager = EventsManager(self.window)
        self.clock = pygame.time.Clock()
        self.run = True
        self.stop = False
        self.player = None
        self.level_manager = LevelManager()
        self.menu = menu

    def check_winner(self):
        """
        Check for the game end condition and return the winner.
        """
        if self.level_manager.all_enemies_defeated and self.level_manager.level == 5:
            return 'You Win!'
        if not self.player.is_alive:
            return 'You died'
        return None

    def draw_winner_and_end_game(self, winner_text):
        """
        Display the winner and end the game.
        """
        self.display_manager.draw_winner(winner_text)
        self.stop = True

    def who_win(self):
        """
        Determine the winner and end the game if a winner is found.
        """
        winner_text = None
        if self.level_manager.all_enemies_defeated and self.level_manager.level == 5:
            winner_text = 'You Win!'

        elif not self.player.is_alive:
            winner_text = 'You died'

        if winner_text:
            draw_text = self.display_manager.draw_winner(winner_text)
            self.menu.menu_end(draw_text)
            self.stop = True

    def new_game(self):
        """
        Start a new game, resetting the level and player.
        """
        self.level_manager.level = 0
        self.level_manager.enemies = []
        self.player.reset()

        self.run = True
        self.main()

    def next_level(self):
        """
        Advance to the next level if all enemies are defeated.
        """
        if all(enemy.is_alive is False for enemy in self.level_manager.get_enemies()):
            self.level_manager.go_to_next_level()
            self.display_manager.draw_level(self.level_manager)
        else:
            return

    def main(self):
        """
        Main game loop, handling game events and updates.
        """
        self.player = Player(self.menu.character_update())
        while self.run:
            self.next_level()
            self.events_manager.handle_user_input(self.player)
            if not self.stop:
                self.events_manager.events(self.level_manager, self.player)
                self.who_win()
            else:
                break
            self.display_manager.draw(self.player, self.level_manager)
            self.run = self.events_manager.run
