import pygame.font

class Button():
	"""Button class."""

	def __init__(self, 
				 ai_settings, 
				 screen, 
				 msg,
				 position=(0, 0),
				 size=(200, 50)):
		"""Initialize button attribute."""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = size[0], size[1]
		self.button_color = (192, 192, 192)
		self.text_color = (255, 255, 255)

		# Not sure why pgyame.font.SysFont keeps frozen
		# adding True, False solved this issue.
		self.font = pygame.font.SysFont(None, 36, True, False)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.rect.x = self.rect.x + position[0]
		self.rect.y = self.rect.y + position[1]

		# The button message needs to be prepped only once
		self.prep_msg(msg)


	def prep_msg(self, msg):
		"""Ture msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(
			msg, 
			True,
			self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		"""Draw  blank button and then draw message."""

		# Fill the button surface with a solid color
		self.screen.fill(self.button_color, self.rect)

		# Blit -> draw many images onto another
		# Blit the text image onto button image
		self.screen.blit(self.msg_image, self.msg_image_rect)
