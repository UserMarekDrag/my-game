from abc import ABC, abstractmethod
from enemy import Bat, Mage, Boss


class LevelStrategy(ABC):
    @abstractmethod
    def create_enemies(self):
        """Abstract method to create enemies"""
        pass


class LevelOneStrategy(LevelStrategy):
    def create_enemies(self):
        """Method to create enemies for Level 1"""
        return [Bat(900, 30), Bat(900, 550)]


class LevelTwoStrategy(LevelStrategy):
    def create_enemies(self):
        """Method to create enemies for Level 2"""
        return [Bat(900, 30), Bat(900, 550), Bat(0, 30)]


class LevelThreeStrategy(LevelStrategy):
    def create_enemies(self):
        """Method to create enemies for Level 3"""
        return [Bat(900, 30), Bat(900, 550), Bat(0, 30), Mage(0, 250)]


class LevelFourStrategy(LevelStrategy):
    def create_enemies(self):
        """Method to create enemies for Level 4"""
        return [Bat(900, 30), Bat(900, 550), Bat(0, 30), Mage(0, 250), Mage(800, 50)]


class LevelFiveStrategy(LevelStrategy):
    def create_enemies(self):
        """Method to create enemies for Level 5"""
        return [Bat(900, 30), Bat(900, 550), Bat(0, 30), Mage(0, 250), Mage(800, 50), Boss()]
