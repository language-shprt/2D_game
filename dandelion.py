import pygame
from pygame.sprite import Sprite

class DandelionSeed(Sprite):
    "A class to represent a single dandelion seed."

    def __init__(self, game_session):
        """Initialize the dandelion seed and set its starting position."""
        super().__init__()
        self.screen = game_session.screen

        self.image = pygame.image.load('images/dandelion_smallest.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self._store_decimal_value()

    def _store_decimal_value(self):
        # Store the dandelion's horizontal position.
        self.x = float(self.rect.x)