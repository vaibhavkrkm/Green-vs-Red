import pygame
from config import *
import mainlogic
import mainmenu
import howtoplay

CLOCK = pygame.time.Clock()

game_state = 0
score = 0

run = True
while run:
	if(game_state == 0):
		# setting up the cursor for mainmenu
		if(pygame.mouse.get_cursor() != pygame.cursors.arrow):
			pygame.mouse.set_cursor(*pygame.cursors.arrow)
		# main menu
		game_state = mainmenu.mainmenu(score)

	elif(game_state == 1):
		# setting the cursor for mainloop
		if(pygame.mouse.get_cursor() != pygame.cursors.diamond):
			pygame.mouse.set_cursor(*pygame.cursors.diamond)
		# main game logic
		game_state, score = mainlogic.mainloop()

	elif(game_state == 2):
		game_state = howtoplay.howtoplay()

	# updating the display
	pygame.display.update()

	# using the FPS
	CLOCK.tick(FPS)
