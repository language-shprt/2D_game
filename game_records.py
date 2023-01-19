class Statistics:
    """Track and record statistics for the Spelling Bee game."""

    def __init__(self, game_session):
        """Initialize the class to manage the game's records."""
        self.settings = game_session.settings

    def level_up(self):
        self.settings.number_dandelions += 1
        self.settings.dandelion_speed += 0.2
        self.settings.number_letters += 1

    