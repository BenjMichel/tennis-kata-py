Score = ['love', 'fifteen', 'thirty', 'forty']

class ScoreError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Game(object):
	"""a Tennis Game between two players: A and B"""
	def __init__(self):
		self.score_A = 0
		self.score_B = 0

	def increase_score_player_A(self):
		if (self.score_A > 3 and self.score_A - self.score_B >= 2):
			raise ScoreError('this score is impossible to reach')
		self.score_A += 1

	def increase_score_player_B(self):
		if (self.score_B > 3 and self.score_B - self.score_A >= 2):
			raise ScoreError('this score is impossible to reach')
		self.score_B += 1

	def get_score(self):
		if (self.score_A <= 3 and self.score_B <= 3
			and not(self.score_A == 3 and self.score_B == 3)):
			return Score[self.score_A] + " - " + Score[self.score_B]
		elif (self.score_A - self.score_B >= 2):
			return "A wins"
		elif (self.score_A - self.score_B == 1):
			return "advantage A"
		elif (self.score_A - self.score_B == 0):
			return "deuce"
		elif (self.score_A - self.score_B == -1):
			return "advantage B"
		elif (self.score_A - self.score_B <= -2):
			return "B wins"

if __name__ == '__main__':
	pass