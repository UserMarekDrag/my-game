from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.interfaces import Drawable, Collidable, Updatable


class TestDrawable(Drawable):
    def draw(self, win):
        pass


class TestCollidable(Collidable):
    def check_collision(self, other, type_other):
        pass


class TestUpdatable(Updatable):
    def update(self):
        pass


def test_drawable_interface():
    drawable = TestDrawable()
    assert hasattr(drawable, 'draw'), "Drawable interface not correctly implemented."


def test_collidable_interface():
    collidable = TestCollidable()
    assert hasattr(collidable, 'check_collision'), "Collidable interface not correctly implemented."


def test_updatable_interface():
    updatable = TestUpdatable()
    assert hasattr(updatable, 'update'), "Updatable interface not correctly implemented."
