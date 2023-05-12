import sys
from unittest.mock import patch
from pathlib import Path
import pytest

# Add the parent directory to the sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Import the required modules from the src package
from src.main import main


def test_main():
    """
    Test the main function that starts the game.
    """
    with patch('src.main.pygame.init') as mock_init, \
            patch('src.main.Menu') as mock_menu, \
            patch('src.main.Game') as mock_game, \
            patch('src.main.pygame.quit') as mock_quit, \
            patch('src.main.sys.exit') as mock_exit:

        mock_quit.side_effect = lambda: None  # Simulate only one call
        mock_exit.side_effect = lambda: None  # Simulate only one call

        main()

        mock_init.assert_called_once()
        mock_menu.assert_called_once()
        mock_game.assert_called_once()
        mock_quit.assert_called()
        mock_exit.assert_called()


def test_main_exception():
    """
    Test the main function when an exception occurs.
    """
    with patch('src.main.pygame.init'), \
            patch('src.main.Menu'), \
            patch('src.main.Game'), \
            patch('src.main.pygame.quit') as mock_quit, \
            patch('src.main.sys.exit') as mock_exit, \
            pytest.raises(Exception):

        main()

        mock_quit.assert_called_once()
        mock_exit.assert_called_once()
