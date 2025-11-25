def linear_search(lst, target):
    """Return index of target in lst, or -1 if not found."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# --- user input part ---
# Enter list elements
raw = input("Enter list elements separated by spaces: ")
# convert to integers; use .split() to get each number
lst = [int(x) for x in raw.split()]

# Enter value to search
target = int(input("Enter value to search for: "))

# Call linear_search
index = linear_search(lst, target)

# Show result
if index != -1:
    print(f"Value {target} found at index {index}")
else:
    print(f"Value {target} not found in the list")