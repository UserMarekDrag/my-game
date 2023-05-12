from pathlib import Path
from unittest.mock import Mock, patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.display_text import DisplayText
from src.config import Config


class TestDisplayText:
    """
    Unit tests for the DisplayText class.
    """

    def setup_method(self):
        """
        Setup method runs before each test.
        It initializes a display text instance with a mock window.
        """
        self.mock_window = Mock()
        self.display_text = DisplayText(self.mock_window)

    @patch.object(Config, 'BLUE', 'BLUE')
    def test_txt_draw(self):
        """
        Test that txt_draw renders the text and calls display_text with the correct arguments.
        """
        mock_font = Mock()
        number = 10
        width = 50
        height = 100
        name = "Player"
        content = "Health"

        with patch.object(mock_font, 'render', return_value='Rendered Text') as mocked_render:
            self.display_text.txt_draw(number, width, height, name, content, mock_font)
            mocked_render.assert_called_once_with(f"{name} {content}: {number}", True, Config.BLUE)

        self.mock_window.blit.assert_called_once_with('Rendered Text', (width, height))

    def test_display_text(self):
        """
        Test that display_text draws the text on the window at the correct position.
        """
        self.display_text.text = 'Rendered Text'
        width = 50
        height = 100

        self.display_text.display_text(width, height)

        self.mock_window.blit.assert_called_once_with('Rendered Text', (width, height))
