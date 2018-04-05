"""
Code editors (2/18/2018):
Jack Morris, Raghav Gupta, Jake Kautzman

Code originally from:
http://programarcadegames.com/python_examples/f.php?file=sprite_collect_blocks.py
player class from:
http://programarcadegames.com/python_examples/f.php?file=move_sprite_keyboard_smooth.py

Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)

class CreditsLevel():
    def __init__(self, Screen):
        #initialize pygame
        pygame.init()

        #define screen
        self.screen = Screen
        
        #define the width and heights
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
    def update(self):
        #define the width and height
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        
         
        # Loop until the user clicks the close button.
        done = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        

        #define a font
        font = pygame.font.SysFont('Calibri', 25, True, False)
        font3 = pygame.font.SysFont('Calibri', 20, True, False)
        font2 = pygame.font.SysFont('Calibri', 15, True, False)
        
        # Clear the screen
        self.screen.fill(WHITE)
     
        #display title
        text = font.render("Credits Screen!!!",True,BLACK)
        text2 = font.render("Gameplay Engineer - Jack Morris",True,BLACK)
        text3 = font.render("Sound/Art Engineer - Jacob Kautzman",True,BLACK)
        text4 = font.render("File Management Engineer - Raghav Gupta",True,BLACK)
        text5 = font2.render("Press Enter To Return To Title Screen",True,BLACK)
        text6 = font3.render("All Pixel Art from: https://opengameart.org/content/random-pixel-characters",True,BLACK)
        text7 = font3.render("Title Music 'One' by Cathedral Of Chemical Equilibrium",True,BLACK)
        text8 = font3.render("Game Music 'Thirteen' by Cathedral Of Chemical Equilibrium",True,BLACK)
        self.screen.blit(text, [275, 20])
        self.screen.blit(text2, [185, 60])
        self.screen.blit(text3, [160, 90])
        self.screen.blit(text4, [135, 120])
        self.screen.blit(text6, [30, 150])
        self.screen.blit(text7, [130, 170])
        self.screen.blit(text8, [110, 190])
        self.screen.blit(text5, [250, 350])
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
