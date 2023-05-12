from pathlib import Path
import sys
from unittest.mock import Mock, patch
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.game import Game
from src.display_manager import DisplayManager
from src.events_manager import EventsManager
from src.level_manager import LevelManager


@pytest.fixture
def mock_menu():
    return Mock()


@pytest.fixture
def mock_game():
    """
    Mock the Game class and its dependencies.
    """
    game = Game(Mock())
    game.window = Mock()
    game.display_manager = Mock()
    game.events_manager = Mock()
    game.clock = Mock()
    game.player = Mock()
    game.level_manager = Mock()
    game.menu = Mock()
    return game


@patch('pygame.display.set_mode', return_value=Mock())
@patch('pygame.time.Clock', return_value=Mock())
def test_init(mock_set_mode, mock_menu):
    """
    Test the initialization of the Game class.
    """
    menu_mock = Mock()
    game = Game(menu_mock)
    assert mock_set_mode.call_count == 2
    assert game.menu == menu_mock
    assert game.window is not None
    assert isinstance(game.display_manager, DisplayManager)
    assert isinstance(game.events_manager, EventsManager)
    assert isinstance(game.clock, Mock)
    assert game.run
    assert not game.stop
    assert game.player is None
    assert isinstance(game.level_manager, LevelManager)


def test_check_winner_no_winner(mock_game):
    """
    Test check_winner when no conditions for winning or losing have been met.
    """
    mock_game.player = Mock(is_alive=True)
    mock_game.level_manager.all_enemies_defeated = False
    mock_game.level_manager.level = 0
    assert mock_game.check_winner() is None


def test_check_winner_player_wins(mock_game):
    """
    Test check_winner when the player has defeated all enemies and reached level 5.
    """
    mock_game.player = Mock(is_alive=True)
    mock_game.level_manager.all_enemies_defeated = True
    mock_game.level_manager.level = 5
    assert mock_game.check_winner() == 'You Win!'


def test_check_winner_player_dies(mock_game):
    """
    Test check_winner when the player's character dies.
    """
    mock_game.player = Mock(is_alive=False)
    assert mock_game.check_winner() == 'You died'


def test_new_game(mock_game):
    """
    Test the new_game function to ensure the level is reset and the game is running.
    """
    mock_game.main = Mock()
    mock_game.player = Mock()
    mock_game.new_game()
    assert mock_game.level_manager.level == 0
    assert mock_game.level_manager.enemies == []
    assert mock_game.player.reset.called
    assert mock_game.run


def test_next_level_no_enemies(mock_game):
    """
    Test next_level function when there are no enemies left to defeat.
    """
    mock_game.level_manager.get_enemies = Mock(return_value=[])
    mock_game.next_level()
    assert mock_game.level_manager.go_to_next_level.called
    assert mock_game.display_manager.draw_level.called


def test_next_level_with_enemies(mock_game):
    """
    Test next_level function when there are still enemies left to defeat.
    """
    mock_enemy = Mock(is_alive=True)
    mock_game.level_manager.get_enemies = Mock(return_value=[mock_enemy])
    mock_game.level_manager.go_to_next_level = Mock()
    mock_game.display_manager.draw_level = Mock()
    mock_game.next_level()
    mock_game.level_manager.go_to_next_level.assert_not_called()
    mock_game.display_manager.draw_level.assert_not_called()


@pytest.mark.parametrize('run, stop, winner_text', [
    (False, False, None),
])
@patch('pygame.display.set_mode')
def test_main(mock_game, run, stop, winner_text):
    """
    Test the main function and its conditions for stopping the game loop.
    """
    mock_game.run = run
    mock_game.stop = stop
    mock_game.who_win = Mock(return_value=winner_text)
    mock_game.player = Mock()
    mock_game.menu.character_update = Mock(return_value='male_player.PNG')  # return a valid value
    mock_game.next_level = Mock()
    mock_game.events_manager.handle_user_input = Mock()
    mock_game.events_manager.events = Mock()
    mock_game.display_manager.draw = Mock()

    # Add the code to set all enemies as defeated
    mock_enemies = []
    mock_game.level_manager.get_enemies = Mock(return_value=mock_enemies)

    mock_game.main()

    if run:
        mock_game.next_level.assert_called_once()

        mock_game.events_manager.handle_user_input.assert_called_once_with(mock_game.player)
        if not stop:
            mock_game.events_manager.events.assert_called_once_with(mock_game.level_manager, mock_game.player)
            mock_game.who_win.assert_called_once()
        else:
            mock_game.who_win.assert_not_called()
        mock_game.display_manager.draw.assert_called_once_with(mock_game.player, mock_game.level_manager)

    else:
        mock_game.next_level.assert_not_called()
