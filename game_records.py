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
        self.highest_score = old_records_table[0][1]
        self.best_player = old_records_table[0][0]
        self.second_highest_score = old_records_table[1][1]
        self.second_player = old_records_table[1][0]
        self.third_highest_score = old_records_table[2][1]
        self.third_player = old_records_table[2][0]

        if self.settings.score >= int(self.highest_score):
            self.third_highest_score = self.second_highest_score
            self.third_player = self.second_player
            self.second_highest_score = self.highest_score
            self.second_player = self.best_player
            self.highest_score = self.settings.score
            self.best_player = self.settings.player_name
        elif self.settings.score >= int(self.second_highest_score):
            self.third_highest_score = self.second_highest_score
            self.third_player =  self.second_player
            self.second_highest_score = self.settings.score
            self.second_player = self.settings.player_name
        elif self.settings.score >= int(self.third_highest_score):
            self.third_highest_score = self.settings.score
            self.third_player =  self.settings.player_name

        self.new_records_table = [self.best_player + ';' + str(self.highest_score) + '\n', self.second_player + ';' + str(self.second_highest_score) + '\n', self.third_player + ';' + str(self.third_highest_score) + '\n']
        print(self.new_records_table)
        return self.new_records_table

    def save_new_records_table(self):
        with open('all_time_score_records.txt', mode='w') as output_data:
            output_data.writelines(self.new_records_table)

    def show_records_table(self):
        self.screen.fill(self.settings.background_color)
        self.font = pygame.font.SysFont('Arial', 50)

        header = 'All-time greatest:'
        header_image = self.font.render(header, True, self.settings.text_color)
        self.header_rect = header_image.get_rect()
        self.header_rect.x = self.screen_rect.width // 2 - 200
        self.header_rect.y = self.screen_rect.height // 2 - 200
        self.screen.blit(header_image, self.header_rect)

        self.draw_player_record(self.best_player, self.highest_score, 1)
        self.draw_player_record(self.second_player, self.second_highest_score, 2)
        self.draw_player_record(self.third_player, self.third_highest_score, 3)
        pygame.display.update()

    def draw_player_record(self, name, score, place):
        player_message = f'{place}. {name} - {score}'
        print(player_message)
        image = self.font.render(player_message, True, self.settings.text_color)
        image_rect = image.get_rect()
        image_rect.x = self.header_rect.x
        image_rect.y = self.header_rect.y + (place + 1) * self.header_rect.height
        self.screen.blit(image, image_rect)