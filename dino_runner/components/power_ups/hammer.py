import pygame

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH

class Hammer(PowerUp):
    def __init__(self):
        self.hammer_thrown = False
        super().__init__(HAMMER, HAMMER_TYPE)

    def update_hammer(self, game_speed):
        self.rect.x += game_speed

