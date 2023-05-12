from pathlib import Path
import sys
from unittest.mock import MagicMock
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.enemy import Bat, Mage, Boss
from src.config import Config


config = Config()


@pytest.fixture
def bat():
    """Fixture to create and return a Bat instance for each test"""
    return Bat(100, 200)


def test_bat_initialization(bat):
    """
    Test the initialization of the Bat class.
    """

    assert bat.first_position_x == 100
    assert bat.first_position_y == 200
    assert bat.size_width == 80
    assert bat.size_height == 60
    assert bat.image_name == config.BAT_IMAGE
    assert bat.health == config.BAT_HEALTH
    assert bat.is_alive
    assert not bat.monster_bullets


def test_bat_reset(bat):
    """
    Test the reset method of the Bat class.
    """
    bat.reset(150, 250)

    assert bat.rect.x == 150
    assert bat.rect.y == 250
    assert bat.health == config.BAT_HEALTH
    assert bat.is_alive


def test_bat_move(bat):
    """
    Test the move method of the Bat class.
    """
    target = MagicMock()
    target.x = 150
    target.y = 250

    bat.move(target=target)

    assert bat.rect.x == 100 + config.VEL_BAT
    assert bat.rect.y == 200 + config.VEL_BAT


def test_bat_shoot(bat):
    """
    Test the shoot method of the Bat class.
    """
    player = MagicMock()

    bat.shoot(player)

    assert not bat.monster_bullets


def test_bat_handle_monster_bullets(bat):
    """
    Test the handle_monster_bullets method of the Bat class.
    """
    player = MagicMock()
    win = MagicMock()

    bat.handle_monster_bullets(player, win)

    assert not bat.monster_bullets


@pytest.fixture
def mage():
    """Fixture to create and return a Mage instance for each test"""
    return Mage(100, 200)


def test_mage_init(mage):
    """
    Test the initialization of the Mage class.
    """

    assert mage.first_position_x == 100
    assert mage.first_position_y == 200
    assert mage.size_width == 60
    assert mage.size_height == 100
    assert mage.health == config.MAGE_HEALTH
    assert mage.is_alive


def test_mage_reset(mage):
    """
    Test the reset method of the Mage class.
    """

    # Change the state of the mage
    mage.rect.x = 150
    mage.rect.y = 250
    mage.health = 0
    mage.is_alive = False

    mage.reset(100, 200)

    assert mage.rect.x == 100
    assert mage.rect.y == 200
    assert mage.health == config.MAGE_HEALTH
    assert mage.is_alive
    assert not mage.monster_bullets


def test_mage_move(mage):
    """
    Test the move method of the Mage class.
    """
    target = MagicMock()

    original_x = mage.rect.x
    original_y = mage.rect.y

    mage.move(target=target)

    assert mage.rect.x == original_x
    assert mage.rect.y == original_y


@pytest.fixture
def boss():
    """Fixture to create and return a Boss instance for each test"""
    return Boss()


def test_boss_init():
    """
    Test the initialization of the Boss class.
    """
    boss = Boss()

    assert boss.first_position_x == 900
    assert boss.first_position_y == 150
    assert boss.size_width == 60
    assert boss.size_height == 100
    assert boss.health == config.BOSS_HEALTH
    assert boss.position == 'center'
    assert boss.time_break == True
    assert boss.time_step == 50
    assert boss.is_alive


def test_boss_reset(boss):
    """
    Test the reset method of the Boss class.
    """

    # Change the state of the boss
    boss.rect.x = 950
    boss.rect.y = 200
    boss.health = 0
    boss.is_alive = False
    boss.position = 'left_down'
    boss.time_break = False
    boss.time_step = 0

    boss.reset()

    assert boss.rect.x == 900
    assert boss.rect.y == 150
    assert boss.health == config.BOSS_HEALTH
    assert boss.is_alive
    assert not boss.monster_bullets
    assert boss.position == 'center'
    assert boss.time_break == True
    assert boss.time_step == 50


def test_boss_waiting(boss):
    """
    Test the waiting function of the boss
    """
    # Test waiting decreases time_step by 1
    boss.time_step = 10
    boss.waiting()
    assert boss.time_step == 9

    # Test waiting sets time_break to True when time_step reaches 0
    boss.time_step = 1
    boss.waiting()
    assert boss.time_break is True
    assert boss.time_step == 0


def test_boss_move(boss):
    """
    Test the move function of the boss
    """
    # Test moving from 'center' to 'left_up'
    for _ in range(int((boss.first_position_x - 400)/config.VEL_BOSS)):  # number of iterations needed to reach the target position
        boss.move()
    assert boss.position == 'left_up'
    assert boss.time_break is False
    assert boss.time_step == 50
    assert boss.rect.x == pytest.approx(400, abs=1e-3)  # The boss should be approximately at x=400


def test_boss_move_no_state_change(boss):
    """
    Test the move method of the Boss class when no state change should occur.
    """
    # Set the boss to a non-moving state
    boss.time_break = False

    # Capture the current state of the boss
    previous_state = (boss.rect.x, boss.rect.y, boss.position)

    # Call the move method
    boss.move()

    # Check that the state has not changed
    current_state = (boss.rect.x, boss.rect.y, boss.position)
    assert previous_state == current_state
