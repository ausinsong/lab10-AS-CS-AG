# https://github.com/ausinsong/lab10-AS-CS-AG.git
# Partner 1: Andrew Gendy
# Partner 2: Austin
# partner 3: Caden Shiver
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Logarithm base must be positive")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b