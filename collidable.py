from abc import ABC, abstractmethod


# Abstract class for collidable objects
class Collidable(ABC):

    @abstractmethod
    def check_collision(self, other):
        """Check if the object collides with another object."""
        pass
