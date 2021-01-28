import unittest
from BowlingGame import BowlingGame


class BowlingGameTest(unittest.TestCase):

    def test_should_not_allow_frames_greater_than_ten(self):
        result = BowlingGame.frame_score(11,1,8)
        self.assertEqual(False,result)

    def test_should_allow_frames_upto_ten(self):
        result = BowlingGame.frame_score(5,1,7)
        self.assertEqual(True,result)

    def test_should_not_allow_frames_to_have_more_than_two_chances(self):
        BowlingGame.frame_score( 1, 1, 8)
        BowlingGame.frame_score(1, 2, 1)
        result= BowlingGame.frame_score(1,3,2)
        self.assertEqual(False, result)

    def test_should_allow_frames_to_have_two_chances(self):
        BowlingGame.frame_score(2, 1, 8)
        result= BowlingGame.frame_score(2,2,1)
        self.assertEqual(True, result)

    def test_total_score_second_frame(self):
        BowlingGame.frame_score(1, 1, 8)
        BowlingGame.frame_score(1,2,1)
        BowlingGame.frame_score(2, 1, 8)
        BowlingGame.frame_score(2, 2, 2)
        self.assertTrue(19,BowlingGame.get_score(2))


    def test_should_update_spare_for_last_frame_total_score(self):
        BowlingGame.frame_score(1, 1, 1)
        BowlingGame.frame_score(1, 2, 4)
        BowlingGame.frame_score(2, 1, 4)
        BowlingGame.frame_score(2, 2, 5)
        BowlingGame.frame_score(3, 1, 6)
        BowlingGame.frame_score(3, 2, 4)
        BowlingGame.frame_score(4, 1, 5)
        BowlingGame.frame_score(4, 2, 5)
        i = 0
        for i in range(5):
            print(BowlingGame.get_score(i))
        self.assertEqual(29, BowlingGame.get_score(3))

    def test_should_update_strike_for_last_frame_total_score(self):
        BowlingGame.frame_score(1, 1, 1)
        BowlingGame.frame_score(1, 2, 4)
        BowlingGame.frame_score(2, 1, 4)
        BowlingGame.frame_score(2, 2, 5)
        BowlingGame.frame_score(3, 1, 6)
        BowlingGame.frame_score(3, 2, 4)
        BowlingGame.frame_score(4, 1, 5)
        BowlingGame.frame_score(4, 2, 5)
        BowlingGame.frame_score(5, 1, 10)
        BowlingGame.frame_score(5, 2, 0)
        BowlingGame.frame_score(6, 1, 0)
        BowlingGame.frame_score(6, 2, 1)
        i = 0
        for i in range(7):
            print(BowlingGame.get_score(i))
        self.assertEqual(60, BowlingGame.get_score(5))
"""
    def test_should_update_double_strike_for_last_frame_total_score(self):
        BowlingGame.frame_score(1, 1, 1)
        BowlingGame.frame_score(1, 2, 4)
        BowlingGame.frame_score(2, 1, 3)
        BowlingGame.frame_score(2, 2, 5)
        BowlingGame.frame_score(3, 1, 4)
        BowlingGame.frame_score(3, 2, 6)
        BowlingGame.frame_score(4, 1, 2)
        BowlingGame.frame_score(4, 2, 0)
        BowlingGame.frame_score(5, 1, 10)
        BowlingGame.frame_score(5, 2, 0)
        BowlingGame.frame_score(6, 1, 4)
        BowlingGame.frame_score(6, 2, 3)
        BowlingGame.frame_score(7, 1, 10)
        BowlingGame.frame_score(7, 2, 0)
        BowlingGame.frame_score(8, 1, 10)
        BowlingGame.frame_score(8, 2, 0)
        BowlingGame.frame_score(9, 1, 5)
        BowlingGame.frame_score(9, 2, 3)

        i = 0
        for i in range(10):
            print(BowlingGame.get_score(i))
        self.assertEqual(79, BowlingGame.get_score(7))"""

    def test_should_return_frame_total_score(self):
        BowlingGame.frame_score(1, 1, 1)
        BowlingGame.frame_score(1, 2, 4)
        BowlingGame.frame_score(2, 1, 4)
        BowlingGame.frame_score(2, 2, 5)
        BowlingGame.frame_score(3, 1, 6)
        BowlingGame.frame_score(3, 2, 4)
        BowlingGame.frame_score(4, 1, 5)
        BowlingGame.frame_score(4, 2, 5)
        BowlingGame.frame_score(5, 1, 10)
        BowlingGame.frame_score(5, 2, 0)
        BowlingGame.frame_score(6, 1, 0)
        BowlingGame.frame_score(6, 2, 1)
        BowlingGame.frame_score(7, 1, 7)
        BowlingGame.frame_score(7, 2, 3)
        BowlingGame.frame_score(8, 1, 6)
        BowlingGame.frame_score(8, 2, 4)
        BowlingGame.frame_score(9, 1, 10)
        BowlingGame.frame_score(9, 2, 0)
        BowlingGame.frame_score(10, 1, 2)
        BowlingGame.frame_score(10, 2, 3)

        i = 0
        for i in range(11):
            print(BowlingGame.get_score(i))
        self.assertEqual(117,BowlingGame.get_score(10))



if __name__ == '__main__':
    unittest.main()
