import unittest
from Score import Score


class MyTestCase(unittest.TestCase):
    def test_total_score_of_first_frame(self):
        self.assertTrue(20,Score.Total_score(10,10))
    def test_total_score_of_second_frame(self):
        self.assertTrue(31,Score.Total_score(10,1))
    def test_total_score_of_third_frame(self):
        self.assertTrue(33,Score.Total_score(1,1))
if __name__ == '__main__':
    unittest.main()

