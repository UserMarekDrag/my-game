import sys
import pygame
from config import Config
from player import Player
from monster import Monster
from enemy import Mage, Boss
from backgrounds import Backgrounds
from menu import Menu
from level_manager import LevelManager

backgrounds = Backgrounds()
config = Config()

pygame.display.set_caption(config.GAME_NAME)


class Game:

    __shooting_enemies = (Mage, Boss)

    def __init__(self):
        self.window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.stop = False
        self.next_level_draw = True
        self.player = None
        self.level_manager = LevelManager()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot(event)

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive and isinstance(enemy, self.__shooting_enemies):
                enemy.shoot(self.player)

    def txt_draw(self, health, width, height, name, health_txt, font):
        text = font.render(
            f"{str(name)} {str(health_txt)}: " + str(health), True, config.BLUE)

        self.window.blit(text, (width, height))

    def draw_level(self):
        self.txt_draw(
            self.level_manager.level,
            config.WIDTH / 2 - 200,
            config.HEIGHT / 2 - 150,
            'Level',
            '',
            config.LEVEL_NUMB_FONT
        )

        pygame.display.update()
        pygame.time.wait(1000)

    def draw(self):
        self.window.blit(backgrounds.BACKGROUND_STATS, (0, 0))
        self.window.blit(backgrounds.BACKGROUND_GAME, (0, 30))
        self.clock.tick(config.FPS)

        self.txt_draw(self.player.health, 10, 1, 'Player', 'Health', config.HEALTH_FONT)
        self.txt_draw(self.level_manager.level, 400, 1, 'Level', '', config.HEALTH_FONT)

        if self.next_level_draw:
            self.draw_level()
            self.next_level_draw = False

        self.player.draw_on_screen(self.window)

        if self.level_manager.level == 5:
            self.txt_draw(self.level_manager.get_boss_hp, 700, 1, 'Boss', 'Health', config.HEALTH_FONT)

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive:
                enemy.draw_on_screen(self.window)

        pygame.display.update()

    def character_movement(self):
        keys_pressed = pygame.key.get_pressed()

        self.player.move(keys=keys_pressed)

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive:
                enemy.move(target=self.player.rect)

    def who_win(self):
        winner_text = ""
        if all(enemy.is_alive is False for enemy in self.level_manager.get_enemies()) and self.level_manager.level == 5:
            winner_text = 'You Win!'

        elif not self.player.is_alive:
            winner_text = 'You died'

        if winner_text != "":
            self.draw_winner(winner_text)
            self.stop = True

    def draw_winner(self, winner_text):
        draw_text = config.WINNER_FONT.render(winner_text, True, config.WHITE)
        self.window.blit(draw_text, (config.WIDTH / 2 - draw_text.get_width() / 2,
                                     config.HEIGHT / 2 - draw_text.get_height()))
        pygame.display.update()
        pygame.time.wait(2000)
        menu.menu_end(draw_text)

    def update_fight(self):
        self.character_movement()

        for enemy in self.level_manager.get_enemies():
            if enemy.is_alive:
                self.player.check_collision(enemy, Monster)
                self.player.handle_bullets(enemy=enemy, win=self.window)
                enemy.handle_monster_bullets(player=self.player, win=self.window)

        pygame.display.update()

    def new_game(self):
        self.level_manager.level = 0
        self.next_level_draw = True
        self.run = True
        self.player.reset()

        self.main()

    def next_level(self):

        if all(enemy.is_alive is False for enemy in self.level_manager.get_enemies()) or self.level_manager.level == 0:
            self.next_level_draw = True
            self.level_manager.go_to_next_level()
        else:
            return

    def main(self):
        self.player = Player(menu.character_update())

        while self.run:
            self.next_level()
            self.events()
            if not self.stop:
                self.update_fight()
                self.who_win()

            else:
                break
            self.draw()


game = Game()
menu = Menu(game)
menu.menu_screen()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
