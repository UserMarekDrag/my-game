"""
Main module - entry point for the game.
"""

import sys

import pygame

from src.game import Game
from src.menu import Menu


def main():
    """
    Main function that starts the game.
    """
    try:
        pygame.init()

        menu = Menu()
        game = Game(menu)
        menu.game = game
        menu.menu_screen()
        game.main()

        pygame.quit()
        sys.exit()
    except Exception as error:
        print(f"An error occurred: {error}")

    finally:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
