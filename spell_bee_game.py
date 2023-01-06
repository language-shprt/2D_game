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
        pygame.display.set_caption('Spelling Bee Game')

        self.bee = Bee(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for events (keyboard and mouse).
            self._check_events()
            self.bee.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.bee.movement_right_flag = True
        elif event.key == pygame.K_LEFT:
            self.bee.movement_left_flag = True
        elif event.key == pygame.K_UP:
            self.bee.movement_up_flag = True
        elif event.key == pygame.K_DOWN:
            self.bee.movement_down_flag = True
        elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.bee.movement_right_flag = False
        elif event.key == pygame.K_LEFT:
            self.bee.movement_left_flag = False
        elif event.key == pygame.K_UP:
            self.bee.movement_up_flag = False
        elif event.key == pygame.K_DOWN:
            self.bee.movement_down_flag = False

    def _update_screen(self):
        # Redraw the screen.
        self.screen.fill(self.settings.background_color)
        # Redraw the bee.
        self.bee.draw_on_screen()

        # Show the most recently drawn surface (screen).
        pygame.display.flip()

if __name__ == '__main__':
    # Make the game instance and run the game.
    spell_bee = SpellBeeGame()
    spell_bee.run_game()