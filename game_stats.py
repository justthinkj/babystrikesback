FILENAME = "all_time_high_score.txt"

class Gamestats():
	"""Track stats for game."""

	def __init__(self, ai_settings):
		"""Initialize stats."""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start game in active state
		self.game_active = False
		self.game_end = False
		# High score should never be reset
		self.high_score = 0
		self.all_time_high_score = 0
		self.read_all_time_high_score()


	def reset_stats(self):
		"""Initalize statistics that can change during the game."""
		self.score = 0
		self.ships_left = self.ai_settings.ships_limit
		self.level = 1


	def read_all_time_high_score(self):
		"""Get all time high score."""
		with open(FILENAME, "r") as file:
			contents = file.read()
			if contents:
				self.all_time_high_score = int(contents)


	def write_all_time_high_score(self):
		"""Write all time high score."""
		with open(FILENAME, "w") as file:
			file.write(str(self.all_time_high_score))
