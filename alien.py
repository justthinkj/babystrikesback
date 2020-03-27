import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Define ship."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/boogie.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new alien at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.alien_speed_factor


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def update(self):
    	"""Move alines."""
    	self.x += (self.speed_factor*self.ai_settings.fleet_direction)
    	self.rect.x = self.x
    

    def check_edges(self, shipSide=""):
    	"""Return True if alien is at the edge of the screen."""
    	side_ship_length = 0 if shipSide == "" else shipSide.rect.width
    	screen_rect = self.screen_rect

    	if self.rect.right >= (screen_rect.right - side_ship_length):
    		return True
    	elif self.rect.left <= 0:
    		return True
    	else:
    		return False

