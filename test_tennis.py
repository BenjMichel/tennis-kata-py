import tennis
import unittest

class TestTennisGame(unittest.TestCase):
	def setUp(self):
		self.g = tennis.Game();

	def test_score_0_0(self):
		self.assertEqual(self.g.get_score(), 'love - love')

	def test_score_15_0(self):
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'fifteen - love')

	def test_score_15_15(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'fifteen - fifteen')

	def test_score_30_15(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'thirty - fifteen')

	def test_score_30_30(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'thirty - thirty')

	def test_score_40_30(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'forty - thirty')

	def test_score_deuce(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'deuce')

	def test_score_advantage_A(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'advantage A')

	def test_score_advantage_B(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'advantage B')

	def test_score_unreachable_A(self):
		try:
			self.g.increase_score_player_A()
			self.g.increase_score_player_A()
			self.g.increase_score_player_A()
			self.g.increase_score_player_A()
			self.g.increase_score_player_A()
		except tennis.ScoreError as err:
			self.assertEqual(err.value, 'this score is impossible to reach')

	def test_score_unreachable_B(self):
		try:
			self.g.increase_score_player_B()
			self.g.increase_score_player_B()
			self.g.increase_score_player_B()
			self.g.increase_score_player_B()
			self.g.increase_score_player_B()
		except tennis.ScoreError as err:
			self.assertEqual(err.value, 'this score is impossible to reach')

	def test_A_wins(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'A wins')

	def test_B_wins(self):
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'B wins')

	def test_score_100(self):
		for i in xrange(1,100):
			self.g.increase_score_player_A()
			self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'deuce')
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'advantage A')
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'advantage B')
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'B wins')

if __name__ == '__main__':
	unittest.main()