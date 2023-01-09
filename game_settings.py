class GameSettings:
    """A class to store all setting for the game."""

    def __init__(self):
        """Initialize the game settings."""
        self.screen_height = 750
        self.screen_width = 1200
        self.background_color = (153, 217, 234)

        self.bee_speed = 0.5

        self.number_dandelions = 3
        self.dandelion_speed = 0.1
        self.wind_speed = 0.4
        self.wind_direction = 0