from pathlib import Path
import sys
from unittest.mock import Mock, patch

import pygame

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.display_manager import DisplayManager
from src.display_text import DisplayText


@patch('pygame.display.update')
@patch('pygame.time.wait')
@patch('src.display_manager.backgrounds')
@patch('src.display_manager.config')
class TestDisplayManager:
    """
    Unit tests for the DisplayManager class
    """

    def setup_method(self):
        """
        Setup method runs before each test method.
        It initializes a display manager instance with a mock window.
        """
        self.mock_window = Mock(spec=pygame.Surface)
        self.mock_display_text = Mock(spec=DisplayText)
        with patch('src.display_manager.DisplayText', return_value=self.mock_display_text):
            self.display_manager = DisplayManager(self.mock_window)

    def test_clear_screen(self, mock_config, mock_backgrounds, mock_wait, mock_update):
        """
        Test that clear_screen calls the fill method on the window with black color
        """
        self.display_manager.clear_screen()
        self.mock_window.fill.assert_called_once_with((0, 0, 0))

    def test_draw_background(self, mock_config, mock_backgrounds, mock_wait, mock_update):
        """
        Test that draw_background blits the background image on the window
        """
        self.display_manager.draw_background()
        assert self.mock_window.blit.call_count == 2

    def test_draw_characters(self, mock_config, mock_backgrounds, mock_wait, mock_update):
        """
        Test that draw_characters draws the player and all living enemies on the screen
        """
        mock_player = Mock()
        mock_enemies = [Mock(is_alive=True), Mock(is_alive=False)]
        self.display_manager.draw_characters(mock_player, mock_enemies)
        mock_player.draw_on_screen.assert_called_once_with(self.mock_window)
        mock_enemies[0].draw_on_screen.assert_called_once_with(self.mock_window)
        mock_enemies[1].draw_on_screen.assert_not_called()

    def test_draw_winner(self, mock_config, mock_backgrounds, mock_wait, mock_update):
        """
        Test that draw_winner draws the winner's text in the center of the screen
        """
        winner_text = 'You win!'
        mock_config.WINNER_FONT.render.return_value = Mock(get_width=Mock(return_value=20), get_height=Mock(return_value=10))
        mock_config.WIDTH = 100
        mock_config.HEIGHT = 100
        self.display_manager.draw_winner(winner_text)
        self.mock_window.blit.assert_called_once()
        assert mock_config.WINNER_FONT.render.call_args[0][0] == winner_text
        mock_update.assert_called_once()
        mock_wait.assert_called_once_with(2000)

    def test_draw_level(self, mock_config, mock_backgrounds, mock_wait, mock_update):
        """
        Test that draw_level displays the current level number
        """
        mock_level_manager = Mock(level=1)
        self.display_manager.draw_level(mock_level_manager)
        self.mock_display_text.txt_draw.assert_called_once_with(
            mock_level_manager.level,
            mock_config.WIDTH / 2 - 200,
            mock_config.HEIGHT / 2 - 150,
            'Level',
            '',
            mock_config.LEVEL_NUMB_FONT
        )
        assert mock_update.call_count == 2
        mock_wait.assert_called_once_with(1000)
