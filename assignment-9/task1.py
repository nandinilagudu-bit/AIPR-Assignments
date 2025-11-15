def sum_even_odd_ai(numbers):
    """Return the sum of even numbers and the sum of odd numbers from a list.

    The function iterates through the provided collection, sums even integers
    separately from odd integers, and returns the two sums as a tuple.

    Args:
        numbers (Iterable[int]): An iterable of integers (e.g., list, tuple).

    Returns:
        (int, int): A tuple containing (sum_of_evens, sum_of_odds).

    Raises:
        TypeError: If the input is not iterable or contains non-integer values.

    Example:
        >>> sum_even_odd_ai([1,2,3,4])
        (6, 4)
    """
    if not hasattr(numbers, '__iter__'):
        raise TypeError("numbers must be iterable of integers")
    even_sum = 0
    odd_sum = 0
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("all elements must be integers")
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum, odd_sum

def sum_even_odd(numbers):
    """Calculate sums of even and odd integers in a list.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        tuple[int, int]: A tuple (even_sum, odd_sum) where:
            even_sum: Sum of even integers in the list.
            odd_sum: Sum of odd integers in the list.

    Raises:
        TypeError: If `numbers` is not an iterable of integers.
    """
    if not hasattr(numbers, '__iter__'):
        raise TypeError("numbers must be an iterable of integers")
    even_sum = 0
    odd_sum = 0
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("all elements must be integers")
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum, odd_sum
print(sum_even_odd([1,2,3,4,5]))       # manual version
# Output: (6, 9)

print(sum_even_odd_ai([1,2,3,4,5]))    # AI docstring version (logic identical)
# Output: (6, 9)
