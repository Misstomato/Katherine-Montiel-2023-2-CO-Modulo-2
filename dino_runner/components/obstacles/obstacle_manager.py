import pygame
import random

from dino_runner.components.obstacles.small_cactus import Small_cactus
from dino_runner.components.obstacles.large_cactus import Large_cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 4) == 0:
                self.obstacles.append(Small_cactus(SMALL_CACTUS))
            elif random.randint(0, 4) == 1:
                self.obstacles.append(Large_cactus(LARGE_CACTUS))
            elif random.randint(0, 4) == 2:
                self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 4) == 3:
                self.obstacles.append(Small_cactus(SMALL_CACTUS))
                self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 4) == 4:
                self.obstacles.append(Small_cactus(SMALL_CACTUS))
                self.
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)