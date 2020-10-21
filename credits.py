import pygame
import colors
from config import *

credits_title = TITLE_FONT.render("Credits :", True, colors.shady_pink)
developed_text = VS_FONT.render("Game Developed by : Vaibhav Kumar", True, colors.bright_yellow)
sounds_text = VS_FONT.render("Sounds from : Zapsplat.com", True, colors.cream)
tool_text = VS_FONT.render("Made with Pygame!", True, colors.earth_green)
escape_text = GAME_FONT.render("Escape : Back", False, colors.bright_yellow)
line_space = 100


def credits():
	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()
		elif(event.type == pygame.KEYUP):
			if(event.key == pygame.K_ESCAPE or event.key == pygame.K_c):
				return 0
	# event section end

	# filling the display surface
	game_display.fill(colors.black)

	# displaying the credits title
	game_display.blit(credits_title, (SCREENWIDTH // 2 - credits_title.get_width() // 2, 50))

	# drawing the seperator line
	pygame.draw.line(game_display, colors.white, (0 + 275, 150), (SCREENWIDTH - 275, 150))

	# displaying the credits text(s)
	game_display.blit(developed_text, (SCREENWIDTH // 2 - developed_text.get_width() // 2, 200))
	game_display.blit(sounds_text, (SCREENWIDTH // 2 - sounds_text.get_width() // 2, 200 + line_space))
	game_display.blit(tool_text, (SCREENWIDTH // 2 - tool_text.get_width() // 2, 200 + 2 * line_space))

	# displaying the escape text
	game_display.blit(escape_text, (SCREENWIDTH // 2 - escape_text.get_width() // 2, SCREENHEIGHT - escape_text.get_height() - 20))

	return 3
