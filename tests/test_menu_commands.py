from pathlib import Path
from unittest.mock import Mock, patch
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.menu_commands import (StartGameCommand, RestartGameCommand, OptionsCommand,
                               QuitGameCommand, ChooseMaleCharacterCommand, ChooseFemaleCharacterCommand)


class TestMenuCommands:

    @pytest.fixture
    def mock_menu(self):
        return Mock()

    def test_start_game_command(self, mock_menu):
        """
        Test if StartGameCommand execute method returns False.
        """
        start_game_command = StartGameCommand(mock_menu)
        assert not start_game_command.execute()

    def test_restart_game_command(self, mock_menu):
        """
        Test if RestartGameCommand execute method calls new_game on menu's game.
        """
        restart_game_command = RestartGameCommand(mock_menu)
        restart_game_command.execute()
        mock_menu.game.new_game.assert_called_once()

    @patch('pygame.display.update')
    @patch('pygame.time.wait')
    def test_options_command(self, mock_wait, mock_update, mock_menu):
        """
        Test if OptionsCommand execute method calls appropriate pygame methods and menu's menu_choice_char method.
        """
        options_command = OptionsCommand(mock_menu)
        assert options_command.execute() == mock_menu.menu_choice_char()
        mock_menu.game.window.blit.assert_called_once()
        mock_update.assert_called_once()
        mock_wait.assert_called_once_with(100)

    @patch('pygame.quit')
    @patch('sys.exit')
    def test_quit_game_command(self, mock_exit, mock_quit, mock_menu):
        """
        Test if QuitGameCommand execute method properly quits the game.
        """
        quit_game_command = QuitGameCommand(mock_menu)
        quit_game_command.execute()
        assert not mock_menu.game.run
        mock_quit.assert_called_once()
        mock_exit.assert_called_once()

    def test_choose_male_character_command(self, mock_menu):
        """
        Test if ChooseMaleCharacterCommand execute method properly updates character_choice to "male".
        """
        choose_male_character_command = ChooseMaleCharacterCommand(mock_menu)
        assert not choose_male_character_command.execute()
        assert mock_menu.character_choice == "male"
        mock_menu.character_update.assert_called_once()

    def test_choose_female_character_command(self, mock_menu):
        """
        Test if ChooseFemaleCharacterCommand execute method properly updates character_choice to "female".
        """
        choose_female_character_command = ChooseFemaleCharacterCommand(mock_menu)
        assert not choose_female_character_command.execute()
        assert mock_menu.character_choice == "female"
        mock_menu.character_update.assert_called_once()
