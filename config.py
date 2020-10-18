import pygame
import sys

pygame.init()

# configuration variables
SCREENWIDTH = 1280
SCREENHEIGHT = 600
FPS = 60

# font
GAME_FONT = pygame.font.SysFont("comicsans", 50)


# important functions
def QUIT():
	pygame.quit()
	sys.exit()


# creating the display surface
game_display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# setting the display window caption
pygame.display.set_caption("Green vs Red!")
