# Function to calculate the sum of first n natural numbers using a for loop

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of first", n, "numbers is:", total)

# Example call
sum_to_n(10)

# Function to calculate sum of first n numbers using while loop

def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum of first", n, "numbers is:", total)

# Example call
sum_to_n_while(10)
