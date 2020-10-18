import pygame
import colors
from Bullet import Bullet
from config import *


class Red:
	size = 20
	position_range_x = [SCREENWIDTH + size, SCREENWIDTH + size + 50]
	position_range_y = [0 + size, SCREENHEIGHT - size]
	velocity_range_x = [-3, -1]
	velocity_range_y = [-1, 1]
	
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity

	def draw(self, surface):
		"""
		Draws the red object on a surface
		:param surface: Surface
		:return: None
		"""
		pygame.draw.circle(surface, colors.really_red, self.position.to_tuple(), Red.size)

	def move(self):
		"""
		Moves the current position of the red object according to the velocity
		:return: None
		"""
		self.position.x += self.velocity.x
		self.position.y += self.velocity.y

	def constraints(self):
		"""
		Method to check if the red object is out of range or not
		"""
		if(self.position.x < 0 - Red.size
		or self.position.y < 0 - Red.size
		or self.position.y > SCREENHEIGHT + Red.size):
			return True
		else:
			return False

	def collide_with_bullet(self, bullet_list):
		for i, BULLET in enumerate(bullet_list):
			if(self.position.x >= BULLET.position.x and self.position.x <= BULLET.position.x + Bullet.width):
				if(self.position.y >= BULLET.position.y - Red.size and self.position.y <= BULLET.position.y + Bullet.height + Red.size):
					return True, i
		else:
			return False, None
