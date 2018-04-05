"""Main File Created by:
Jack Morris, Raghav Gupta, Jake Kautzman"""

import pygame
import game_level_library
import title_screen
import credits_screen

screen = pygame.display.set_mode([700, 400])

#Screen selector
currentScreen = 0
#0=Title 1=Game 2=Credits

#Checks if on screen
if currentScreen == 1:
    level = game_level_library.GameLevel(screen)
if currentScreen == 0:
    level = title_screen.TitleLevel(screen)
if currentScreen == 2:
    level = credits_screen.CreditsLevel(screen)

# Loops the entire main until player closes the game
done = False
         
# Screen update speed
clock = pygame.time.Clock()

# Play "One" by Cathedral Of Chemical Equilibrium
# Available from:
# http://freemusicarchive.org/music/Cathedral_Of_Chemical_Equilibrium/Sonic_Action/One_1260


#player movement speed
SPEED = 2

#player movement arrays
horMoveArray = [False, False]
vertMoveArray = [False, False]

#---------------------------Game Loop------------------------------#
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
        
        #Player key bindings
        #Game Screen    
        elif (currentScreen == 1): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    horMoveArray[0] = True
                elif event.key == pygame.K_RIGHT:
                    horMoveArray[1] = True
                elif event.key == pygame.K_UP:
                    vertMoveArray[0] = True
                elif event.key == pygame.K_DOWN:
                    vertMoveArray[1] = True
                if event.key == pygame.K_RETURN:
                    currentScreen = 0
                    level = title_screen.TitleLevel(screen)
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    horMoveArray[0] = False
                elif event.key == pygame.K_RIGHT:
                    horMoveArray[1] = False
                elif event.key == pygame.K_UP:
                    vertMoveArray[0] = False
                elif event.key == pygame.K_DOWN:
                    vertMoveArray[1] = False
        #Title Screen
        elif (currentScreen == 0):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    currentScreen = 1
                    level = game_level_library.GameLevel(screen)
                if event.key == pygame.K_c:
                    currentScreen = 2
                    level = credits_screen.CreditsLevel(screen)
        #Credits Screen
        elif (currentScreen == 2):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    currentScreen = 0
                    level = title_screen.TitleLevel(screen)

                          
    #Player movement if on gameScreen              
    if (currentScreen == 1):      
        xSpeed = (SPEED*horMoveArray[1])-(SPEED*horMoveArray[0])
        ySpeed = (SPEED*vertMoveArray[1])-(SPEED*vertMoveArray[0])
        level.update(xSpeed, ySpeed)

    if (currentScreen == 0 or currentScreen == 2):
        level.update()
            
    
    clock.tick(60) 
pygame.quit()
