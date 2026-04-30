# Calculator.py

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot Divide by 0")
    else:
        return a/b

def power(a,b):
    return a**b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    else:
        return a**0.5


