from abc import ABC, abstractmethod


# Abstract class for updatable objects
class Updatable(ABC):

    @abstractmethod
    def update(self):
        """Update the object's state."""
        pass
