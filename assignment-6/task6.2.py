# Function to print the first 10 multiples of a number using a for loop

def print_multiples(num):
    print(f"First 10 multiples of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Example call
print_multiples(5)


# AI-generated function using while loop

def print_multiples_while(num):
    print(f"First 10 multiples of {num}:")
    i = 1
    while i <= 10:
        print(num * i)
        i += 1

# Example call
print_multiples_while(5)
