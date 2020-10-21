import pygame
import sys

# initializing important pygame functionalities
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)

# configuration variables
SCREENWIDTH = 1280
SCREENHEIGHT = 600
FPS = 60

# font(s)
TITLE_FONT = pygame.font.SysFont("comicsans", 110)
VS_FONT = pygame.font.SysFont("comicsans", 80)
GAME_FONT = pygame.font.SysFont("comicsans", 50)


# important functions
def QUIT():
	pygame.quit()
	sys.exit()


# creating the display surface
game_display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# setting the display window caption
pygame.display.set_caption("Green vs Red!")
