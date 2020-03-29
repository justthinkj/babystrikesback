import pygame
import sys
from pygame.sprite import Group, Sprite

class Raindrop(Sprite):
	"""Define raindrop."""

	def __init__(self, screen):
		"""Initialize raindrop."""
		super(Raindrop, self).__init__()
		self.screen = screen

		self.image = pygame.image.load("../../images/boogie.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def blitme(self):
		"""Draw."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Update location."""
		self.x += 1
		self.rect.x = self.x


def run_game():
	pygame.init()
	
	screen = pygame.display.set_mode((1200, 500))
	pygame.display.set_caption("Raindrops")

	#raindrop = Raindrop(screen)
	raindrops = Group()
	
	num_rd_x = 2
	for i in range(num_rd_x):
		raindrop = Raindrop(screen)
		raindrop.x = raindrop.rect.width + i*2*raindrop.rect.width
		raindrop.rect.x = raindrop.x
		raindrops.add(raindrop)
	
	while True:
		screen.fill((255,255,255))

		# pygame.event.get() is required to start the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		for rd in raindrops:
			rd.blitme()

		for rd in raindrops:
			rd.update()
			
		#raindrop.blitme()
		pygame.display.flip()


run_game()

