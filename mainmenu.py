import pygame
from config import *
import colors

title_text_green = TITLE_FONT.render("Green", True, colors.earth_green)
title_text_red = TITLE_FONT.render("Red", True, colors.really_red)
vs_text = VS_FONT.render("vs", False, colors.cream)
start_text = GAME_FONT.render("SPACE TO BEGIN!", False, colors.bright_yellow)
how_to_play_text = GAME_FONT.render("H : How to Play", False, colors.white)
quit_text = GAME_FONT.render("ESC TO QUIT", False, colors.shady_yellow)


def mainmenu(score=0):
	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()
		elif(event.type == pygame.KEYUP):
			if(event.key == pygame.K_SPACE):
				# start game
				return 1
			elif(event.key == pygame.K_h):
				return 2
			elif(event.key == pygame.K_c):
				return 3
			elif(event.key == pygame.K_ESCAPE):
				QUIT()
	# event section end

	# filling the display surface
	game_display.fill(colors.black)

	# title of the game
	game_display.blit(title_text_green, (SCREENWIDTH // 2 - title_text_green.get_width() // 2, 50))
	game_display.blit(vs_text, (SCREENWIDTH // 2 - vs_text.get_width() // 2, 150))
	game_display.blit(title_text_red, (SCREENWIDTH // 2 - title_text_red.get_width() // 2, 250))

	# seperator line
	pygame.draw.line(game_display, colors.white, (0 + 200, 350), (SCREENWIDTH - 200, 350))

	# showing the score
	score_text = GAME_FONT.render(f"Your Score : {score}", True, colors.deep_green)
	game_display.blit(score_text, (SCREENWIDTH // 2 - score_text.get_width() // 2, 375))

	# options of the game
	game_display.blit(start_text, (SCREENWIDTH // 2 - start_text.get_width() // 2, SCREENHEIGHT - start_text.get_height() - 100))
	game_display.blit(quit_text, (SCREENWIDTH - quit_text.get_width() - 20, SCREENHEIGHT - quit_text.get_height() - 40))
	game_display.blit(how_to_play_text, (0 + 20, SCREENHEIGHT - how_to_play_text.get_height() - 40))

	return 0
