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
from block_library import *
from goodblock_library import *
from badblock_library import *
from player_library import *
from File import *

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)

class GameLevel():
    def __init__(self, Screen):
        #initialize pygame
        pygame.init()

        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds/gameSound.ogg')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play(-1)
        
        #define screen
        self.screen = Screen
        
        #define the width and heights
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        # This is a list of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'Group.'
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
         
        # This is a list of every sprite. 
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()

        file = File()
        #goodSprites
        for item in file.LoadFile():
            if (item[0] == "good_block"):
                # This represents a block
                block = GoodBlock(GREEN, 20, 15, item[1], int(item[2]))
             
                # Set a random location for the block
                block.rect.x = random.randrange(screen_width-20) #keep them all on screen
                block.rect.y = random.randrange(screen_height-15)
             
                # Add the block to the list of objects
                self.good_block_list.add(block)
                self.all_sprites_list.add(block)

            #badSprites
            elif (item[0] == "bad_block"):
                # This represents a block
                block = BadBlock(RED, 20, 15, item[1], int(item[2]))
             
                # Set a random location for the block
                block.rect.x = random.randrange(screen_width-20) #keep them all on screen
                block.rect.y = random.randrange(screen_height-15)
             
                # Add the block to the list of objects
                self.bad_block_list.add(block)
                self.all_sprites_list.add(block)
         
        # Create a RED player block
        self.player = Player(50, 50)
        self.all_sprites_list.add(self.player)
        
        #initial location of player
        self.player.rect.x = 50
        self.player.rect.y = 50
        
        #start a score
        self.score = 0
        
    def update(self, xSpeed, ySpeed):
        #define the width and height
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        
         
        # Loop until the user clicks the close button.
        done = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        

        #define a font
        font = pygame.font.SysFont('Calibri', 25, True, False)

        #move the player
        self.player.changespeed(xSpeed, ySpeed)

        # Clear the screen
        self.screen.fill(WHITE)
     
        #See if the player block has collided with anygood blocks.
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
     
        #Check the list of collisions.
        goodBlockSound = pygame.mixer.Sound("sounds/goodBlockSound.wav")
        for block in blocks_hit_list:
            self.score += 5
            goodBlockSound.play()

        # See if the player block has collided with any bad blocks.
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)
     
        #adjust score and play sound
        badBlockSound = pygame.mixer.Sound("sounds/badBlockSound.wav")
        for block in blocks_hit_list:
            self.score -= 1
            badBlockSound.play()

        #update all sprites
        self.all_sprites_list.update()

        #keep the player on the screen
        borderSound = pygame.mixer.Sound("sounds/borderSound.wav")
        if (self.player.rect.x > screen_width - self.player.width):
            self.player.rect.x = screen_width - self.player.width
            borderSound.play()
        if (self.player.rect.y > screen_height - self.player.height):
            self.player.rect.y = screen_height - self.player.height
            borderSound.play()
        if (self.player.rect.x < 0):
            self.player.rect.x = 0
            borderSound.play()
        if (self.player.rect.y < 0):
            self.player.rect.y = 0
            borderSound.play()
        
        # Draw all the sprites
        self.all_sprites_list.draw(self.screen)

        #display score
        text = font.render("Score: " + str(self.score),True,BLACK)
        text2 = font.render("Press Enter To Return To Title Screen",True,BLACK)
        self.screen.blit(text, [0, 0])
        self.screen.blit(text2, [300, 0])
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
