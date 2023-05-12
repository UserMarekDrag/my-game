from pathlib import Path
from unittest.mock import Mock
import sys

import pygame
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.bullet import Bullet


@pytest.fixture
def bullet_instance():
    """
    Creates a Bullet instance with predefined values for testing.
    """
    direction = 1
    x = 50
    y = 50
    bullet_vel = 5
    color = (255, 255, 255)
    return Bullet(direction, x, y, bullet_vel, color)


def test_bullet_init(bullet_instance):
    """
    Test the initialization of the Bullet class.
    """
    assert bullet_instance.direction == 1
    assert bullet_instance.bullet_vel == 5
    assert bullet_instance.color == (255, 255, 255)
    assert bullet_instance.bullet.x == 50
    assert bullet_instance.bullet.y == 50


def test_bullet_draw(mocker, bullet_instance):
    """
    Test the draw method of the Bullet class.
    """
    mock_surface = pygame.Surface((100, 100))  # create a real pygame.Surface instance
    mocker.patch('pygame.draw.rect')  # mock the pygame.draw.rect function

    bullet_instance.draw(mock_surface)

    pygame.draw.rect.assert_called_once_with(mock_surface, bullet_instance.color, bullet_instance.bullet)


def test_bullet_out_of_screen(bullet_instance):
    """
    Test the is_out_of_screen method of the Bullet class.
    """
    bullet_instance.bullet.x = 1500
    assert bullet_instance.is_out_of_screen() is True

    bullet_instance.bullet.x = 500
    assert bullet_instance.is_out_of_screen() is False


def test_bullet_collides_with(mocker, bullet_instance):
    """
    Test the collides_with method of the Bullet class.
    """
    mock_enemy = Mock()  # Mock Enemy object for testing
    mock_rect = mocker.patch('pygame.Rect', autospec=True)
    bullet_instance.bullet = mock_rect

    mock_rect.colliderect.return_value = True
    assert bullet_instance.collides_with(mock_enemy) is True

    mock_rect.colliderect.return_value = False
    assert bullet_instance.collides_with(mock_enemy) is False


def test_bullet_check_collision(bullet_instance):
    """
    Test the check_collision method of the Bullet class.
    """
    mock_other = Mock(is_alive=True)  # Mock Collidable object for testing
    bullet_instance.colliderect = Mock(return_value=True)
    assert bullet_instance.check_collision(mock_other, 'enemy') is True

    mock_other.is_alive = False
    assert bullet_instance.check_collision(mock_other, 'enemy') is False


def test_bullet_update(bullet_instance):
    """
    Test the update method of the Bullet class.
    """
    bullet_instance.update()
    assert bullet_instance.bullet.x == 55  # x was 50, direction was 1 and bullet_vel was 5
