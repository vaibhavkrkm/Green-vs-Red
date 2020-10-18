import pygame
import random
import colors
from advanced_math import *
from config import *
from Red import Red
from Green import Green
from Bullet import Bullet

# user events
RED_SPAWN = pygame.USEREVENT
pygame.time.set_timer(RED_SPAWN, 1000)

# game variables
red_list = []
del_red_list = []
green_list = []
bullets = []
del_bullets = []

# TEMPORARY
green_list.append(Green(Vector2(200, 90)))
green_list.append(Green(Vector2(150, 200)))
green_list.append(Green(Vector2(100, 300)))
green_list.append(Green(Vector2(200, 300)))


def spawn_red():
	red_x = random.randint(Red.position_range_x[0], Red.position_range_x[1])
	red_y = random.randint(Red.position_range_y[0], Red.position_range_y[1])
	red_vel_x = random.randint(Red.velocity_range_x[0], Red.velocity_range_x[1])
	red_vel_y = random.randint(Red.velocity_range_y[0], Red.velocity_range_y[1])
	current_red = Red(Vector2(red_x, red_y), Vector2(red_vel_x, red_vel_y))
	red_list.append(current_red)


def mainloop():
	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()
		if(event.type == RED_SPAWN):
			spawn_red()

	# filling the game display surface
	game_display.fill(colors.black)

	# for loop for managing red objects
	for i, RED in enumerate(red_list):
		RED.draw(game_display)
		RED.move()
		is_destroyed = RED.constraints()
		if(is_destroyed):
			del_red_list.append(i)

	# for loop for despawning red objects if they are out of range
	for DEL_RED in del_red_list:
		del red_list[DEL_RED]

	# clearing the del_red_list
	del_red_list.clear()

	# for loop for managing green objects
	for i, GREEN in enumerate(green_list):
		GREEN.draw(game_display)
		bullet_result = GREEN.bullet_events()
		if(bullet_result is not None):
			bullets.append(bullet_result)
		else:
			pass
	# for loop for bullets
	for i, BULLET in enumerate(bullets):
		BULLET.draw(game_display)
		BULLET.move()
		is_destroyed = BULLET.constraints()
		if(is_destroyed):
			del_bullets.append(i)
			break

	# for loop for despawning bullets if they are out of range
	for DEL_BULLET in del_bullets:
		print(DEL_BULLET)
		del bullets[DEL_BULLET]

	# clearing the del_bullets list
	del_bullets.clear()
