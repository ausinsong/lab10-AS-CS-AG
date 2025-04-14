import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    #def test_add(self): # 3 assertions
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
import calculator
import math
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

    def test_subtract():
        assert calculator.sub(5, 3) == 2
        assert calculator.sub(0, 0) == 0
        assert calculator.sub(-2, -4) == 2

    def test_divide_by_zero():
        try:
            calculator.div(0, 10)
            print("test_divide_by_zero FAILED (no exception)")
        except ZeroDivisionError:
            print("test_divide_by_zero passed")

    def test_logarithm():
        assert math.isclose(calculator.log(2, 8), 3)
        assert math.isclose(calculator.log(10, 100), 2)

    def test_log_invalid_base():
        for a, b in [(1, 10), (-2, 10), (2, -10)]:
            try:
                calculator.log(a, b)
                print(f"test_log_invalid_base FAILED (a={a}, b={b})")
            except ValueError:
                print(f"test_log_invalid_base passed (a={a}, b={b})")

    def run_all_tests():
        try:
            test_add()
            print("test_add passed")
        except AssertionError:
            print("test_add FAILED")

        try:
            test_subtract()
            print("test_subtract passed")
        except AssertionError:
            print("test_subtract FAILED")

        test_divide_by_zero()

        try:
            test_logarithm()
            print("test_logarithm passed")
        except AssertionError:
            print("test_logarithm FAILED")

        test_log_invalid_base()


if __name__ == "__main__":
    unittest.main()