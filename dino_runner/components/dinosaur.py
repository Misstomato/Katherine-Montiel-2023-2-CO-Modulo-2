import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER, HAMMER

RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
DUCK_IMAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    DUCK_Y_POS = 350

    def __init__(self, game):
        self.game = game
        self.type = DEFAULT_TYPE
        self.dino_image = RUN_IMAGE[self.type][0]
        self.dino_rect = self.dino_image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False
        self.has_power_up = False
        self.power_up_time = 0
        self.hammer = HAMMER

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        
        if self.step_index > 9:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.dino_image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.dino_image = RUN_IMAGE[self.type][self.step_index // 5]
        self.dino_rect = self.dino_image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1   

    def jump(self):
        self.dino_image = JUMP_IMAGE[self.type]
        #en el eje y = 310
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.dino_image = DUCK_IMAGE[self.type][self.step_index // 5]
        self.dino_rect = self.dino_image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.DUCK_Y_POS
        self.step_index += 1

    def reset(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_speed = self.JUMP_SPEED
