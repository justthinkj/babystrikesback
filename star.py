import pygame
from random import randint

class Star():
    """Define ship."""
    
    def __init__(self, 
                 ai_settings, 
                 screen,
                 ship,
                 shipSide):
        """Initialize the star and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/pan.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new star at the top left corner of the screen
        #self.rect.left = self.screen_rect.left
        #self.rect.top = self.screen_rect.top

        # Available space for star to appear
        self.max_x = \
            ai_settings.screen_width - shipSide.rect.width - self.rect.width
        self.max_y = \
            ai_settings.screen_height - ship.rect.height - self.rect.height
        
        # Timer to change location
        self.timer = 0
        self.timeout = ai_settings.star_timeout

        self.randomize()


    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)


    def randomize(self):
        """Randomize star location."""
        self.rect.x = randint(0, self.max_x)
        self.rect.y = randint(0, self.max_y)


    def update(self):
        """Update star location randomly."""
        if self.timer < self.timeout:
            self.timer += 1
        elif self.timer == self.timeout:
            self.randomize()
            self.timer = 0
        else:
            print("Unexpected timer value")
