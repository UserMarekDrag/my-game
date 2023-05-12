from pathlib import Path
import sys
from unittest.mock import Mock, patch, PropertyMock
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.monster import Monster


@pytest.fixture
def monster():
    """
    Creates a Monster instance for testing.
    """
    return Monster("test_image.png", 100, 100, 50, 50, 5)


def test_monster_init(monster):
    """
    Test the initialization of the Monster class.
    """
    assert monster.name == "Monster"
    assert monster.image_name == "test_image.png"
    assert monster.width == 50
    assert monster.height == 50
    assert monster.health == 5
    assert monster.is_alive
    assert monster.rect.x == 100
    assert monster.rect.y == 100
    assert monster.monster_bullets == []


@patch('src.config.Config.BOSS_MAX_BULLETS', new_callable=PropertyMock, return_value=1)
def test_monster_shoot(mock_max_bullets, monster):
    """
    Test the shoot method of the Monster class.
    """
    mock_player = Mock()
    mock_player.rect.x = 50
    monster.monster_bullets = ["test"]
    monster.shoot(mock_player)
    assert len(monster.monster_bullets) == mock_max_bullets.return_value


def test_check_direction(monster):
    """
    Test the check_direction method of the Monster class.
    """
    mock_player = Mock()
    mock_player.rect.x = 50
    assert monster.check_direction(mock_player) == -1
    mock_player.rect.x = 150
    assert monster.check_direction(mock_player) == 1
