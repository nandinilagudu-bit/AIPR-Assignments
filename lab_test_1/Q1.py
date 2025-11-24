"""Simple Fibonacci utilities and a CLI prompt that only accepts positive integers.

Usage (interactive):
    python fibonacci.py

This will prompt: "How many Fibonacci numbers would you like? "
and print the first n Fibonacci numbers (starting with 0).

The module also exposes:
    - compute_fib(n): returns a list of first n Fibonacci numbers
    - nth_fibonacci(n): returns the nth Fibonacci number (1-based)
    - get_positive_int(prompt): prompts until a positive integer is entered
"""

from typing import List


def get_positive_int(prompt: str = "Enter a positive integer: ") -> int:
    """Prompt the user until they provide a positive integer (> 0).

    Returns:
        int: the positive integer entered by the user.
    """
    while True:
        try:
            s = input(prompt).strip()
            if s == "":
                print("Input cannot be empty. Try again.")
                continue
            value = int(s)
            if value <= 0:
                print("Please enter a positive integer greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def compute_fib(n: int) -> List[int]:
    """Return a list with the first n Fibonacci numbers starting from 0.

    Args:
        n (int): number of terms to generate (must be positive).

    Raises:
        ValueError: if n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def nth_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (1-based indexing).

    Example: nth_fibonacci(1) == 0, nth_fibonacci(2) == 1
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    try:
        n = get_positive_int("How many Fibonacci numbers would you like? ")
        seq = compute_fib(n)
        print(f"Fibonacci sequence (first {n} terms):")
        print(", ".join(str(x) for x in seq))
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled. Exiting.")
