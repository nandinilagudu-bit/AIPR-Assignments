#AI inserted try–except for safe handling.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
print(divide(10, 2))   # normal case
print(divide(5, 0))    # division by zero case