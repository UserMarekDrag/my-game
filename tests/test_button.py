from pathlib import Path
import sys
import pygame


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.button import Button, ButtonBuilder


def test_button_init():
    """
    Test the initialization of the Button class.
    """
    button = Button()
    assert button.position_x == 0
    assert button.position_y == 0
    assert button.width > 0
    assert button.height > 0
    assert isinstance(button.image, pygame.Surface)
    assert isinstance(button.rect, pygame.Rect)


def test_button_is_pressed():
    """
    Test the is_pressed method of the Button class.
    """
    button = Button()
    # When button is not clicked, it should return False
    assert not button.is_pressed((0, 0), (0, 0, 0))
    # When button is clicked, it should return True
    button.rect.x = 0
    button.rect.y = 0
    assert button.is_pressed((1, 1), (1, 0, 0))


def test_button_builder_init():
    """
    Test the initialization of the ButtonBuilder class.
    """
    builder = ButtonBuilder()
    assert isinstance(builder._button, Button)


def test_button_builder_set_position_method():
    """
    Test the set_position method of the ButtonBuilder class.
    """
    builder = ButtonBuilder()
    builder.set_position(10, 20)
    assert builder._button.position_x == 10
    assert builder._button.position_y == 20
    assert builder._button.rect.x == 10
    assert builder._button.rect.y == 20


def test_button_builder_set_content():
    """
    Test the set_content method of the ButtonBuilder class.
    """
    builder = ButtonBuilder()
    builder.set_content("Test")
    assert builder._button.content == "Test"
    assert isinstance(builder._button.text, pygame.Surface)


def test_button_builder_set_action():
    """
    Test the set_action method of the ButtonBuilder class.
    """
    builder = ButtonBuilder()

    def action():
        print("Action executed")

    builder.set_action(action)
    assert builder._button.action == action


def test_button_builder_build():
    """
    Test the build method of the ButtonBuilder class.
    """
    builder = ButtonBuilder()
    button = builder.set_position(10, 20).set_content("Test").set_action(lambda: print("Action executed")).build()
    assert isinstance(button, Button)
    assert button.position_x == 10
    assert button.position_y == 20
    assert button.content == "Test"
