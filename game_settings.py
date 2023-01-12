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
        # 0 is right, 1 is left
        self.wind_direction = 0

        self.number_letters = 3
        self.square_color = (190, 150, 110)
        self.square_dimension = 60
        self.starting_x = 30
        self.starting_y = 30
        self.border_color = (60, 60, 60)
        self.border = 3

        self.text_color = (90, 0, 0)