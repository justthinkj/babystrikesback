import pygame
from pygame.sprite import Sprite

class BulletSide(Sprite):
	"""A class to manage bullets fired from the side ship."""

	def __init__(self, ai_settings, screen, shipSide):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = screen

		# Create a bullet rect at (0,0) and then set correct position.
		self.rect = pygame.Rect(0, 0, 
			ai_settings.bullet_height, ai_settings.bullet_width)
		self.rect.centery = shipSide.rect.centery
		self.rect.left = shipSide.rect.left

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

		self.color = ai_settings.bullet_side_color
		self.speed_factor = ai_settings.bullet_side_speed_factor


	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.x -= self.speed_factor

		# Update rect position
		self.rect.x = self.x


	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)