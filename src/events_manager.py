import pygame
from enemy import Mage, Boss
from monster import Monster


class EventsManager:
    """
    A class responsible for managing events in the game, such as handling user input and managing object interactions.
    """

    __shooting_enemies = (Mage, Boss)

    def __init__(self, window):
        self.window = window
        self.run = True

    def events(self, level_manager, player):
        """
        Process all game events, such as moving characters and handling collisions.
        """
        self.handle_enemy_shooting(level_manager, player)
        self.handle_enemy_moving(level_manager, player)
        self.handle_player_moving(player)
        self.handle_collision(level_manager, player)
        self.handle_fighting(level_manager, player)

        pygame.display.update()

    def handle_user_input(self, player):
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                player.shoot(event)

    def get_alive_enemies(self, level_manager):
        """
        Get a list of all alive enemies.
        """
        return [enemy for enemy in level_manager.get_enemies() if enemy.is_alive]

    def handle_enemy_shooting(self, level_manager, player):
        """
        Handle enemy shooting events.
        """
        for enemy in self.get_alive_enemies(level_manager):
            if isinstance(enemy, self.__shooting_enemies):
                enemy.shoot(player)

    def handle_enemy_moving(self, level_manager, player):
        """
        Handle enemy movement events.
        """
        for enemy in self.get_alive_enemies(level_manager):
            enemy.move(target=player.rect)

    def handle_player_moving(self, player):
        """
        Handle player movement events based on key presses.
        """
        keys_pressed = pygame.key.get_pressed()
        player.move(keys=keys_pressed)

    def handle_fighting(self, level_manager, player):
        """
        Handle fighting events between the player and enemies.
        """
        for enemy in self.get_alive_enemies(level_manager):
            player.handle_bullets(enemy=enemy, win=self.window)
            enemy.handle_monster_bullets(player=player, win=self.window)

    def handle_collision(self, level_manager, player):
        """
        Handle collision events between the player and enemies.
        """
        for enemy in self.get_alive_enemies(level_manager):
            player.check_collision(enemy, Monster)
