import unittest
import arithmetic_functions
import statistics_functions


class TestArithmeticFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(arithmetic_functions.add(3, 4), 7)
        self.assertEqual(arithmetic_functions.add(-2, 5), 3)

    def test_subtraction(self):
        self.assertEqual(arithmetic_functions.subtract(10, 5), 5)
        self.assertEqual(arithmetic_functions.subtract(7, 2), 5)

    def test_multiplication(self):
        self.assertEqual(arithmetic_functions.multiply(3, 4), 12)
        self.assertEqual(arithmetic_functions.multiply(-2, 5), -10)

    def test_division(self):
        self.assertEqual(arithmetic_functions.divide(10, 2), 5)
        self.assertEqual(arithmetic_functions.divide(9, 3), 3)


class TestStatisticsFunctions(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(statistics_functions.mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(statistics_functions.mean([2, 4, 6, 8, 10]), 6)

    def test_median(self):
        self.assertEqual(statistics_functions.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(statistics_functions.median([2, 4, 6, 8, 10]), 6)

    def test_mode(self):
        self.assertEqual(statistics_functions.mode([1, 2, 2, 3, 4, 4, 4, 5]), [2, 4])
        self.assertEqual(statistics_functions.mode([2, 2, 2, 3, 3, 4, 4, 5]), [2])


if __name__ == '__main__':
    unittest.main()