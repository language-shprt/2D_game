import sys
import pygame

from time import sleep

from game_settings import GameSettings
from game_records import Statistics
from word import WordSpell
from letter_holders import LetterHolder
from bee import Bee
from dandelion import DandelionSeed

class SpellBeeGame:
    """Overall class to manage the game."""

    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()

        self.level_time = 0

        self.settings = GameSettings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Spelling Bee Game')

        self.stats = Statistics(self)
        self.bee = Bee(self)
        
        self.dandelions = pygame.sprite.Group()
        self.new_dandelion = DandelionSeed(self)
        self.dandelions.add(self.new_dandelion)

        self.word = WordSpell(self)
        self.model_word = self.word.get_random_word()
        self.letters_model_word = self.word.get_letters(self.model_word)
        self.player_word = self.word.create_placeholder_word()
        self.empty_pane = WordSpell(self)
        self.holders = pygame.sprite.Group()
        self.create_letter_holders()
    
    def create_letter_holders(self):
        while len(self.holders) < self.settings.number_letters:
            self.new_holder = LetterHolder(self)
            if pygame.sprite.spritecollideany(self.new_holder, self.holders):
                print(self.holders)
                continue
            else:
                self.holders.add(self.new_holder)
        
    def start_new_level(self):
        """"Respond to the correctly completed level."""
        self.dandelions.empty()
        self.holders.empty()
        self.stats.level_up()
        self.model_word = self.word.get_random_word()
        self.letters_model_word = self.word.get_letters(self.model_word)
        self.player_word = self.word.create_placeholder_word()
        self.create_letter_holders()
        self.new_dandelion = DandelionSeed(self)
        self.dandelions.add(self.new_dandelion)
        self.bee.center_bee()
        self.settings.bonuses_number += 1
        self.level_time = 0
        
    def run_game(self):
        """Start the main loop for the game."""
        self.get_player_name()
        while True:
            # Watch for events (keyboard and mouse).
            self.get_time()
            if self.level_time > self.settings.time_memorize_letters:
                self._check_events()
                self.bee.update()
            self._update_dandelions()
            self.check_bee_letter_holder_collisions()
            self._update_screen()
    
    def get_time(self):
        player_time = pygame.time.Clock().tick(60)
        self.level_time += player_time
        return self.level_time
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
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
            self.game_over()

    def get_player_name(self):
        player_name_input_flag = True
        self.screen.fill(self.settings.background_color)
        available_space = self.screen.get_rect().width - 600
        input_frame = pygame.Rect(200, 200, available_space, 60)
        input_frame.center = self.screen.get_rect().center
        pygame.draw.rect(self.screen, self.settings.square_color, input_frame)
        while player_name_input_flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        self.game_over()
                    elif event.key == pygame.K_BACKSPACE:
                        self.settings.player_name = self.settings.player_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        player_name_input_flag = False
                    else:
                        self.settings.player_name += event.unicode
            font = pygame.font.SysFont('Arial', 50)
            player_name_image = font.render(self.settings.player_name, True, self.settings.text_color)
            message = 'Please enter your name'
            message_image = font.render(message, True, self.settings.text_color)
            self.screen.fill(self.settings.background_color)
            pygame.draw.rect(self.screen, self.settings.square_color, input_frame)
            self.screen.blit(message_image, (input_frame.x + 20, input_frame.y - 100))
            self.screen.blit(player_name_image, (input_frame.x + 20, input_frame.y))
            pygame.display.update()
        print(f'player name is: {self.settings.player_name}')

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
        if len(self.dandelions) < self.settings.number_dandelions and self.new_dandelion.rect.bottom > 200:
            self.new_dandelion = DandelionSeed(self)
            self.dandelions.add(self.new_dandelion)

    def _delete_old_dandelions(self):
        for dandelion in self.dandelions.copy():
            if dandelion.rect.top >= self.settings.screen_height:
                self.dandelions.remove(dandelion)
    
    def _update_dandelions(self):
        self.dandelions.update()    
        self._delete_old_dandelions()
        self._create_falling_dandelions()
        self._check_bee_dandelion_collisions()

    def _check_bee_dandelion_collisions(self):
        if pygame.sprite.spritecollideany(self.bee, self.dandelions):
                print("Collision with a dandelion. Game over!")
                self.game_over()

    def check_bee_letter_holder_collisions(self):
        for holder in self.holders.copy():
            if pygame.sprite.collide_rect(self.bee, holder):
                print("The bee touched the holder!")
                index_holder_picked = self.holders.sprites().copy().index(holder)
                self.check_spelling(index_holder_picked, holder)

    def _remove_letter_holder(self, holder):
        holder.rect.x = -100
        holder.rect.y = -100
    
    def check_spelling(self, index_holder_picked, holder):
        if '*' in self.player_word:
            current_letter_index = self.player_word.index('*')
            if self.model_word[current_letter_index] == self.model_word[index_holder_picked]:
                print('correct letter!')
                self.player_word[current_letter_index] = self.model_word[index_holder_picked]
                self._remove_letter_holder(holder)
                self.stats.recalcualte_player_score()
                print(self.player_word)
            else:
                print('wrong letter')
                if self.settings.bonuses_number > 1:
                    print('...but there are bonuses!')
                    right_index = 0
                    for i in range(self.settings.number_letters):
                        if self.model_word[i] == self.model_word[index_holder_picked]:
                            right_index = i
                            
                    self.player_word[right_index] = self.model_word[index_holder_picked]
                    self.settings.bonuses_number -= 1
                    self._remove_letter_holder(holder)
                    print(self.player_word)
                else:
                    self.player_word[current_letter_index] = self.model_word[index_holder_picked]
                    print(self.player_word)
                    print('Wrong letter, no bonuses. Game over!')
                    self.game_over()

        if '*' not in self.player_word:
            if self.player_word == self.letters_model_word:
                print("The level is successfully completed!")
                self.start_new_level()
            else:
                print("The spelling is not correct. Game over!")
                self.game_over()
    
    def _update_screen(self):
        # Redraw the screen.
        self.screen.fill(self.settings.background_color)
        # Redraw the dandelions.
        for dandelion in self.dandelions.sprites():
            dandelion.draw_dandelion()
        # Redraw an empty word pane.
        for i in range(self.settings.number_letters):
            self.empty_pane.create_empty_word_pane(i)
            self.empty_pane.draw_letter_in_square(self.player_word, i)
        # Redraw the word.
        for i in range(self.settings.number_letters):
            self.word.create_word_pane(i, self.settings.starting_x)
            self.word.draw_letter_in_square(self.model_word, i)
        # Redraw letter holders.
        for holder in self.holders.sprites():
            holder.draw_letter_holder()
            index = self.holders.sprites().copy().index(holder)
            # if self.level_time <= self.settings.time_memorize_letters:
            holder.draw_letter_in_holder(self.model_word, index)
        # Redraw the bee.
        self.bee.draw_on_screen()
        self.stats.show_bonuses()
        self.stats.show_score_on_screen()

        # Show the most recently drawn surface (screen).
        pygame.display.flip()

    def update_records_table(self):
        old_records_table = self.stats.read_highest_scores()
        new_records_table = self.stats.check_for_new_records(old_records_table)
        self.stats.save_new_records_table()

    def game_over(self):
        """End the game."""
        self.update_records_table()
        self.stats.show_records_table()
        # Pause for a while.
        sleep(3)
        sys.exit()

if __name__ == '__main__':
    # Make the game instance and run the game.
    spell_bee = SpellBeeGame()
    spell_bee.run_game()