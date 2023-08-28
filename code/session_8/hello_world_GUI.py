# Author: Al Sweigart (2012): Making Games with Python & Pygame
# Adapted by Qi Yu: Added detailed comments

import pygame, sys
from pygame.locals import * # import * : import everything from pygame.locals

# ----- 1. pygame.init(): Initialize all imported pygame modules -----
# This line always needs to be called after importing the pygame module
# and before calling any other Pygame function
pygame.init()

# ----- 2. Drawing the window -----
# It returns a Surface object, or the so-called "display Surface".
# (400, 300): a tuple defining the width and height of the window (unit: pixels)
DISPLAYSURF = pygame.display.set_mode((400, 300)) # store the object to a variable DISPLAYSURF

# ----- 3. Set the caption of the window -----
pygame.display.set_caption('My first GUI!')

# ----- 4. The main game loop -----
# See a good illustration of game loop in Swiegart (2012),
# chapter "Game Loops and Game States"
while True:
    # ----- The following line handles the evens of the user: -----
    # Actions of users, such as pressing keys or moving mouses, are recorded.
    # The pygame.event.get() function gets all actions (events).
    # You can uncomment the line "print(event)" to see this.
    for event in pygame.event.get():
        print(event)

        # ----- The following line checks if the type of event is equal to QUIT. -----
        if event.type == QUIT:
            pygame.quit() # Deactivate pygame module
            sys.exit() # This is used to terminate the program and exit from it
        # See Sweigart (2012): ALWAYS call pygame.quit() before sys.exit() !!

    # ----- Draws the object returned by pygame.display.set_mode(): -----
    # When the following line is called,
    # everything drawn on the Surface object will be displayed on the window.
    # It is not relevant in this script, as we are not drawing new stuffs.
    pygame.display.update()