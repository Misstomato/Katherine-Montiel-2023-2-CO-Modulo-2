import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Small_cactus(Obstacle):
    #image is a list
    def __init__(self, image):
        #type is an index
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325