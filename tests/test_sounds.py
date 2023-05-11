from pathlib import Path
import sys
import pygame
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.sounds import Sounds


@pytest.fixture
def sounds_instance():
    """
    Fixture: Initialize an instance of Sounds before each test.
    """
    return Sounds()


def test_singleton_instance(sounds_instance):
    """
    Test to check if the singleton works correctly.
    """
    sounds1 = sounds_instance
    sounds2 = sounds_instance
    assert sounds1 is sounds2


def test_init_sounds(sounds_instance):
    """
    Test to check the initialization of the sound effects.
    """
    sounds_instance.init_sounds()
    assert isinstance(sounds_instance.bullet_hit_sound, pygame.mixer.Sound)
    assert isinstance(sounds_instance.bullet_fire_sound, pygame.mixer.Sound)


def test_sound_files_exist(sounds_instance):
    """
    Test to check if the sound files exist.
    """
    sounds_instance.init_sounds()

    base_dir = Path(__file__).resolve().parent.parent.parent
    bullet_hit_sound_file = base_dir / 'Game' / 'Assets' / 'Grenade+1.mp3'
    bullet_fire_sound_file = base_dir / 'Game' / 'Assets' / 'Gun+Silencer.mp3'

    assert bullet_hit_sound_file.exists()
    assert bullet_fire_sound_file.exists()
