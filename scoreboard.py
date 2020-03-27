import pygame.font
from pygame.sprite import Group

from bottle import Bottle

class Scoreboard():
	"""Scoreboard class to report scoring information."""

	def __init__(self, ai_settings, screen, stats):
		"""Initialize scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# Font settings for scoring information.
		self.text_color = (100, 100, 100)
		self.font = pygame.font.SysFont(None, 24, True, False)

		# Prepare the initial score image
		# self.prep_score(stats.score)


	def prep_score(self, scoretype):
		"""Ture msg into a rendered image and center text on the button."""
		if scoretype == "score":
			
			score_str = "{:,}".format(self.stats.score)		
			self.score_image = self.font.render(
				'Score: '+score_str, 
				True,
				self.text_color)
			self.score_image_rect = self.score_image.get_rect()
			self.score_image_rect.top = 10
			self.score_image_rect.right = self.screen_rect.right - 10

		elif scoretype == "highscore":

			highscore_str = "{:,}".format(self.stats.high_score)		
			self.highscore_image = self.font.render(
				'High Score: '+highscore_str, 
				True,
				self.text_color)
			self.highscore_image_rect = self.highscore_image.get_rect()
			self.highscore_image_rect.y = 10
			self.highscore_image_rect.centerx = self.screen_rect.centerx + 100	

		elif scoretype == "alltimehighscore":

			alltimehighscore_str = "{:,}".format(self.stats.all_time_high_score)		
			self.alltimehighscore_image = self.font.render(
				'All Time High: '+alltimehighscore_str, 
				True,
				self.text_color)
			self.alltimehighscore_image_rect = self.alltimehighscore_image.get_rect()
			self.alltimehighscore_image_rect.y = 10
			self.alltimehighscore_image_rect.centerx \
				= self.screen_rect.centerx - 120	

		elif scoretype == "level":
			level_str = "LEVEL " + str(self.stats.level)		
			self.level_image = self.font.render(
				level_str, 
				True,
				self.text_color)
			self.level_image_rect = self.level_image.get_rect()
			self.level_image_rect.y = 30
			self.level_image_rect.centerx = self.screen_rect.centerx

		else:
			raise ValueError("Unsupported type"+str(scoretype))


	def prep_ship(self):
		"""Show the number of ships left."""
		self.bottles = Group()

		for s in range(self.stats.ships_left):
			bottle = Bottle(self.ai_settings, self.screen)
			bottle.rect.x = 10 + s*bottle.rect.width
			bottle.rect.y = 10
			self.bottles.add(bottle)


	def blitme(self):
		"""Draw score onto screen."""
		self.prep_score("score")
		self.prep_score("highscore")
		self.prep_score("alltimehighscore")
		self.prep_score("level")
		self.prep_ship()

		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.highscore_image, self.highscore_image_rect)
		self.screen.blit(
			self.alltimehighscore_image, 
			self.alltimehighscore_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.bottles.draw(self.screen)
