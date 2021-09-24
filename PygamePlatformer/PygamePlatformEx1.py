# This is the start of my platformer game made with pygame

# importing the pygame and random modules
import pygame
from pygame.locals import *
import random

# this allows me to use my keyboard with pygame
# it also allows me to quit the game
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# setting the screen width and height
# they are capitalized because they do not change
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 800

# initialize pygame
pygame.init()

# creates the screen with our previously defined height and width
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# sets the running variable to true
# while running is true, the game runs
running = True

# main game loop
while running:

    # checks for pygame events
    for event in pygame.event.get():
        # checks for keys being pressed down
        if event.type == KEYDOWN:
            # if the escape button is pressed, the game closes
            if event.key == K_ESCAPE:
                pygame.quit()
            
        # checks for the window being closed
        # without this code, closing the window does not close the game
        if event.type == QUIT:
            running = False

    # makes the screen the color of the sky
    screen.fill((135, 206, 250))

    # updates the screen and clears old drawings
    pygame.display.flip()

# ends the program
pygame.quit()