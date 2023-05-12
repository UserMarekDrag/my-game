from pathlib import Path
from unittest.mock import Mock, patch
import sys
import pytest
import pygame

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.events_manager import EventsManager


class TestEventsManager:

    @pytest.fixture
    def mock_window(self):
        return Mock()

    @pytest.fixture
    def events_manager(self, mock_window):
        return EventsManager(mock_window)

    @pytest.fixture
    def mock_level_manager(self):
        return Mock()

    @pytest.fixture
    def mock_player(self):
        return Mock()

    def test_handle_user_input_quit(self, events_manager, mock_player):
        """
        Test if handle_user_input correctly handles QUIT event.
        """
        mock_event = Mock(type=pygame.QUIT)
        with patch('pygame.event.get', return_value=[mock_event]):
            events_manager.handle_user_input(mock_player)
            assert not events_manager.run

    def test_handle_user_input_keydown(self, events_manager, mock_player):
        """
        Test if handle_user_input correctly handles KEYDOWN event.
        """
        mock_event = Mock(type=pygame.KEYDOWN)
        with patch('pygame.event.get', return_value=[mock_event]):
            events_manager.handle_user_input(mock_player)
            mock_player.shoot.assert_called_once_with(mock_event)

    def test_get_alive_enemies(self, events_manager, mock_level_manager):
        """
        Test if get_alive_enemies returns the correct list of enemies.
        """
        mock_enemy_1 = Mock(is_alive=True)
        mock_enemy_2 = Mock(is_alive=False)
        mock_enemy_3 = Mock(is_alive=True)
        mock_level_manager.get_enemies.return_value = [mock_enemy_1, mock_enemy_2, mock_enemy_3]
        assert events_manager.get_alive_enemies(mock_level_manager) == [mock_enemy_1, mock_enemy_3]
