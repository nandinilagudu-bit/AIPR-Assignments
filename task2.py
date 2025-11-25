import re
from typing import List, Union

# task2.py
# Bubble Sort with user input and verification


Number = Union[int, float]


def bubble_sort(arr: List[Number]) -> List[Number]:
    """In-place bubble sort (stable). Returns the sorted list."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def is_sorted(arr: List[Number]) -> bool:
    """Check if array is sorted in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def parse_number(token: str) -> Number:
    """Try to parse token as int, then float."""
    token = token.strip()
    if token == "":
        raise ValueError("Empty token")
    try:
        return int(token)
    except ValueError:
        return float(token)


def read_number_list(prompt: str = "Enter numbers (separated by spaces or commas): ") -> List[Number]:
    s = input(prompt).strip()
    if not s:
        return []
    tokens = re.split(r"[,\s]+", s)
    return [parse_number(t) for t in tokens]


def user_input_bubble_sort():
    arr = read_number_list()
    print("Original:", arr)
    sorted_arr = bubble_sort(arr.copy())
    print("Sorted:  ", sorted_arr)
    print("Verified sorted:" , is_sorted(sorted_arr))


if __name__ == "__main__":
    user_input_bubble_sort()