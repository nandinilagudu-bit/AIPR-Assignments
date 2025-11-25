# Optimization of Chocolate Production (No external libraries)

# Variables:
# x = units of chocolate A
# y = units of chocolate B

max_profit = 0
best_x = 0
best_y = 0

# Loop through all possible integer values within limits
for x in range(6):  # milk max = 5, so A cannot exceed 5
    for y in range(6):  # same reason for B
        # Constraints:
        if (x + y <= 5) and (3*x + 2*y <= 12):
            # Profit calculation
            profit = 6*x + 5*y

            # Check best profit
            if profit > max_profit:
                max_profit = profit
                best_x = x
                best_y = y

# Output
print("Optimal Production Plan:")
print(f"Produce {best_x} units of Chocolate A")
print(f"Produce {best_y} units of Chocolate B")
print(f"Maximum Profit: Rs {max_profit}")
