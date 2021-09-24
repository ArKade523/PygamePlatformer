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

# creating a class for a player
class Player(pygame.sprite.Sprite):
    # initialization function
    def __init__(self):
        super(Player, self).__init__()

        # assigns the player model to 'character', which is defined later to be an image sprite
        self.surf = character

        # cuts out any white in the png file of the sprite
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
# initialize pygame
pygame.init()

# creates the screen with our previously defined height and width
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# turns the character into a format that pygame can read
character = pygame.image.load("sprites\character.png").convert()
character = pygame.transform.scale(character, (54, 69))

# creates the player as an instance of the Player class
player = Player()

# creates a group of pygame sprites to be run together later
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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
                running = False
            
            # checks for the window being closed
            # without this code, closing the window does not close the game
            if event.type == QUIT:
                running = False

    # makes the screen the color of the sky
    screen.fill((135, 206, 250))

    # draws all entities in all_sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # updates the screen and clears old drawings
    pygame.display.flip()

# ends the program
pygame.quit()