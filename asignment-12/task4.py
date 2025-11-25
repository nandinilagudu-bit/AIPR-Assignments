# Function definition
def f(x):
    return 2*x**3 + 4*x + 5

# Derivative of f(x)
def f_prime(x):
    return 6*x**2 + 4

# Check if derivative can be zero
# Solve 6x^2 + 4 = 0  →  ax^2 + bx + c
a, b, c = 6, 0, 4
discriminant = b**2 - 4*a*c

print("Checking possibility of minimum...\n")

if discriminant < 0:
    print("No real value of x where f'(x) = 0.")
    print("So, f(x) is strictly increasing and has no finite minimum in real numbers.\n")

else:
    # (This case won't occur but included for academic completeness)
    import math
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Critical points:", x1, x2)
