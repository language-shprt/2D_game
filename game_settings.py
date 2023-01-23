class GameSettings:
    """A class to store all setting for the game."""

    def __init__(self):
        """Initialize the game settings."""
        self.background_color = (153, 217, 234)

        self.bee_speed = 10
        self.bonuses_number = 1

        self.player_name = '*'
        self.score = 0
        self.score_correct_letter = 5
        self.time_memorize_letters = 2000

        self.number_dandelions = 3
        self.dandelion_speed = 2
        self.wind_speed = 0.4
        # 0 is right, 1 is left
        self.wind_direction = 0

        self.number_letters = 3
        self.square_color = (30, 170, 75)
        self.square_dimension = 60
        self.starting_x = 62
        self.starting_y = 25
        self.border_color = (60, 60, 60)
        self.border = 3

        self.text_color = (90, 0, 0)