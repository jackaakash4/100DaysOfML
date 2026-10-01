"""
1. test_safe_divide_normal() — a normal division that should work correctly
2. test_safe_divide_by_zero() — division by zero, should return None
3. test_safe_divide_negative() — test it works correctly with negative numbers too

"""

def divide(a, b):
    try:    
        return a/b
    except ZeroDivisionError:
        return None

def test_safe_divide_normal():
    assert divide(10, 2) == 5.00

def test_safe_divide_by_zero():
    assert divide(10, 0) is None

def test_safe_divide_negative():
    assert divide(10, -2) == -5.00
