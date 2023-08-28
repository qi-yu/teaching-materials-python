# Author: Al Sweigart (2012): Making Games with Python & Pygame
# Adapted by Qi Yu: Added detailed comments

import pygame, sys
from pygame.locals import *

# ----- 1. Initialize all imported pygame modules -----
pygame.init()

# ----- 2. Set up the window -----
# Initialize the Surface object (the "display surface")
DISPLAYSURF = pygame.display.set_mode((500, 400))

# Set the caption
pygame.display.set_caption('Drawing')

# ----- 3. Set up colors to use: -----
# RGB codes are used.
# (RGB = construct colors from Red, Green, Blue)
# A website to check RGB code of each color:
# https://www.rapidtables.com/web/color/RGB_Color.html

BLACK = (0, 0, 0) # Assign the RGB-value (0, 0, 0) to a variable BLACK
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ----- 4. Draw on the Surface object -----
# Fill in the entire Surface object with color WHITE defined above
DISPLAYSURF.fill(WHITE)

## 4.1 Draw a polygon
pygame.draw.polygon(
    DISPLAYSURF, # Draw on which surface?
    GREEN, # What color?
    ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)), # Coordinates of the five points?
    #1  # Width of the edges
        # Edge width is an optional argument.
        # When not defined, it will be  polygon filled by the color defined above.
)

## 4.2 Draw lines
pygame.draw.line(
    DISPLAYSURF,
    BLUE,
    (60, 60),   # coordinate of the starting point
    (120, 60),  # coordinate of the ending point
    4           # width of the line
)

pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)

## 4.3 Draw a circle
pygame.draw.circle(
    DISPLAYSURF,
    BLUE,
    (300, 50),  # center of the circle
    20,         # radius
    0           # edge width
)

## 4.4 Draw a rectangle
pygame.draw.rect(
    DISPLAYSURF,
    RED,
    (200, 150, 100, 50), # 200 and 150: coordinate of top left corner;
                         # 100: width
                         # 50: height
)

## 4.5 Draw a ellipse
pygame.draw.ellipse(
    DISPLAYSURF,
    RED,
    (300, 250, 40, 80), # The bounding rectangle of the ellipse
    1 # edge width
)


## 4.6 Draw individual pixels:
## A PixelArray object should be created for doing this.
## Creating a PixelArray object of a Surface object will “lock” the Surface object:
## the drawing functions can still be called on it,
## but it cannot have images like PNG or JPG images drawn on it.

# Create a PixelArray object:
pixObj = pygame.PixelArray(DISPLAYSURF)

# Draw some pixels:
pixObj[320][200] = BLACK
pixObj[322][202] = BLACK
pixObj[324][204] = BLACK
pixObj[326][206] = BLACK
pixObj[328][208] = BLACK

# Delete the PixelArray oblect when finished drawing pixels:
# This will "unlock" the surface again.
del pixObj

# ----- 5. The main game loop -----
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()