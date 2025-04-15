# https://github.com/ausinsong/lab10-AS-CS-AG.git
# Partner 1: Andrew Gendy
# Partner 2: Austin
# partner 3: Caden Shiver
import unittest
from calculator import *
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(0, 0), 0)
        self.assertEqual(calculator.subtract(-2, -4), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)  # Updated to div

    def test_logarithm(self):
        self.assertTrue(math.isclose(calculator.logarithm(2, 8), 3))
        self.assertTrue(math.isclose(calculator.logarithm(10, 100), 2))

    def test_log_invalid_base(self):
        for a, b in [(1, 10), (-2, 10), (2, -10)]:
            with self.assertRaises(ValueError):
                calculator.logarithm(a, b)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)  # Updated to mul
        self.assertEqual(calculator.mul(-2, 5), -10)  # Updated to mul
        self.assertEqual(calculator.mul(0, 100), 0)  # Updated to mul

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)  # Updated to div
        self.assertEqual(calculator.div(-10, 2), -5)  # Updated to div
        self.assertEqual(calculator.div(20, 2), 10)  # Updated to div

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):  # Log of negative number or zero
            logarithm(-10, 10)
        with self.assertRaises(ValueError):  # Log of zero
            logarithm(0, 10)
        with self.assertRaises(ValueError):  # Log base non-positive
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)
        self.assertRaises(ValueError, square_root, -9)  # Testing square root of a negative number

    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

    # Do not touch this

if __name__ == "__main__":
    unittest.main()