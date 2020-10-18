import pygame
import colors
import math
from advanced_math import *
from config import *
from Bullet import Bullet


class Green:
	size = 20
	cooldown = 1000

	def __init__(self, position):
		self.position = position
		self.inital_ticks = pygame.time.get_ticks()
		self.final_ticks = self.inital_ticks

	def draw(self, surface):
		"""
		Draws the green object on a surface
		:param surface: Surface
		:return: None
		"""
		pygame.draw.circle(surface, colors.earth_green, self.position.to_tuple(), Green.size)

	def bullet_events(self):
		"""
		Used to trigger bullet events for a green object
		:return: Bullet or None
		"""
		self.final_ticks = pygame.time.get_ticks()
		if(self.final_ticks - self.inital_ticks >= Green.cooldown):
			self.inital_ticks = self.final_ticks
			return Bullet(Vector2(self.position.x, self.position.y - Bullet.height // 2))
		else:
			return None

	def collide_with_red(self, red_list):
		for RED in red_list:
			if(math.sqrt((RED.position.x - self.position.x) ** 2 + (RED.position.y - self.position.y) ** 2) < Green.size * 2):
				return True
		else:
			return False

	@staticmethod
	def spawn_green(pos):
		return Green(pos)
