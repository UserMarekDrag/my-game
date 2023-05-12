from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.levels import LevelOneStrategy, LevelTwoStrategy, LevelThreeStrategy, LevelFourStrategy, LevelFiveStrategy
from src.enemy import Bat, Mage, Boss


class TestLevels:
    """
    Unit tests for the LevelStrategy subclasses.
    """

    def setup_method(self):
        """
        Setup method runs before each test.
        It initializes the instances of different level strategies.
        """
        self.level_one = LevelOneStrategy()
        self.level_two = LevelTwoStrategy()
        self.level_three = LevelThreeStrategy()
        self.level_four = LevelFourStrategy()
        self.level_five = LevelFiveStrategy()

    def test_level_one_strategy(self):
        """
        Test that LevelOneStrategy creates the correct enemies.
        """
        enemies = self.level_one.create_enemies()
        assert len(enemies) == 2
        assert all(isinstance(enemy, Bat) for enemy in enemies)

    def test_level_two_strategy(self):
        """
        Test that LevelTwoStrategy creates the correct enemies.
        """
        enemies = self.level_two.create_enemies()
        assert len(enemies) == 3
        assert all(isinstance(enemy, Bat) for enemy in enemies)

    def test_level_three_strategy(self):
        """
        Test that LevelThreeStrategy creates the correct enemies.
        """
        enemies = self.level_three.create_enemies()
        assert len(enemies) == 4
        assert all(isinstance(enemy, Bat) or isinstance(enemy, Mage) for enemy in enemies)

    def test_level_four_strategy(self):
        """
        Test that LevelFourStrategy creates the correct enemies.
        """
        enemies = self.level_four.create_enemies()
        assert len(enemies) == 5
        assert all(isinstance(enemy, Bat) or isinstance(enemy, Mage) for enemy in enemies)

    def test_level_five_strategy(self):
        """
        Test that LevelFiveStrategy creates the correct enemies.
        """
        enemies = self.level_five.create_enemies()
        assert len(enemies) == 6
        assert all(isinstance(enemy, Bat) or isinstance(enemy, Mage) or isinstance(enemy, Boss) for enemy in enemies)
