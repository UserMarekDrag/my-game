import sys
import pygame
from config import Config
from player import Player
from monster import Monster
from enemy import Bat, Mage, Boss
from backgrounds import Backgrounds
from menu import Menu

backgrounds = Backgrounds()
config = Config()

pygame.display.set_caption(config.GAME_NAME)


class Game:

    __shooting_enemies = (Mage, Boss)

    def __init__(self):
        self.win = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.stop = False
        self.stage = 0
        self.next_stage_draw = True

        self.player = Player(config.MALE_CHARACTER)

        self.bat_1 = Bat(500, 130)
        self.bat_2 = Bat(900, 550)
        self.bat_3 = Bat(0, 30)

        self.mage_1 = Mage(0, 250)
        self.mage_2 = Mage(800, 50)

        self.boss = Boss()

        self.enemies = set()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.player.shoot(event)

            for enemy in self.enemies:
                if enemy.is_alive and isinstance(enemy, self.__shooting_enemies):
                    enemy.shoot(self.player)

    def txt_draw(self, health, width, height, name, health_txt, font):
        text = font.render(
            f"{str(name)} {str(health_txt)}: " + str(health), True, config.BLUE)

        self.win.blit(text, (width, height))

    def draw_stage(self):
        self.txt_draw(self.stage, config.WIDTH / 2 - 200, config.HEIGHT / 2 - 150, 'Stage', '', config.STAGE_NUMB_FONT)

        pygame.display.update()
        pygame.time.wait(1000)

    def draw(self):
        self.win.blit(backgrounds.BACKGROUND_STATS, (0, 0))
        self.win.blit(backgrounds.BACKGROUND_GAME, (0, 30))
        self.clock.tick(config.FPS)

        self.txt_draw(self.player.health, 10, 1, 'Player', 'Health', config.HEALTH_FONT)
        self.txt_draw(self.stage, 400, 1, 'Stage', '', config.HEALTH_FONT)

        if self.next_stage_draw:
            self.draw_stage()
            self.next_stage_draw = False

        self.player.draw_on_screen(self.win)

        if self.stage == 5:
            self.txt_draw(self.boss.health, 700, 1, 'Boss', 'Health', config.HEALTH_FONT)

        for enemy in self.enemies:
            if enemy.is_alive:
                enemy.draw_on_screen(self.win)

        pygame.display.update()

    def character_movement(self):
        keys_pressed = pygame.key.get_pressed()

        self.player.move(keys=keys_pressed)

        for enemy in self.enemies:
            if enemy.is_alive:
                enemy.move(target=self.player.rect)

    def health_count(self):
        winner_text = ""
        if not self.boss.is_alive and self.stage == 5:
            winner_text = 'You Win!'

        elif not self.player.is_alive:
            winner_text = 'You died'

        if winner_text != "":
            self.draw_winner(winner_text)
            self.stop = True

    def draw_winner(self, winner_text):
        draw_text = config.WINNER_FONT.render(winner_text, True, config.WHITE)
        self.win.blit(draw_text, (config.WIDTH / 2 - draw_text.get_width() / 2,
                                  config.HEIGHT / 2 - draw_text.get_height()))
        pygame.display.update()
        pygame.time.wait(2000)
        menu.menu_end(draw_text)

    def update_fight(self):
        self.character_movement()

        for enemy in self.enemies:
            if enemy.is_alive:
                self.player.check_collision(enemy, Monster)
                self.player.handle_bullets(enemy=enemy, win=self.win)
                enemy.handle_monster_bullets(player=self.player, win=self.win)

        pygame.display.update()

    def new_game(self):
        self.stage = 0
        self.run = True

        self.enemies = set()

        self.player.reset()

        self.bat_1.reset(900, 30)
        self.bat_2.reset(900, 550)
        self.bat_3.reset(0, 30)

        self.mage_1.reset(0, 250)
        self.mage_2.reset(800, 50)

        self.boss.reset()

        self.main()

    def next_stage_values(self):

        self.next_stage_draw = True

        if self.stage >= 0:
            self.enemies.add(self.bat_1)

            self.bat_1.reset(900, 30)

        if self.stage >= 1:
            self.enemies.add(self.bat_1)
            self.enemies.add(self.bat_2)

            self.bat_1.reset(900, 30)
            self.bat_2.reset(900, 550)

        if self.stage >= 2:
            self.enemies.add(self.bat_3)

            self.bat_3.reset(0, 30)

        if self.stage >= 3:
            self.enemies.add(self.mage_1)

            self.mage_1.reset(0, 250)

        if self.stage >= 4:
            self.enemies.add(self.mage_2)

            self.mage_2.reset(800, 50)

        if self.stage == 5:
            self.enemies.add(self.boss)

            self.boss.reset()

    def next_stage(self):

        if all(enemy.is_alive is False for enemy in self.enemies):
            if self.stage < 5:
                self.stage += 1
            self.next_stage_values()
        return self.stage

    def main(self):
        self.player = Player(menu.character_update())

        while self.run:
            self.stage = self.next_stage()
            self.events()
            if not self.stop:
                self.update_fight()
                self.health_count()
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
