def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")


# Call the function with different inputs
print("Python Output:")
check_number(-5)
check_number(0)
check_number(7)
