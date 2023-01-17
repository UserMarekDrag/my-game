import sys
import pygame
from config import *
from sounds import *
from player import *
from monsters import *
from animation import *
from map import *


pygame.display.set_caption(GAME_NAME)


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Hero()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw(self, player):
        self.win.blit(BACKGROUND, (0, 0))
        self.clock.tick(FPS)

        self.win.blit(self.player.CREATURE, (player.x, player.y))

        pygame.display.update()

    def movement(self, player):

        keys_pressed = pygame.key.get_pressed()
        self.player.static_handle_movement(keys_pressed, player)

    def main(self):
        player = self.player.rect
        while self.run:
            self.events()
            self.movement(player)
            self.draw(player)


game = Game()
if __name__ == '__main__':
    game.main()

pygame.quit()
sys.exit()
