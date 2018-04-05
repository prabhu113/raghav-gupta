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

class TitleLevel():
    def __init__(self, Screen):
        #initialize pygame
        pygame.init()
        
        pygame.mixer.music.stop()
        
        pygame.mixer.music.load('sounds/titleSound.ogg')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play(-1)
        
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
        
        # Clear the screen
        self.screen.fill(WHITE)
     
        #display title
        text = font.render("Title Screen!!!",True,BLACK)
        text2 = font.render("Press Enter To Start Game",True,BLACK)
        text3 = font.render("Press 'C' To View Credits",True,BLACK)
        self.screen.blit(text, [275, 150])
        self.screen.blit(text2, [220, 180])
        self.screen.blit(text3, [230, 210])
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
