import pygame
from block_library import *

class BadBlock(Block):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def update(self):
        super().update()
        self.image = pygame.image.load("art/enemy.png").convert()
        self.rect.y += 3

        if (self.rect.y > 400):
            self.rect.y = -15
