def factorial(n):
    """Return factorial of n using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Calls as requested
    print(f"Input: 5 → Output: Factorial = {factorial(5)}")
    print(f"Input: 0 → Output: Factorial = {factorial(0)}")
