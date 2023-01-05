import pygame

class Bee:
    """A class to manage a bee."""

    def __init__(self, game_session):
        """Initialize the bee and set its position at the beginning of the game."""
        self.screen = game_session.screen
        # Access the screen's rect attribute.
        self.screen_rect = game_session.screen.get_rect()

        self.image = pygame.image.load('images/bee_small.bmp')
        # Access the image rect attribute.
        self.rect = self.image.get_rect()

        # The bee starts at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def draw_on_screen(self):
        """Draw the bee at its current locaton."""
        self.screen.blit(self.image, self.rect)