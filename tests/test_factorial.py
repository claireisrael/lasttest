import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assert_equal(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assert_equal(factorial(1), 1)

    def test_factorial_of_positive_interger(self):
        self.assert_equal(factorial(5), 120)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == '__main__':
    unittest.main()
    