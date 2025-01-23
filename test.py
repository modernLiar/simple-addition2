import unittest
from add import add  # Import the add function from your program

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Test adding two positive numbers

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)  # Test adding two negative numbers

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)  # Test adding a negative and a positive number

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)  # Test adding zero to a number

if __name__ == '__main__':
    unittest.main()