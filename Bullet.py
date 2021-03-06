import pygame
import colors
from advanced_math import *
from config import *


class Bullet:
	speed = 30
	width = 25
	height = 5

	def __init__(self, position):
		self.position = position
		self.rect = pygame.Rect(*Vector2.to_tuple(position), Bullet.width, Bullet.height)

	def __repr__(self):
		return f"({self.position.x})"

	def draw(self, surface):
		self.rect = pygame.draw.rect(surface, colors.really_blue, (*self.position.to_tuple(), Bullet.width, Bullet.height))

	def move(self):
		"""
		Moves the x position of the bullet to the right side
		:return: None
		"""
		self.position.x += Bullet.speed

	def constraints(self):
		"""
		Method to check if the bullet is out of range or not
		:return: bool
		"""
		if(self.position.x > SCREENWIDTH + Bullet.width):
			return True
		else:
			return False
