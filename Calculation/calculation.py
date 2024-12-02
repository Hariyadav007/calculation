import math

# Addition
def addition(a, b):
    return a + b

# Multiplication
def multiplication(a, b):
    return a * b

# Sin and Cos Calculation
def calculate_sin_cos(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return math.sin(angle_radians), math.cos(angle_radians)

# Distance between two points
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Additional functions for extended functionality
# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Area of a Circle
def area_of_circle(radius):
    return math.pi * radius ** 2