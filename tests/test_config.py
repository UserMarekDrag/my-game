from pathlib import Path
import sys
import pygame
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.config import Config


@pytest.fixture
def config_instance():
    """
    Fixture: Initialize an instance of Config before each test.
    """
    return Config()


def test_singleton_instance(config_instance):
    """
    Test to check if the singleton works correctly.
    """
    config1 = config_instance
    config2 = config_instance
    assert config1 is config2


def test_config_values(config_instance):
    """
    Test to check the values of the configuration.
    """
    assert isinstance(config_instance.GAME_NAME, str)
    assert isinstance(config_instance.WIDTH, int)
    assert isinstance(config_instance.HEIGHT, int)
    assert isinstance(config_instance.FPS, int)


def test_color_values(config_instance):
    """
    Test to check the color values in the configuration.
    """
    assert isinstance(config_instance.WHITE, tuple)
    assert isinstance(config_instance.BLACK, tuple)
    assert isinstance(config_instance.RED, tuple)
    assert isinstance(config_instance.YELLOW, tuple)


def test_font_values(config_instance):
    """
    Test to check the font values in the configuration.
    """
    assert isinstance(config_instance.HEALTH_FONT, pygame.font.Font)
    assert isinstance(config_instance.WINNER_FONT, pygame.font.Font)
    assert isinstance(config_instance.LEVEL_NUMB_FONT, pygame.font.Font)


def test_constant_values(config_instance):
    """
    Test to check the constant values in the configuration.
    """
    assert isinstance(config_instance.PLAYER_HEALTH, int)
    assert isinstance(config_instance.BOSS_HEALTH, int)
    assert isinstance(config_instance.BAT_HEALTH, int)
    assert isinstance(config_instance.MAGE_HEALTH, int)
    assert isinstance(config_instance.PLAYER_MAX_BULLETS, int)
    assert isinstance(config_instance.BOSS_MAX_BULLETS, int)
    assert isinstance(config_instance.MAGE_MAX_BULLETS, int)
    assert isinstance(config_instance.BUTTON_WIDTH, int)
    assert isinstance(config_instance.BUTTON_HEIGHT, int)
    assert isinstance(config_instance.FONT_SIZE, int)
    assert isinstance(config_instance.BUTTON_POSITION_WIDTH_ON_SCREEN, float)
    assert isinstance(config_instance.BUTTON_POSITION_HEIGHT_ON_SCREEN, int)
