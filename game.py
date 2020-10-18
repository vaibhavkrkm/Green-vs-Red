import pygame
from config import *
import mainlogic

CLOCK = pygame.time.Clock()

run = True
while run:
	# main game logic
	mainlogic.mainloop()

	# updating the display
	pygame.display.update()

	# using the FPS
	CLOCK.tick(FPS)
