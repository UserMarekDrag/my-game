from abc import ABC, abstractmethod


# Abstract class for drawable objects
class Drawable(ABC):

    @abstractmethod
    def draw(self, win):
        """Draw the object on the screen."""
        pass
