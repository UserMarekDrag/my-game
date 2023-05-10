import pygame
from config import Config
from backgrounds import Backgrounds
from display_text import DisplayText


backgrounds = Backgrounds()
config = Config()


class DisplayManager:
    """
    A class responsible for managing all display-related aspects of the game.
    """

    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.display_text = DisplayText(self.window)

    def draw(self, player, level_manager):
        """
        Draw game objects, such as the player, enemies and stats, on the screen.
        """
        self.clear_screen()
        self.draw_background()
        self.draw_characters(player, level_manager.get_enemies())
        self.draw_stats(player, level_manager)
        pygame.display.update()

    def clear_screen(self):
        """
        Clear the screen by filling it with black color.
        """
        self.window.fill((0, 0, 0))

    def draw_background(self):
        """
        Draw the game's background.
        """
        self.window.blit(backgrounds.BACKGROUND_STATS, (0, 0))
        self.window.blit(backgrounds.BACKGROUND_GAME, (0, 30))
        self.clock.tick(config.FPS)

    def draw_characters(self, player, enemies):
        """
        Draw the player and enemies on the screen.
        """
        player.draw_on_screen(self.window)
        for enemy in enemies:
            if enemy.is_alive:
                enemy.draw_on_screen(self.window)

    def draw_stats(self, player, level_manager):
        """
        Draw the player's health and the current level.
        If level is 5, also draw the boss's health.
        """
        self.display_text.txt_draw(player.health, 10, 1, 'Player', 'Health', config.HEALTH_FONT)
        self.display_text.txt_draw(level_manager.level, 400, 1, 'Level', '', config.HEALTH_FONT)

        if level_manager.level == 5:
            self.display_text.txt_draw(level_manager.get_boss_hp, 700, 1, 'Boss', 'Health', config.HEALTH_FONT)

    def draw_winner(self, winner_text):
        """
        Display the winner's text in the center of the screen.
        """
        draw_text = config.WINNER_FONT.render(winner_text, True, config.WHITE)
        self.window.blit(draw_text, (config.WIDTH / 2 - draw_text.get_width() / 2,
                                     config.HEIGHT / 2 - draw_text.get_height()))
        pygame.display.update()
        pygame.time.wait(2000)
        return draw_text

    def draw_level(self, level_manager):
        """
        Display the current level number.
        """
        self.draw_background()
        pygame.display.update()
        self.display_text.txt_draw(level_manager.level, config.WIDTH / 2 - 200, config.HEIGHT / 2 - 150,
                                   'Level', '', config.LEVEL_NUMB_FONT)

        pygame.display.update()
        pygame.time.wait(1000)
