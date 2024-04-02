"""
Recursive functions are functions that calls itself. It is always made up of 2 portions, the base case and the recursive case.

The base case is the condition to stop the recursion.
The recursive case is the part where the function calls on itself.

"""
# Let's use recursive functions to find the factorial of an integer. A factorial is the product of all integers from 1 to the number itself.

# In the example below, we will be looking for the factorial of 4, or, 4!. 

def factorial(x):
    if x == 1: # This is the base case
        return 1

    else: # This is the recursive case
        return(x * factorial(x-1))

print(factorial(4))

"""
Recursive Sum Function

This Python program demonstrates a recursive function to sum all numbers from 1 to n.
"""

def recursive_sum(n):
    """
    Recursive function to sum all numbers from 1 to n.
    """
    if n == 1:  # Base case: If n is 1, return 1
        return 1
    else:       # Recursive case: Add n to the sum of numbers from 1 to (n-1)
        return n + recursive_sum(n-1)

# Calculate the sum of numbers from 1 to 5
result = recursive_sum(5)
print("Sum of numbers from 1 to 5:", result)  # Output: Sum of numbers from 1 to 5: 15


"""
Recursive Smallest Number Finder

This Python program demonstrates a recursive function to find the smallest number in a list.
"""

def recursive_min(lst):
    """
    Recursive function to find the smallest number in a list.
    """
    # Base case: If the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: Compare the first element with the minimum of the rest of the list
    else:
        return min(lst[0], recursive_min(lst[1:]))

# Example list
A = [1, 4, 24, 17, -5, 10, -22]

# Find the smallest number in the list A
smallest = recursive_min(A)
print("The smallest number in the list is:", smallest)  # Output: The smallest number in the list is: -22


# Explanation:

# Recursive Min Function:
# The recursive_min function finds the smallest number in a list recursively.
# If the list has only one element (base case), it returns that element.
# Otherwise (recursive case), it compares the first element with the minimum of the rest of the list (excluding the first element).
# This process continues recursively until the base case is reached.
# Usage:
# In this example, we have a list A = [1, 4, 24, 17, -5, 10, -22].
# We use the recursive_min function to find the smallest number in the list.
# The result is printed, showing the smallest number in the list as -22.



