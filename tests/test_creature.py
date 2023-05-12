from pathlib import Path
import sys
from unittest.mock import patch, PropertyMock
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.creature import Creature, Config


class ConcreteCreature(Creature):
    def move(self, keys=None, target=None):
        pass

    def reset(self, position_x, position_y):
        pass


@pytest.fixture
def creature():
    """
    Creates a Creature instance with predefined values for testing.
    """
    return ConcreteCreature("TestCreature", "test_image.png", 100, 100, 50, 50, 100)


def test_creature_init(creature):
    """
    Test the initialization of the Creature class.
    """
    assert creature.name == "TestCreature"
    assert creature.image_name == "test_image.png"
    assert creature.width == 50
    assert creature.height == 50
    assert creature.health == 100
    assert creature.rect.x == 100
    assert creature.rect.y == 100
    assert creature.is_alive


@patch('pygame.Surface')
def test_creature_draw_on_screen(mock_surface, creature):
    """
    Test the draw_on_screen method of the Creature class.
    """
    creature.draw_on_screen(mock_surface)
    mock_surface.blit.assert_called_once_with(creature.CREATURE, (creature.rect.x, creature.rect.y))


@patch.object(Config, 'DAMAGE', new_callable=PropertyMock, return_value=10)
def test_creature_take_damage(mock_damage, creature):
    """
    Test the take_damage method of the Creature class.
    """
    initial_health = creature.health
    creature.take_damage()
    assert creature.health == initial_health - mock_damage.return_value

    creature.health = mock_damage.return_value
    creature.take_damage()
    assert creature.health == 0
    assert not creature.is_alive
