# https://github.com/ausinsong/lab10-AS-CS-AG.git
# Partner 1: Andrew Gendy
# Partner 2: Austin
# partner 3: Caden Shiver
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Square root of a negative number is not allowed")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):  # Renamed from multiply
    return a * b

def div(a, b):  # Renamed from divide
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exp(a, b):  # Renamed from exponent
    return a ** b