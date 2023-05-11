from abc import ABC, abstractmethod


# Abstract class for drawable objects
class Drawable(ABC):

    @abstractmethod
    def draw(self, win):
        """Draw the object on the screen."""
        pass


# Abstract class for collidable objects
class Collidable(ABC):

    @abstractmethod
    def check_collision(self, other, type_other):
        """Check if the object collides with another object."""
        pass


# Abstract class for updatable objects
class Updatable(ABC):

    @abstractmethod
    def update(self):
        """Update the object's state."""
        pass
