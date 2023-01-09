import pygame
import random
from pygame.sprite import Sprite

class DandelionSeed(Sprite):
    "A class to represent a single dandelion seed."

    def __init__(self, game_session):
        """Initialize the dandelion seed and set its starting position."""
        super().__init__()
        self.screen = game_session.screen
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

        self.image = pygame.image.load('images/dandelion_smallest.bmp')
        self.rect = self.image.get_rect()

        # Starting position of a new dandelion (top of the screen, random x).
        self.rect.x = random.randint(0, self.screen_rect.width)
        self.rect.y = 0

        self._store_decimal_value()

    def _store_decimal_value(self):
        # Store the dandelion's position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def _update_coordinates(self):
        # Update the coordinates after the movement is completed.
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # Move the dandelion left or right and down.
        self.y += self.settings.dandelion_speed
        self.settings.wind_direction = random.randint(0, 1) 
        if self.settings.wind_direction == 0:
            self.x += self.settings.wind_speed
        else:
            self.x -= self.settings.wind_speed
        self._update_coordinates()

    def draw_dandelion(self):
        """Draw a dandelion to the screen."""
        self.screen.blit(self.image, self.rect)