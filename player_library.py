
""" Code Originally from:
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

"""Code Edited by (2/18/2018):
Jack Morris, Raghav Gupta, Jake Kautzman
"""


import pygame

BLUE  = (  0,   0, 255)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.width = 15
        self.height = 15
        self.image = pygame.image.load("art/player.png").convert()
        
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        #changed to set speed
        """ Change the speed of the player"""
        self.change_x = x
        self.change_y = y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
