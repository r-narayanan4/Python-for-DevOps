# Example 1: Finding the area of a circle using instance methods.

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Initialize the radius attribute of the Circle instance.

    def area(self):
        return 3.14 * self.radius ** 2  # Calculate and return the area of the circle using the instance's radius.

circle1 = Circle(5)  # Create a Circle instance with radius 5.
print(circle1.area())  # Print the area of circle1.
