import pygame
import sys
from game import Game
from menu import Menu


def main():
    try:
        pygame.init()

        menu = Menu()
        game = Game(menu)
        menu.game = game
        menu.menu_screen()
        game.main()

        pygame.quit()
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
