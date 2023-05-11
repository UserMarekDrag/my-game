import os
import pygame


# Singleton class to manage sound effects
class Sounds:
    """
    A singleton class for managing sound effects in the game.

    Attributes:
    -----------
    BULLET_HIT_SOUND: pygame.mixer.Sound
        Sound played when a bullet hits an enemy or the player
    BULLET_FIRE_SOUND: pygame.mixer.Sound
        Sound played when a bullet is fired by the player's character
    """

    _instance = None

    def __new__(cls):
        """
        Create a new instance of Sounds class if it does not exist, otherwise return the existing one.

        Returns:
        --------
        cls._instance : Sounds
            The instance of the Sounds class
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_sounds()
        return cls._instance

    def init_sounds(self):
        pygame.mixer.init()
        try:
            self.BULLET_HIT_SOUND = pygame.mixer.Sound(
                os.path.join('../Assets', 'Grenade+1.mp3'))
            self.BULLET_FIRE_SOUND = pygame.mixer.Sound(
                os.path.join('../Assets', 'Gun+Silencer.mp3'))
        except pygame.error as e:
            print('Error while loading sounds:', e)
