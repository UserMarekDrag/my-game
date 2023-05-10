import pygame
from config import Config
from player import Player
from monster import Monster
from enemy import Mage, Boss
from backgrounds import Backgrounds
from level_manager import LevelManager
from display_manager import DisplayManager

backgrounds = Backgrounds()
config = Config()

pygame.display.set_caption(config.GAME_NAME)


class Game:

    __shooting_enemies = (Mage, Boss)

    def __init__(self, menu):
        self.window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.display_manager = DisplayManager(self.window)
        self.run = True
        self.stop = False
        self.player = None
        self.level_manager = LevelManager()
        self.menu = menu

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot(event)

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive and isinstance(enemy, self.__shooting_enemies):
                enemy.shoot(self.player)

    def character_movement(self):
        keys_pressed = pygame.key.get_pressed()

        self.player.move(keys=keys_pressed)

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive:
                enemy.move(target=self.player.rect)

    def who_win(self):
        winner_text = ""
        if self.level_manager.all_enemies_defeated and self.level_manager.level == 5:
            winner_text = 'You Win!'

        elif not self.player.is_alive:
            winner_text = 'You died'

        if winner_text != "":
            draw_text = self.display_manager.draw_winner(winner_text)
            self.menu.menu_end(draw_text)
            self.stop = True

    def update_fight(self):
        self.character_movement()

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive:
                self.player.check_collision(enemy, Monster)
                self.player.handle_bullets(enemy=enemy, win=self.window)
                enemy.handle_monster_bullets(player=self.player, win=self.window)

        pygame.display.update()

    def new_game(self):
        self.level_manager.level = 1
        self.level_manager.enemies = []
        self.player.reset()

        self.run = True
        self.main()

    def next_level(self):

        if all(enemy.is_alive is False for enemy in self.level_manager.get_enemies()):
            self.display_manager.draw_level(self.level_manager)
            self.level_manager.go_to_next_level()
        else:
            return

    def main(self):
        self.player = Player(self.menu.character_update())

        while self.run:
            self.next_level()
            self.events()
            if not self.stop:
                self.update_fight()
                self.who_win()
            else:
                break
            self.display_manager.draw(self.player, self.level_manager)
