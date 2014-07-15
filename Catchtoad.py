#-------------------------------------------------------------------------------
# Name:         Catch_The_Toad
# Purpose:      Move Mario using the arrow keys and help him catch the randomly
#               Spawning toads! Once you get all the toads you complete the level!
#               The toads start spawning faster as each level progresses.
# Author:      Shawn Gong
#
# Created:     09/07/2014
# Copyright:   (c) Shawn Gong 2014
# Licence:      No licence
#-------------------------------------------------------------------------------

import pygame, sys, random
from pygame.locals import *
from threading import Timer


#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0)
pygame.display.set_caption("Catch Toad")

#Lose Text
losFont = pygame.font.SysFont("impact", 60)
loser = losFont.render("YOU LOSE", True, (128,128,0))

#Instruction Text
insFont = pygame.font.SysFont("impact", 25)
instructions = insFont.render("Hit Enter to Continue", True, (128,128,0))

#Set up Color Constants
BLUE = (0,0,255)
BLACK = (0,0,0)


#Set up the image data structures
toadCounter = 0
NEW_TOAD = 40 #increasing this decreases speed bears spawn, decreasing increases the speed that bears spawn
TOAD_SIZE = 64
marioImage = pygame.image.load('Mario1.png').convert()
marioImage.set_colorkey(BLACK)
marioImageTwo = pygame.image.load('Mario2.png').convert()
marioImageTwo.set_colorkey(BLACK)
toadImage = pygame.image.load('Toad1.png').convert()
toadImage.set_colorkey(BLACK)
toadImageTwo = pygame.image.load('Toad2.png').convert()
toadImageTwo.set_colorkey(BLACK)
#Copy picture(S) to the directory of the program
player = pygame.Rect(300, 100, 64,64)
toads = []
for i in range(20):
    toads.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - TOAD_SIZE), random.randint(0, WINDOW_HEIGHT - TOAD_SIZE), TOAD_SIZE, TOAD_SIZE))

#Movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False


def lose():
    windowSurface.fill(BLACK)
    windowSurface.blit(loser, (100,130))
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_lose_menu = True
    while in_lose_menu:
        clock.tick(1)
        startGame = False
        in_lose_menu = False
        pygame.display.quit()
        pygame.quit()

def level_screen():
    windowSurface.fill(BLACK)
    #Next Level Text
    lvlFont = pygame.font.SysFont("impact", 40)
    lvl = lvlFont.render("Level:  " + str(level) + "  Completed", True, (100, 149, 237))
    windowSurface.blit(lvl, (50, 104))
    windowSurface.blit(instructions, (90,180))
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_start_menu = True
    while in_start_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    startGame = True
                    in_start_menu = False
                    global colisionNumber
                    colisionNumber = 0
                    toadCounter = 0
                    toads.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - TOAD_SIZE), random.randint(0, WINDOW_HEIGHT - TOAD_SIZE), TOAD_SIZE, TOAD_SIZE))
                    for i in range(20):
                        toads.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - TOAD_SIZE), random.randint(0, WINDOW_HEIGHT - TOAD_SIZE), TOAD_SIZE, TOAD_SIZE))
                    if NEW_TOAD >= 5:
                        global NEW_TOAD
                        NEW_TOAD -= 5
                    else:
                        break

#run the game loop
startGame = True
colisionNumber = 0
level = 0
while startGame:
    #check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            #keyboard variables
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_UP:
                moveUp = True
                moveDown  = False
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft = False;
            if event.key == K_RIGHT:
                moveRight = False;
            if event.key == K_UP:
                moveUp = False;
            if event.key == K_DOWN:
                moveDown = False;
    toadCounter += 1

    #add new bears

    if toadCounter >= NEW_TOAD:
        toadCounter = 0
        toads.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - TOAD_SIZE), random.randint(0, WINDOW_HEIGHT - TOAD_SIZE), TOAD_SIZE, TOAD_SIZE))

    #draw white background
    windowSurface.fill(BLACK)

    #movement speed
    MOVE_SPEED = 10

    #move player
    if moveDown and player.bottom <WINDOW_HEIGHT:
        player.top += MOVE_SPEED
    if moveUp and player.top > 0:
        player.top -= MOVE_SPEED
    if moveLeft and player.left > 0:
        player.left -= MOVE_SPEED
    if moveRight and player.right < WINDOW_WIDTH:
        player.right += MOVE_SPEED

    windowSurface.blit(marioImage, player)
    for toad in toads:
        windowSurface.blit(toadImage, toad)

    #check if player has intersected with bear

    for toad in toads[:]: #this makes a copy of the array
        if player.colliderect(toad):
            windowSurface.blit(toadImageTwo, toad)
            windowSurface.blit(marioImageTwo, player)

        def explosion():
            for toad in toads:
                if player.colliderect(toad):
                    toads.remove(toad)
                    global colisionNumber
                    colisionNumber += 1
        if player.colliderect(toad):
            t = Timer(1, explosion)
            t.start()

        scoreFont = pygame.font.SysFont("impact", 20)
        score = scoreFont.render("SCORE:" + str(colisionNumber), True, (192,192,192))
        windowSurface.blit(score, (10,10))

    if len(toads) == 0:
        global level
        level += 1
        level_screen()
    elif len(toads) >= 30:
        lose()

    #draw the window
    pygame.display.update()
    mainClock.tick(40)



pygame.display.quit()
pygame.quit()












