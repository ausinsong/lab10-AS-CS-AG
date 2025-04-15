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
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 0) == 0
        assert calculator.subtract(-2, -4) == 2

    def test_divide_by_zero(self):
        try:
            calculator.divide(0, 10)
            print("test_divide_by_zero FAILED (no exception)")
        except ZeroDivisionError:
            print("test_divide_by_zero passed")

    def test_logarithm(self):
        assert math.isclose(calculator.logarithm(2, 8), 3)
        assert math.isclose(calculator.logarithm(10, 100), 2)

    def test_log_invalid_base(self):
        for a, b in [(1, 10), (-2, 10), (2, -10)]:
            try:
                calculator.log(a, b)
                print(f"test_log_invalid_base FAILED (a={a}, b={b})")
            except ValueError:
                print(f"test_log_invalid_base passed (a={a}, b={b})")

    def run_all_tests(self):
        try:
            add(self, add)
            print("test_add passed")
        except AssertionError:
            print("test_add FAILED")

        try:
            subtract(self, subtract)
            print("test_subtract passed")
        except AssertionError:
            print("test_subtract FAILED")


        try:
            logarithm(self, logarithm)
            print("test_logarithm passed")
        except AssertionError:
            print("test_logarithm FAILED")

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(20, 2), 10)


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