import pygame
import json
import random

from game_settings import GameSettings

class WordSpell():
    """A class to represent a word for player to spell."""

    def __init__(self, game_session):
        """Initialize a random word (model) and establish its position inside colored squares."""

        self.screen = game_session.screen
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

    def get_random_word(self):
        with open('word_pull.json', encoding='utf-8') as input_data:
            text_in_file = json.load(input_data)

        word_length = self.settings.number_letters
        possible_words = text_in_file[str(word_length)]
        word_to_spell = random.choice(possible_words).upper()
        return word_to_spell

    def create_word_pane(self, letter_index, starting_x):
        # Drawing border
        color = self.settings.border_color
        square_y = self.settings.starting_y
        square_x = 20 + starting_x*(letter_index)
        dimension = self.settings.square_dimension
        border = pygame.Rect(square_x, square_y, dimension, dimension)
        pygame.draw.rect(self.screen, color, border)

        # Drawing squares
        color = self.settings.square_color
        square_y = self.settings.starting_y + self.settings.border
        square_x = 20 + starting_x*(letter_index) + self.settings.border 
        dimension = self.settings.square_dimension - 2*self.settings.border
        self.word_square = pygame.Rect(square_x, square_y, dimension, dimension)
        pygame.draw.rect(self.screen, color, self.word_square)

    def draw_letter_in_square(self, word, letter_index):
        # Drawing each letter inside a square
        text_color = self.settings.text_color
        self.font = pygame.font.SysFont('Arial', 50)
        self.letter_image = self.font.render(word[letter_index], True, text_color)
        self.letter_image_rect = self.letter_image.get_rect()
        self.letter_image_rect.center = self.word_square.center
        self.screen.blit(self.letter_image, self.letter_image_rect)

    def create_empty_word_pane(self, letter_index):
        # Drawing border
        color = self.settings.border_color
        square_y = self.settings.starting_y
        dimension = self.settings.square_dimension
        square_x = self.screen_rect.width - 80 - (dimension + 2) *(letter_index)
        border = pygame.Rect(square_x, square_y, dimension, dimension)
        pygame.draw.rect(self.screen, color, border)

        # Drawing squares
        color = self.settings.square_color
        square_y = self.settings.starting_y + self.settings.border
        square_x = square_x + self.settings.border
        dimension = dimension - 2*self.settings.border
        self.word_square = pygame.Rect(square_x, square_y, dimension, dimension)
        pygame.draw.rect(self.screen, color, self.word_square)