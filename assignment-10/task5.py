def divide_numbers(a, b):
    """
    Divide two numbers and handle division errors gracefully.

    This function attempts to divide 'a' by 'b'.
    If division by zero occurs, it catches the exception and
    returns a helpful error message instead of crashing.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


# Running the function
print(divide_numbers(10, 0))