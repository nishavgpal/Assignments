import unittest
from BowlingGame import BowlingGame
test_data_strike_tenth_frames = [1, 4, 5, 3, 4, 6, 2, 0, 10, 4, 3, 10, 10, 5, 3,10,5,5]



class BowlingGameTest(unittest.TestCase):

    def play_bowling_game(self):
        BowlingGame.define_variables(self)
        test_data_ten_frames = [1, 4, 5, 3, 4, 6, 2, 0, 10, 4, 3, 10, 10, 5, 3, 7, 3, 10, 1]
        for i in range(19):
            BowlingGame.score_calculator(self, test_data_ten_frames[i])



    def test_maximum_frames_allowed_as_ten(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertFalse(False, BowlingGame.score_calculator)


    def test_totalscore_as_tenth_framescore(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertEqual(122, BowlingGame.fetch_framescore(self, 10))


    def test_framescore_withspare(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertEqual(27, BowlingGame.fetch_framescore(self, 4))



    def test_framescore_withsinglestrike(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertEqual(51, BowlingGame.fetch_framescore(self, 6))


    def test_totalscore_withdoublestrike(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertEqual(122, BowlingGame.fetch_framescore(self, 10))


    def test_update_triple_strike_for_frame_total_score(self):
        BowlingGame.define_variables(self)
        for i in range(3):
            BowlingGame.score_calculator(self, 10)
        self.assertEqual(30, BowlingGame.fetch_framescore(self, 1))


    def test_update_spare_at_tenth_frame(self):
        BowlingGameTest.play_bowling_game(self)
        self.assertEqual(122, BowlingGame.fetch_framescore(self, 10))


    def test_update_strike_at_tenth_frame(self):
        BowlingGame.define_variables(self)
        for i in range(18):
            BowlingGame.score_calculator(self, test_data_strike_tenth_frames[i])
        self.assertEqual(122, BowlingGame.fetch_framescore(self, 10))


    def test_gutter_rolls_total_score_zero(self):
        BowlingGame.define_variables(self)
        for i in range(20):
            BowlingGame.score_calculator(self, 0)
        self.assertEqual(0, BowlingGame.fetch_framescore(self, 10))


    def test_all_strike_total_score(self):
        BowlingGame.define_variables(self)
        for i in range(12):
            BowlingGame.score_calculator(self, 10)
        self.assertEqual(300, BowlingGame.fetch_framescore(self, 10))


    def test_all_strike_with_maximum_allowed_only_ten_frames(self):
        BowlingGame.define_variables(self)
        for i in range(13):
            BowlingGame.score_calculator(self, 10)
        self.assertFalse(False, BowlingGame.score_calculator)


if __name__ == '__main__':
    unittest.main()
