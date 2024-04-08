# Example 2: Using static methods to add two numbers

class Math:
    # Define a static method named "add_numbers" that takes two parameters "x" and "y"
    @staticmethod
    def add_numbers(x, y):
        # Returns the sum of the two numbers
        return x + y

# Create an instance of the Math class and call the "add_numbers" method, passing in two arguments
print(Math.add_numbers(2, 3))
