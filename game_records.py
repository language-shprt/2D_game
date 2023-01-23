import pygame
from dandelion import DandelionSeed
from pygame.sprite import Group

class Statistics:
    """Track and record statistics for the Spelling Bee game."""

    def __init__(self, game_session):
        """Initialize the class to manage the game's records."""
        self.game_session = game_session
        self.screen = game_session.screen
        self.screen_rect = game_session.screen.get_rect()
        self.settings = game_session.settings

    def level_up(self):
        self.settings.number_dandelions += 1
        self.settings.dandelion_speed += 0.2
        self.settings.number_letters += 1

    def show_bonuses(self):
        """Show how many bonuses the player has."""
        self.bonuses = Group()
        for bonus_number in range(self.settings.bonuses_number):
            bonus = DandelionSeed(self.game_session)
            bonus.rect.x = self.screen_rect.width - bonus_number * bonus.rect.width
            bonus.rect.bottom = self.screen_rect.bottom
            self.bonuses.add(bonus)
        
        self.bonuses.draw(self.screen)

    def recalcualte_player_score(self):
        self.settings.score += self.settings.score_correct_letter
        return self.settings.score

    def show_score_on_screen(self):
        text_color = self.settings.text_color
        self.font = pygame.font.SysFont('Arial', 50)
        self.score_image = self.font.render(str(self.settings.score), True, text_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 10
        self.screen.blit(self.score_image, self.score_image_rect)

    def read_highest_scores(self):
        with open('all_time_score_records.txt', mode='r') as input_data:
            records_table = input_data.readlines()
        print(records_table)
        old_records_table = [score.replace('\n', '').split(';') for score in records_table]
        return old_records_table

    def check_for_new_records(self, old_records_table):
        highest_score = old_records_table[0][1]
        best_player = old_records_table[0][0]
        second_highest_score = old_records_table[1][1]
        second_player = old_records_table[1][0]
        third_highest_score = old_records_table[2][1]
        third_player = old_records_table[2][0]

        if self.settings.score >= int(highest_score):
            third_highest_score = second_highest_score
            third_player = second_player
            second_highest_score = highest_score
            second_player = best_player
            highest_score = self.settings.score
            best_player = self.settings.player_name
        elif self.settings.score >= int(second_highest_score):
            third_highest_score = second_highest_score
            third_player =  second_player
            second_highest_score = self.settings.score
            second_player = self.settings.player_name
        elif self.settings.score >= int(third_highest_score):
            third_highest_score = self.settings.score
            third_player =  self.settings.player_name

        new_records_table = [best_player + ';' + str(highest_score) + '\n', second_player + ';' + str(second_highest_score) + '\n', third_player + ';' + str(third_highest_score) + '\n']
        print(new_records_table)
        return new_records_table

    def save_new_records_table(self, new_records_table):
        with open('all_time_score_records.txt', mode='w') as output_data:
            output_data.writelines(new_records_table)