class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the games's static settings."""
        # Screen settings
        self.screen_width = 640 #1200
        self.screen_height = 480 #500
        self.bg_color = (0,0,0)

        # Ship settings
        self.ships_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # TIY 12.5
        # Side bullet settings
        self.bullet_side_color = (100,100,100)
        self.bullets_side_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.fleet_spacing_factor_x = 2
        self.fleet_spacing_factor_y = 2

        # How quickly the game speed up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase for each level
        self.score_scale = 1.5

        # TIY 13.2
        self.star_timeout = 60

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.bullet_side_speed_factor = 3
        self.alien_speed_factor = 1
        self.star_timeout = 60

        # fleet_direction: 
        # 1 = right
        # -1 = left
        self.fleet_direction = 1

        # Score
        self.alien_points = 50
        

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.bullet_side_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        # Round the point to 10
        self.alien_points = int(round((self.alien_points * self.score_scale), -1))
