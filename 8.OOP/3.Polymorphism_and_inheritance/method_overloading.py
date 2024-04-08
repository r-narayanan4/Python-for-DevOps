'''
Method overloading in Python is not directly supported like in languages such as Java or C++. However, you can achieve 
similar behavior using default parameter values or variable-length argument lists. 
Let me demonstrate both approaches:

'''

# 1. Using Default Parameter Values:

class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of MathOperations
math_ops = MathOperations()

# Calling the add method with different number of arguments
print(math_ops.add(2))         # Output: 2
print(math_ops.add(2, 3))      # Output: 5
print(math_ops.add(2, 3, 4))   # Output: 9

# In this example, the add method can take 2 or 3 arguments. 
# If only one argument is provided, the default values for b and c are assumed to be zero.

# 2. Using Variable-length Argument Lists (*args):

class MyCalculator:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        return result

# Creating an instance of MyCalculator
my_calc = MyCalculator()

# Calling the add method with different number of arguments
print(my_calc.add(2))            # Output: 2
print(my_calc.add(2, 3))         # Output: 5
print(my_calc.add(2, 3, 4))      # Output: 9
print(my_calc.add(2, 3, 4, 5))   # Output: 14

'''
In this example, the add method accepts any number of arguments by using *args, allowing it to be called with varying numbers of 
parameters.

While Python doesn't have explicit method overloading like some other languages, these techniques can achieve similar results by
providing flexibility in the number of arguments a method can accept.

'''
