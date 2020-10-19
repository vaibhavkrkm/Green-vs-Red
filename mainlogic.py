import pygame
import random
import colors
import math
from advanced_math import *
from config import *
from Red import *
from Green import Green
from Bullet import Bullet

# user events
RED_SPAWN = pygame.USEREVENT
pygame.time.set_timer(RED_SPAWN, 1000)

# game variables
red_list = []
del_red_list = []

green_list = []
del_green_list = []

bullets = []
del_bullets = []

life = 10
life_text = GAME_FONT.render(f"Lives : {life}", True, colors.shady_red)


def spawn_red():
	red_x = random.randint(Red.position_range_x[0], Red.position_range_x[1])
	red_y = random.randint(Red.position_range_y[0], Red.position_range_y[1])
	red_vel_x = random.randint(Red.velocity_range_x[0], Red.velocity_range_x[1])
	red_vel_y = random.randint(Red.velocity_range_y[0], Red.velocity_range_y[1])
	current_red = Red(Vector2(red_x, red_y), Vector2(red_vel_x, red_vel_y))
	red_list.append(current_red)


def mainloop():
	global life_text, life

	# event section start
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			QUIT()
		if(event.type == RED_SPAWN):
			spawn_red()
		if(event.type == pygame.MOUSEBUTTONUP):
			if(event.button == 1):
				if(Point.make_point_from_seq(event.pos).x < SCREENWIDTH // 2):
					# spawning the green object
					new_green = Green.spawn_green(Vector2(*event.pos))
					green_list.append(new_green)
			elif(event.button == 3):
				for i, GREEN in enumerate(green_list):
					clicked_point = Point.make_point_from_seq(event.pos)
					green_pos = GREEN.position
					green_radius = GREEN.size
					distance = math.sqrt((green_pos.y - clicked_point.y)**2 + (green_pos.x - clicked_point.x)**2)
					if(distance < green_radius):
						# despawning the green object
						del_green_list.append(i)
						break

	# filling the game display surface
	game_display.fill(colors.black)

	# displaying the text(s)
	game_display.blit(life_text, (20, 20))

	# for loop for managing red objects
	for i, RED in enumerate(red_list):
		RED.draw(game_display)
		RED.move()
		is_destroyed = RED.constraints()
		if(is_destroyed == True):
			del_red_list.append(i)
		elif(is_destroyed == "lose-life"):
			del_red_list.append(i)
			life -= 1
			life_text = GAME_FONT.render(f"Lives : {life}", True, colors.shady_red)

	# for loop for checking if a bullet is colliding with any of the red objects
	for i, RED in enumerate(red_list):
		is_destroyed, bullet_index = RED.collide_with_bullet(bullets)
		if(is_destroyed):
			del_red_list.append(i)
			del_bullets.append(bullet_index)

	# for loop for despawning red objects if they are out of range
	for DEL_RED in del_red_list:
		try:
			del red_list[DEL_RED]
		except IndexError:
			pass

	# clearing the del_red_list
	del_red_list.clear()

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
		try:
			del bullets[DEL_BULLET]
		except IndexError:
			pass

	# clearing the del_bullets list
	del_bullets.clear()

	# for loop for managing green objects
	for i, GREEN in enumerate(green_list):
		GREEN.draw(game_display)
		bullet_result = GREEN.bullet_events()
		if(bullet_result is not None):
			bullets.append(bullet_result)
		else:
			pass
		is_destroyed = GREEN.collide_with_red(red_list)
		if(is_destroyed):
			del_green_list.append(i)

	# for loop for despawning green objects if they collide with the red objects
	for DEL_GREEN in del_green_list:
		try:
			del green_list[DEL_GREEN]
		except IndexError:
			pass

	# clearing the green list
	del_green_list.clear()

	# checking the life
	if(life <= 0):
		print("Gameover!")
