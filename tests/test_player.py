from pathlib import Path
import sys
from unittest.mock import Mock, patch, PropertyMock
import pytest
from pygame import K_x, K_LEFT, K_DOWN, K_UP, K_RIGHT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.player import Player
from src.config import Config


@pytest.fixture
def player():
    """
    Creates a Player instance with a test image for testing.
    """
    return Player("test_image.png")


def test_player_init(player):
    """
    Test the initialization of the Player class.
    """
    assert player.name == "Hero"
    assert player.image_name == "test_image.png"
    assert player.width == 40
    assert player.height == 80
    assert player.health == Config.PLAYER_HEALTH
    assert player.is_alive
    assert player.rect.x == 350
    assert player.rect.y == 150
    assert player.bullets == []


def test_player_reset(player):
    """
    Test the reset method of the Player class.
    """
    player.health = 0
    player.is_alive = False
    player.bullets = ["test"]
    player.reset(400, 200)
    assert player.health == Config.PLAYER_HEALTH
    assert player.is_alive
    assert player.rect.x == 400
    assert player.rect.y == 200
    assert player.bullets == []


@patch('src.config.Config.PLAYER_MAX_BULLETS', new_callable=PropertyMock, return_value=1)
def test_player_shoot(mock_max_bullets, player):
    """
    Test the shoot method of the Player class.
    """
    mock_event = Mock()
    mock_event.key = K_x
    player.bullets = ["test"]
    player.shoot(mock_event)
    assert len(player.bullets) == mock_max_bullets.return_value


@patch('src.config.Config.VEL_PLAYER', new_callable=PropertyMock, return_value=10)
def test_player_move(mock_vel_player, player):
    """
    Test the move method of the Player class.
    """
    player.rect.x = 100
    player.rect.y = 100
    keys = {K_LEFT: True, K_RIGHT: False, K_UP: False, K_DOWN: False}  # Initialize all keys as False
    player.move(keys)
    assert player.rect.x == 100 - mock_vel_player.return_value
