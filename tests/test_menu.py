from pathlib import Path
from unittest.mock import Mock, patch
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.menu import Menu
from src.button import ButtonBuilder


class TestMenu:

    @pytest.fixture
    def mock_button(self):
        return Mock()

    @pytest.fixture
    def mock_button_builder(self, mock_button):
        mock = Mock(spec=ButtonBuilder)
        mock.set_position.return_value = mock
        mock.set_content.return_value = mock
        mock.set_action.return_value = mock
        mock.build.return_value = mock_button
        return mock

    @pytest.fixture
    def menu(self):
        return Menu()

    @patch('src.menu.ButtonBuilder')
    def test_create_buttons(self, mock_button_builder_class, menu, mock_button_builder, mock_button):
        """
        Test if create_buttons method properly creates buttons.
        """
        mock_button_builder_class.return_value = mock_button_builder
        menu.create_buttons()
        assert all(isinstance(button, Mock) for button in menu.buttons.values())

    def test_character_update(self, menu):
        """
        Test if character_update method returns the correct character.
        """
        assert menu.character_update() == menu.character_dictionary[menu.character_choice]

    def test_handle_button_click(self, menu, mock_button):
        """
        Test if handle_button_click method calls execute on button action if the button is pressed.
        """
        mock_button.is_pressed.return_value = True
        assert menu.handle_button_click(mock_button, (0, 0), (0, 0, 0)) == mock_button.action.execute.return_value
        mock_button.action.execute.assert_called_once()
