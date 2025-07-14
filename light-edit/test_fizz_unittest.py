import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")
        self.assertEqual(fizzbuzz(9), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")
        self.assertEqual(fizzbuzz(20), "buzz")

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz(15), "fizz buzz")
        self.assertEqual(fizzbuzz(30), "fizz buzz")
        self.assertEqual(fizzbuzz(45), "fizz buzz")

    def test_other_numbers(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(fizzbuzz(17), 17)


if __name__ == '__main__':
    unittest.main()