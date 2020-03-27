import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Define ship."""
    
    def __init__(self, ai_settings, screen, small_size=False):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen

        
        # Load the ship image and get it rect.
        self.image = pygame.image.load("images/juju.bmp")
        
        # Get smaller size ship
        if small_size:
            self.image = pygame.transform.rotozoom(
                self.image, 
                0, 
                0.75)
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        
        ## TIY-Center moving all direction
        # Start each new ship at the center of the screen
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center
        # Since rect attributes only store integer values
        self.center = float(self.rect.centerx)

        ## TIY-Center moving all direction
        # self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False

        ## TIY
        # self.moving_up = False
        # self.moving_down = False

    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to the right.
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            # Move the ship to the left.
            self.center -= self.ai_settings.ship_speed_factor
        
        ## TIY
        """
        elif self.moving_up and self.rect.top > 0:
            # Note: screen x,y coordiate start at top-left corner
            # ie. screen_rect.top = 0
            # Move the ship up
            self.centery -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # Move the ship down
            self.centery += self.ai_settings.ship_speed_factor
        """

        # Update rect object from self.center.
        self.rect.centerx = self.center

        ## TIY
        # self.rect.centery = self.centery


    def center_ship(self):
        """Center ship."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
