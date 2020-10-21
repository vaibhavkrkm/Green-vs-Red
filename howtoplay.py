import pygame
import colors
from config import *

how_to_play_title = TITLE_FONT.render("How to Play :", True, colors.bright_yellow)
how_to_play_text1 = GAME_FONT.render("Place the ranged Green units in the left side of the", False, colors.white)
how_to_play_text2 = GAME_FONT.render("battlefield such that they can protect your side from the evil Red units!", False, colors.white)
controls_title = VS_FONT.render("Controls --->", True, colors.earth_green)
spawn_text = GAME_FONT.render("Left Click - Spawn Green Unit (Costs 10 Points)", False, colors.white)
despawn_text = GAME_FONT.render("Right Click - Despawn Green Unit (Worth 5 Points)", False, colors.white)
end_game_text = GAME_FONT.render("ESC - End Game", False, colors.white)
escape_text = GAME_FONT.render("Escape : Back", False, colors.bright_yellow)
line_space = 50


def howtoplay():
	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()
		elif(event.type == pygame.KEYUP):
			if(event.key == pygame.K_ESCAPE or event.key == pygame.K_h):
				return 0
	# event section end

	# filling the display surface
	game_display.fill(colors.black)

	# displaying the how to play title
	game_display.blit(how_to_play_title, (SCREENWIDTH // 2 - how_to_play_title.get_width() // 2, 50))

	# drawing the seperator line
	pygame.draw.line(game_display, colors.white, (0 + 275, 150), (SCREENWIDTH - 275, 150))

	# displaying the how to play text(s)
	game_display.blit(how_to_play_text1, (SCREENWIDTH // 2 - how_to_play_text1.get_width() // 2, 200))
	game_display.blit(how_to_play_text2, (SCREENWIDTH // 2 - how_to_play_text2.get_width() // 2, 200 + line_space))

	# drawing the seperator line
	pygame.draw.line(game_display, colors.white, (0 + 275, 350), (SCREENWIDTH - 275, 350))

	# displaying the controls title
	game_display.blit(controls_title, (0 + 50, 425))

	# displaying the controls text(s)
	game_display.blit(spawn_text, (SCREENWIDTH - spawn_text.get_width() - 50, 375))
	game_display.blit(despawn_text, (SCREENWIDTH - despawn_text.get_width() - 50, 375 + line_space))
	game_display.blit(end_game_text, (SCREENWIDTH - end_game_text.get_width() - 50, 375 + 2 * line_space))

	# displaying the escape text
	game_display.blit(escape_text, (SCREENWIDTH // 2 - escape_text.get_width() // 2, SCREENHEIGHT - escape_text.get_height() - 20))

	return 2
