import unittest


class MyTestCase(unittest.TestCase):
    def test_total_score_of_a_frame(self):
        self.assertTrue(100, Score.total(10,0))


if __name__ == '__main__':
    unittest.main()
