from pathlib import Path
from unittest.mock import MagicMock, create_autospec
import sys


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.level_manager import LevelManager
from src.enemy import Boss


class TestLevelManager:
    """
    Unit tests for the LevelManager class.
    """

    def setup_method(self):
        """
        Setup method runs before each test.
        It initializes the instance of LevelManager.
        """
        self.level_manager = LevelManager()

    def test_get_enemies_for_stage(self):
        """
        Test that get_enemies_for_stage sets the correct level strategy and creates the enemies for each level.
        """
        for level in range(1, 6):
            self.level_manager.level = level
            self.level_manager.get_enemies_for_stage()
            assert self.level_manager.level_strategy is not None
            assert len(self.level_manager.enemies) > 0

    def test_all_enemies_defeated(self):
        """
        Test that all_enemies_defeated returns True only when all enemies are defeated.
        """
        mock_enemy = MagicMock()
        mock_enemy.is_alive = False
        self.level_manager.enemies = [mock_enemy]

        assert self.level_manager.all_enemies_defeated

        mock_enemy.is_alive = True
        assert not self.level_manager.all_enemies_defeated

    def test_get_boss_hp(self):
        """
        Test that get_boss_hp returns the correct health of the boss.
        """
        mock_boss = create_autospec(Boss, instance=True)
        mock_boss.is_alive = True
        mock_boss.health = 100

        self.level_manager.enemies = [mock_boss]

        assert self.level_manager.get_boss_hp == 100

    def test_go_to_next_level(self):
        """
        Test that go_to_next_level increments the level number and gets the enemies for the next level stage.
        """
        self.level_manager.level = 1
        self.level_manager.go_to_next_level()

        assert self.level_manager.level == 2
        assert len(self.level_manager.enemies) > 0
