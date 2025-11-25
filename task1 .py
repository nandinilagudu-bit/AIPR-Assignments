import math

def calculate_area(shape, *dimensions):
    shape = shape.lower()

    area_formulas = {
        "rectangle": lambda x, y: x * y,
        "square": lambda x: x * x,
        "circle": lambda r: math.pi * r * r
    }

    if shape not in area_formulas:
        raise ValueError("Unsupported shape.")

    return area_formulas[shape](*dimensions)


# ---- Testing output ----
print("Rectangle area (4 x 6):", calculate_area("rectangle", 4, 6))
print("Square area (side = 5):", calculate_area("square", 5))
print("Circle area (radius = 3):", round(calculate_area("circle", 3), 2))
