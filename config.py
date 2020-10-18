import pygame
import sys

pygame.init()

# configuration variables
SCREENWIDTH = 1280
SCREENHEIGHT = 600
FPS = 60


# important functions
def QUIT():
	pygame.quit()
	sys.exit()


# creating the display surface
game_display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# setting the display window caption
pygame.display.set_caption("Green vs Red!")
