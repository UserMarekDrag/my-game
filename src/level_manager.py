from src.levels import LevelOneStrategy, LevelTwoStrategy, LevelThreeStrategy, LevelFourStrategy, LevelFiveStrategy
from src.enemy import Boss


class LevelManager:
    def __init__(self):
        self.level = 0
        self.level_strategy = None
        self.enemies = []

    def get_enemies_for_stage(self):
        """Get the enemies for the current level stage based on the level number."""
        if self.level == 1:
            self.level_strategy = LevelOneStrategy()
        elif self.level == 2:
            self.level_strategy = LevelTwoStrategy()
        elif self.level == 3:
            self.level_strategy = LevelThreeStrategy()
        elif self.level == 4:
            self.level_strategy = LevelFourStrategy()
        elif self.level == 5:
            self.level_strategy = LevelFiveStrategy()

        self.enemies = self.level_strategy.create_enemies()

    def get_enemies(self):
        """Get the list of enemies for the current level stage."""
        return self.enemies

    @property
    def get_boss_hp(self):
        """
        Get the current health of the boss enemy if it is still alive.
        """
        for enemy in self.enemies:
            if enemy.is_alive and isinstance(enemy, Boss):
                if enemy.health is None:
                    return
                return enemy.health

    @property
    def all_enemies_defeated(self):
        return all(enemy.is_alive is False for enemy in self.enemies)

    def go_to_next_level(self):
        """
        Increment the level number and get the enemies for the next level stage.
        """
        if self.level < 5:
            self.level += 1
        return self.get_enemies_for_stage()
