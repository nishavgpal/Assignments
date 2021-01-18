import unittest
from Score import Score


class MyTestCase(unittest.TestCase):
    def test_total_score_of_a_frame(self):
        self.assertTrue(100, Score.Total_score(self))


if __name__ == '__main__':
    unittest.main()
