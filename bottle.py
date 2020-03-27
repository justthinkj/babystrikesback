import pygame
from pygame.sprite import Sprite

class Bottle(Sprite):
    """Define ship."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Bottle, self).__init__()
        self.screen = screen
        
        # Load the ship image and get it rect.
        self.image = pygame.image.load("images/bottle.bmp")
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Start each new ship at the bottom center of the screen.
        self.rect.x = 0
        self.rect.y = 0 

    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
