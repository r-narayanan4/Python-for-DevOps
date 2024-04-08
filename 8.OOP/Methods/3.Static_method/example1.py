# Example 1: Using static methods to perform mathematical operations

class MathOperations:
    # Static method that adds two numbers
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

    # Static method that multiplies two numbers
    @staticmethod
    def multiply_numbers(num1, num2):
        return num1 * num2

    # Static method that computes the factorial of a number
    @staticmethod
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * MathOperations.factorial(num - 1)

# Example usage
print(MathOperations.add_numbers(2, 3))  # Output: 5
print(MathOperations.multiply_numbers(4, 5))  # Output: 20
print(MathOperations.factorial(4))  # Output: 24
