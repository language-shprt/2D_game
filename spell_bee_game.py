import sys
import pygame

from game_settings import GameSettings
from bee import Bee

class SpellBeeGame:
    """Overall class to manage the game."""

    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()
        self.settings = GameSettings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Spell Bee Game')

        self.bee = Bee(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for events (keyboard and mouse).
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen.
            self.screen.fill(self.settings.background_color)
            self.bee.draw_on_screen()

            # Show the most recently drawn surface (screen).
            pygame.display.flip()

if __name__ == '__main__':
    # Make the game instance and run the game.
    spell_bee = SpellBeeGame()
    spell_bee.run_game()