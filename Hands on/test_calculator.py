
import unittest
import calculator


class Test_calculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)



