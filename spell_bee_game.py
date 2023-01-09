import sys
import pygame

from game_settings import GameSettings
from bee import Bee
from dandelion import DandelionSeed

class SpellBeeGame:
    """Overall class to manage the game."""

    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()
        self.settings = GameSettings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Spelling Bee Game')

        self.bee = Bee(self)
        self.dandelions = []
        self.dandelions_counter = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for events (keyboard and mouse).
            self._check_events()
            self.bee.update()
            for dandelion in self.dandelions:
                dandelion.update()
            self._delete_old_dandelions()
            self._create_falling_dandelions()
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
            self.bee.movement_direction = "to_the_right"
        elif event.key == pygame.K_LEFT:
            self.bee.movement_left_flag = True
            self.bee.movement_direction = "to_the_left"
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

    def _create_falling_dandelions(self):
        if self.dandelions_counter < self.settings.number_dandelions and (len(self.dandelions) == 0 or self.dandelions[-1].rect.bottom > 200):
            new_dandelion = DandelionSeed(self)
            self.dandelions_counter += 1
            self.dandelions.append(new_dandelion)
            print(self.dandelions_counter)

    def _delete_old_dandelions(self):
        for dandelion in self.dandelions.copy():
            if dandelion.rect.top >= self.settings.screen_height:
                self.dandelions.remove(dandelion)
                self.dandelions_counter -= 1
            print(len(self.dandelions))
    
    def _update_screen(self):
        # Redraw the screen.
        self.screen.fill(self.settings.background_color)
        # Redraw the bee.
        self.bee.draw_on_screen()
        # Redraw the dandelions.
        for dandelion in self.dandelions:
            dandelion.draw_dandelion()

        # Show the most recently drawn surface (screen).
        pygame.display.flip()

if __name__ == '__main__':
    # Make the game instance and run the game.
    spell_bee = SpellBeeGame()
    spell_bee.run_game()