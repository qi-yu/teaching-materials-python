# Author: Al Sweigart (2012): Making Games with Python & Pygame
# Adapted by Qi Yu: Added detailed comments

import pygame, sys
from pygame.locals import *

pygame.init()

# ----- 1. Set frames per second -----
# Frame rate (or refresh rate): the number of pictures that the program draws per second.
# Frame rate is measured in frames per second (FPS).
FPS = 30

# The following line initializes a Clock object:
# A pygame.time.Clock object helps make sure our program runs at a certain maximum FPS
# It ensures that our game programs don’t run too fast by putting in small pauses on each iteration of the game loop
fpsClock = pygame.time.Clock()

# ----- 2. Set up the window -----
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Animation')

# ----- 3. Set up colors to use -----
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# ----- 4. Load images and sound files -----
# It is a convention to put all images and sound files to a folder named "assets".
# This makes the project structure clearer.

## 4.1  Load image:
## Calling the  pygame.image.load() function to load an image.
## This will create another Surface object with the image drawn on it.
catImg = pygame.image.load('assets/img/cat.png')

catx = 10 # initial x coordinate (to be used later)
caty = 10 # initial y coordinate
direction = 'right' # initial moving direction

## 4.2 Load sound file:
soundObj = pygame.mixer.Sound('assets/sound/hit_sound.mp3')

# Comment out the following lines to also add a background music:
pygame.mixer.music.load('assets/sound/background.mp3')
pygame.mixer.music.play(-1, # -1: infinite loop.
                        0.0)  # 0.0: The position of the sound file to start

# ----- 5. Draw text -----
fontObj = pygame.font.Font('freesansbold.ttf', # The font to use
                           32 # font size
                           )

# Create a Surface with text.
textSurfaceObj = fontObj.render('Awesome cat!', # The text to write/render to the surface
                                True,  # The argument "antialias": if True, the characters will have smooth edges
                                       # See Swiegart (2012), section "Anti-Aliasing"
                                GREEN, # Font color
                                BLUE   # Background color
                                )
textRectObj = textSurfaceObj.get_rect() # Get the rectangular area of the text Surface
textRectObj.center = (250, 150) # Set where on the Surface to display the text


# ----- 6. The main game loop -----
while True:
    DISPLAYSURF.fill(WHITE)

    # Call the .blit() method to copy the text Surface to DISPLAYSURF.
    # "Blitting" = drawing the contents of one Surface onto another
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
            soundObj.play()

    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            soundObj.play()

    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            soundObj.play()

    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            soundObj.play()

    # ----- Use the blit() method to copy catImg to DISPLAYSURF: -----
    DISPLAYSURF.blit(
        catImg,         # the image
        (catx, caty)    # the position: the coordinate of the topleft corner of the image
    )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    # Calling the .tick() method of the Clock object initialized above:
    # !! This method should be called at the very end of the game loop !!
    # (usually after calling pygame.display.update() )
    fpsClock.tick(FPS)