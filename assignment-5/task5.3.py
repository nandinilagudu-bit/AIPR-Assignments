# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    
    # Base case: if n is 1, return 1
    elif n == 1:
        return 1
    
    # Recursive case: sum of the two previous Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
num = 6
print(f"The {num}th Fibonacci number is:", fibonacci(num))
