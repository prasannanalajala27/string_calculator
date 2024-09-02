import unittest
from calculator import add


# Testcase to test functionality of string calculator
class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)


if __name__ == "__main__":
    unittest.main()
