#  Practical Example 1: How does the Python code structure work?





import math

a = 3.14159

def fun(name):
    """Prints a greeting message."""
    print(f"Hello",name)

def calculate_area(radius):
    """Calculates the area of a circle."""
    return a * radius ** 2

if __name__ == "__main__":
    fun("Ajay")
    radius = 5
    area = calculate_area(radius)
    print(f"The area of a circle with radius",radius,"is", area)
