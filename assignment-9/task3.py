"""
calculator_module.py

A small calculator module providing basic arithmetic operations.

Manual module-level note:
This module implements add, subtract, multiply, divide functions that accept two numbers.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First addend.
    b : float
        Second addend.

    Returns
    -------
    float
        Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract two numbers.
    Parameters
    ----------
    a : float
        Minuend.
    b : float
        Subtrahend.
    Returns
    -------
    float
        Difference a - b.
    """
    return a - b
def multiply(a, b):
    """
    Multiply two numbers.
    Parameters
    ----------
    a : float
        First factor.
    b : float
        Second factor.
    Returns
    -------
    float
        Product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        Quotient a / b.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

# Example usage
if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))

"""
Calculator Module (AI-generated)

Provides four basic arithmetic functions: add, subtract, multiply, divide.

Usage examples:
    >>> from calculator_module import add, divide
    >>> add(3, 4)
    7
    >>> divide(10, 2)
    5.0

Notes:
- Functions accept numeric inputs (int or float).
- divide raises ZeroDivisionError on division by zero.
"""

def add(a, b):
    """Return the arithmetic sum of a and b.
    Accepts integers or floats and returns their sum as a numeric type.
    """
    return a + b
def subtract(a, b):
    """Return the result of subtracting b from a.
    Works with integers and floats; preserves numeric type where possible.
    """
    return a - b
def multiply(a, b):
    """Return the product of a and b.
    Handles integer and floating point multiplication.
    """
    return a * b
def divide(a, b):
    """Return a / b, raising ZeroDivisionError when b == 0.
    Example:
        >>> divide(9, 3)
        3.0
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
