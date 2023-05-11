from pathlib import Path
import pygame


class Sounds:
    """
    A singleton class for managing sound effects in the game.

    Attributes:
    -----------
    bullet_hit_sound: pygame.mixer.Sound
        Sound played when a bullet hits an enemy or the player
    bullet_fire_sound: pygame.mixer.Sound
        Sound played when a bullet is fired by the player's character
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of Sounds class if it does not exist, otherwise return the existing one.

        Returns:
        --------
        cls._instance : Sounds
            The instance of the Sounds class
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Check if the instance has been initialized
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.init_sounds()

    def init_sounds(self):
        pygame.mixer.init()
        base_dir = Path(__file__).resolve().parent.parent.parent
        try:
            bullet_hit_sound_file = base_dir / 'game' / 'Assets' / 'Grenade+1.mp3'
            self.bullet_hit_sound = pygame.mixer.Sound(str(bullet_hit_sound_file))

            bullet_fire_sound_file = base_dir / 'game' / 'Assets' / 'Gun+Silencer.mp3'
            self.bullet_fire_sound = pygame.mixer.Sound(str(bullet_fire_sound_file))
        except pygame.error as error:
            print('Error while loading sounds:', error)
