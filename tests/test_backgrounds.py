from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.backgrounds import Backgrounds


@pytest.fixture
def backgrounds_instance():
    """
    Fixture: Initialize an instance of Backgrounds before each test.
    """
    return Backgrounds()


def test_singleton_instance(backgrounds_instance):
    """
    Test to check if the singleton works correctly.
    """
    backgrounds1 = backgrounds_instance
    backgrounds2 = backgrounds_instance
    assert backgrounds1 is backgrounds2


def test_init_backgrounds(backgrounds_instance):
    """
    Test to check the initialization of the backgrounds.
    """
    backgrounds_instance.init_backgrounds()
    assert backgrounds_instance.background_game is not None
    assert backgrounds_instance.background_stats is not None
    assert backgrounds_instance.background_menu is not None
    assert backgrounds_instance.logo is not None


def test_background_files_exist(backgrounds_instance):
    """
    Test to check if the background files exist.
    """
    backgrounds_instance = backgrounds_instance
    backgrounds_instance.init_backgrounds()

    base_dir = Path(__file__).resolve().parent.parent.parent
    background_game_file = base_dir / 'Game' / 'Assets' / 'background_game.png'
    background_stats_file = base_dir / 'Game' / 'Assets' / 'background_stats.png'
    background_menu_file = base_dir / 'Game' / 'Assets' / 'background_menu.png'
    logo_file = base_dir / 'Game' / 'Assets' / 'logo.png'

    assert background_game_file.exists()
    assert background_stats_file.exists()
    assert background_menu_file.exists()
    assert logo_file.exists()
