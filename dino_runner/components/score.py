import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, PINK

class Score:
    def __init__(self, high_score):
        self.high_score = high_score
        self.current_score = 0
        self.font = pygame.font.Font(FONT_STYLE, 18) 
        self.color = BLACK

    def update(self):
        self.current_score += 1
        self.check_highest()

    def draw(self, screen):
        self.label = self.font.render(f'HS {self.high_score}  {self.current_score}', 1, self.color)
        label_width = self.label.get_rect().width
        screen.blit(self.label, (SCREEN_WIDTH - label_width - 10, 10))

    def check_highest(self):
        if self.current_score >= self.high_score:
            self.high_score = self.current_score

    def set_dark_mode(self):
        if self.color == BLACK:
            self.color = PINK
        else:
            self.color = BLACK