"""
Code editors (2/9/2018):
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
import random
from block_library import *
from goodblock_library import *
from badblock_library import *
from player_library import *

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)


# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

#goodSpritesAreGood
for i in range(50):
    # This represents a block
    block = GoodBlock(GREEN, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-20) #keep them all on screen
    block.rect.y = random.randrange(screen_height-15)
 
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

#badSpritesAreBad
for i in range(50):
    # This represents a block
    block = BadBlock(RED, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-20) #keep them all on screen
    block.rect.y = random.randrange(screen_height-15)
 
    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player(50, 50)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

#initial location of player
player.rect.x = 50
player.rect.y = 50

#define a font
font = pygame.font.SysFont('Calibri', 25, True, False)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True

        #implementation of movement adapted from the same location Player is from
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
  
    # Clear the screen
    screen.fill(WHITE)
 
    #See if the player block has collided with anygood blocks.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
 
    #Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        

    # See if the player block has collided with any bad blocks.
    blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    #adjust score
    for block in blocks_hit_list:
        score += -1

    #update all sprites
    all_sprites_list.update()

    #keep the player on the screen
    if (player.rect.x > screen_width-15):
        player.rect.x = screen_width-15
        print("Too Far Right")
    if (player.rect.y > screen_height-15):
        player.rect.y = screen_height-15
        print("Too Far Down")
    if (player.rect.x < 0):
        player.rect.x = 0
        print("Too Far Left")
    if (player.rect.y < 0):
        player.rect.y = 0
        print("Too Far Up")
    
    # Draw all the sprites
    all_sprites_list.draw(screen)

    #display score
    text = font.render("Score: " + str(score),True,BLACK)
    screen.blit(text, [0, 0])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
