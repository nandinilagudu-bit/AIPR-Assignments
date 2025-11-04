

from __future__ import annotations


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a given string.
    
    Args:
        text: The input string to count vowels in.
        
    Returns:
        The number of vowels found in the string (case-insensitive).
        
    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("Python")
        1
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("")
        0
    """
    if not text:
        return 0
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    # Demonstration of the function
    test_cases = [
        "Hello",
        "Python",
        "AEIOU",
        "xyz",
        "",
        "Hello World",
        "Programming",
        "a",
        "A",
        "12345",
    ]
    
    print("=" * 60)
    print("VOWEL COUNTING FUNCTION DEMONSTRATION")
    print("=" * 60)
    for test in test_cases:
        result = count_vowels(test)
        print(f"Input: {repr(test):20} -> Output: {result}")
    print("=" * 60)

