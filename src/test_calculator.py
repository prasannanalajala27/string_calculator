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

    def test_newlines_delimiter(self):
        self.assertEqual(add("1,2\n2,3"), 8)

    def test_custom_delimiter_semicolon(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_colon(self):
        self.assertEqual(add("//:\n1:2:3"), 6)

    def test_custom_delimiter_pipe(self):
        self.assertEqual(add("//|\n1|2|3|4"), 10)


if __name__ == "__main__":
    unittest.main()
