import pygame

class Bee:
    """A class to manage a bee."""

    def __init__(self, game_session):
        """Initialize the bee and set its position at the beginning of the game."""
        self.screen = game_session.screen
        # Access the screen's rect attribute.
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

        self.image = pygame.image.load('images/bee_small.bmp')
        # Access the image rect attribute.
        self.rect = self.image.get_rect()

        # The bee starts at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.movement_right_flag = False
        self.movement_left_flag = False
        self.movement_up_flag = False
        self.movement_down_flag = False

        self.movement_direction = "to_the_left"

        self._store_decimal_value()

    def _store_decimal_value(self):
        # Keep a decimal value of each coordinate.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _update_coordinates(self):
        # Update the coordinates after the movement is completed.
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Change the bee position if movement falg set to True."""
        if self.movement_right_flag and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bee_speed
        if self.movement_left_flag and self.rect.left > 0:
            self.x -= self.settings.bee_speed
        if self.movement_up_flag and self.rect.top > self.settings.starting_y + self.settings.square_dimension + 2:
            self.y -= self.settings.bee_speed
        if self.movement_down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bee_speed

        self._update_coordinates()


    def draw_on_screen(self):
        """Draw the bee at its current locaton."""
        if self.movement_direction == "to_the_left":
            self.screen.blit(self.image, self.rect)
        elif self.movement_direction == "to_the_right":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)