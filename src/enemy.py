from src.config import Config
from src.monster import Monster


config = Config()


class Bat(Monster):
    """
    A class representing a bat monster.

    Attributes:
        first_position_x (int): the initial x position of the monster.
        first_position_y (int): the initial y position of the monster.
        size_width (int): the width of the monster sprite.
        size_height (int): the height of the monster sprite.
    """
    def __init__(self, x, y):
        self.first_position_x = x
        self.first_position_y = y
        self.size_width = 80
        self.size_height = 60
        super().__init__(config.BAT_IMAGE, self.first_position_x, self.first_position_y, self.size_width, self.size_height, config.BAT_HEALTH)

    def move(self, keys=None, target=None):
        """
        Moves the bat towards the target.

        Args:
            keys (dict): dictionary of keys pressed.
            target (Player): instance of the Player class representing the target.
        """
        if target.x > self.rect.x:
            self.rect.x += config.VEL_BAT
        if target.x < self.rect.x:
            self.rect.x -= config.VEL_BAT
        if target.y > self.rect.y:
            self.rect.y += config.VEL_BAT
        if target.y < self.rect.y:
            self.rect.y -= config.VEL_BAT

    def reset(self, position_x, position_y):
        """
        Resets the bat instance to its initial position and state.

        Args:
            position_x (int): the initial x position of the bat.
            position_y (int): the initial y position of the bat.
        """
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_alive = True
        self.health = config.BAT_HEALTH

    def shoot(self, player):
        """
        The Bat class does not shoot, so this method does nothing.
        """
        pass

    def handle_monster_bullets(self, player, win):
        """
        The Bat class does not shoot, so this method does nothing.
        """
        pass


class Mage(Monster):
    """
    A class representing a mage monster.

    Attributes:
        first_position_x (int): the initial x position of the monster.
        first_position_y (int): the initial y position of the monster.
        size_width (int): the width of the monster sprite.
        size_height (int): the height of the monster sprite.
    """
    def __init__(self, x, y):
        self.first_position_x = x
        self.first_position_y = y
        self.size_width = 60
        self.size_height = 100
        super().__init__(config.MAGE_IMAGE, self.first_position_x, self.first_position_y, self.size_width, self.size_height, config.MAGE_HEALTH)

    def move(self, keys=None, target=None):
        """
        The Mage class does not move, so this method does nothing.
        """
        pass

    def reset(self, position_x, position_y):
        """
        Resets the bat instance to its initial position and state.

        Args:
            position_x (int): the initial x position of the bat.
            position_y (int): the initial y position of the bat.
        """
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_alive = True
        self.health = config.MAGE_HEALTH
        self.monster_bullets = []


class Boss(Monster):
    """
    A class representing a boss monster.

    Attributes:
        first_position_x (int): the initial x position of the monster.
        first_position_y (int): the initial y position of the monster.
        size_width (int): the width of the monster sprite.
        size_height (int): the height of the monster sprite.
        position (str): the current position of the boss.
        time_break (bool): a flag that indicates if the boss is waiting or moving.
        time_step (int): the time left until the boss stops waiting.
    """
    def __init__(self):
        self.first_position_x = 900
        self.first_position_y = 150
        self.size_width = 60
        self.size_height = 100
        super().__init__(config.BOSS_IMAGE, self.first_position_x, self.first_position_y, self.size_width, self.size_height, config.BOSS_HEALTH)
        self.position = 'center'
        self.time_break = True
        self.time_step = 50

    def reset(self, position_x=900, position_y=150):
        """Reset the player to its initial state at the given position."""
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_alive = True
        self.health = config.BOSS_HEALTH
        self.monster_bullets = []
        self.position = 'center'
        self.time_break = True
        self.time_step = 50

    def waiting(self):
        """
        Decreases the time left until the boss stops waiting.
        """
        if self.time_step == 0:
            self.time_break = True
        else:
            self.time_step -= 1

    def move(self, keys=None, target=None):
        """
        Moves the boss instance to a new position.

        Args:
            keys (pygame.key): the keys pressed by the player.
            target (Player): the player instance.
        """
        # center
        if self.position == 'center' and self.time_break:
            if self.rect.x > 400:
                self.rect.x -= config.VEL_BOSS
            if self.rect.y > 150:
                self.rect.y -= config.VEL_BOSS
            if self.rect.x == 400 and self.rect.y == 150:
                self.position = 'left_up'
                self.time_break = False
                self.time_step = 50

        # wait in center
        elif self.position == 'left_up' and not self.time_break:
            self.waiting()

        #  go to left up
        elif self.position == 'left_up' and self.time_break:
            if self.rect.x > 100:
                self.rect.x -= config.VEL_BOSS
            if self.rect.y > 80:
                self.rect.y -= config.VEL_BOSS
            if self.rect.x == 100 and self.rect.y == 80:
                self.position = 'right_up'
                self.time_break = False
                self.time_step = 50

        # wait in left up
        elif self.position == 'right_up' and not self.time_break:
            self.waiting()

        #  go to right up
        elif self.position == 'right_up' and self.time_break:
            if self.rect.x < 600:
                self.rect.x += config.VEL_BOSS
            if self.rect.x == 600 and self.rect.y == 80:
                self.position = 'left_down'
                self.time_break = False
                self.time_step = 50

        # wait in right up
        elif self.position == 'left_down' and not self.time_break:
            self.waiting()

        #  go to left_down
        elif self.position == 'left_down' and self.time_break:
            if self.rect.x > 100:
                self.rect.x -= config.VEL_BOSS
            if self.rect.y < 250:
                self.rect.y += config.VEL_BOSS
            if self.rect.x == 100 and self.rect.y == 250:
                self.position = 'right_down'
                self.time_break = False
                self.time_step = 50

        # wait in left_down
        elif self.position == 'right_down' and not self.time_break:
            self.waiting()

        #  go to right_down
        elif self.position == 'right_down' and self.time_break:
            if self.rect.x < 600:
                self.rect.x += config.VEL_BOSS
            if self.rect.x == 600 and self.rect.y == 250:
                self.position = 'center'
                self.time_break = False
                self.time_step = 50

        # wait in right_down
        elif self.position == 'center' and not self.time_break:
            self.waiting()
