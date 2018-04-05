import pygame
import random
from block_library import *

class GoodBlock(Block):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def update(self):
        super().update()
        self.image = pygame.image.load("art/goodGuy.png").convert()
        self.rect.x += random.randrange(-3, 4)
        self.rect.y += random.randrange(-3, 4)
