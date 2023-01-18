import pygame
import random
from pygame.sprite import Sprite

class LetterHolder(Sprite):
    "A class to represent a single letter holder with a letter."

    def __init__(self, game_session):
        """Initialize a letter holder and set its starting position."""
        super().__init__()
        self.screen = game_session.screen
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

        self.image = pygame.image.load('images/flower_letter_small.bmp')
        self.rect = self.image.get_rect()

        # Position of a new letter holder (top of the screen, random x).
        available_space_x = self.screen_rect.width - self.rect.width
        available_space_y =  self.screen_rect.height - self.rect.height
        self.rect.x = random.randint(self.rect.width, available_space_x)
        self.rect.y = random.randint(self.rect.height, available_space_y)

    def draw_letter_in_holder(self, word, letter_index):
        # Drawing each letter inside a square
        text_color = self.settings.text_color
        self.font = pygame.font.SysFont('Arial', 30)
        self.letter_image = self.font.render(word[letter_index], True, text_color)
        self.letter_image_rect = self.letter_image.get_rect()
        self.letter_image_rect.center = self.rect.center
        self.screen.blit(self.letter_image, self.letter_image_rect)
    
    def draw_letter_holder(self):
        """Draw a letter holder to the screen."""
        self.screen.blit(self.image, self.rect)