import pygame
from dandelion import DandelionSeed
from pygame.sprite import Group

class Statistics:
    """Track and record statistics for the Spelling Bee game."""

    def __init__(self, game_session):
        """Initialize the class to manage the game's records."""
        self.game_session = game_session
        self.screen = game_session.screen
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

    def level_up(self):
        self.settings.number_dandelions += 1
        self.settings.dandelion_speed += 0.2
        self.settings.number_letters += 1

    def show_bonuses(self):
        """Show how many bonuses the player has."""
        self.bonuses = Group()
        for bonus_number in range(self.settings.bonuses_number):
            bonus = DandelionSeed(self.game_session)
            bonus.rect.x = self.screen_rect.width - bonus_number * bonus.rect.width
            bonus.rect.bottom = self.screen_rect.bottom
            self.bonuses.add(bonus)
        
        self.bonuses.draw(self.screen)