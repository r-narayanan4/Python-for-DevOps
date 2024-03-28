# Set comprehension to create a set of squared numbers
squared_numbers = {x**2 for x in range(5)}
print("Squared Numbers:", squared_numbers)
# Output: Squared Numbers: {0, 1, 4, 9, 16}

# Set comprehension with condition to create a set of even numbers
even_numbers = {x for x in range(10) if x % 2 == 0}
print("Even Numbers:", even_numbers)
# Output: Even Numbers: {0, 2, 4, 6, 8}

# Set comprehension with multiple conditions to create a set of tuples
tuple_set = {(x, y) for x in range(1, 3) for y in range(1, 3) if x != y}
print("Tuple Set:", tuple_set)
# Output: Tuple Set: {(1, 2), (2, 1)}

# Set comprehension with string manipulation to create a set of unique characters
string_set = {char.lower() for char in "Hello, World!" if char.isalpha()}
print("String Set:", string_set)
# Output: String Set: {'o', 'e', 'r', 'd', 'l', 'h', 'w'}

'''Set comprehensions in Python provide a concise and elegant way to create sets using a single line of code. They are similar to list comprehensions but produce sets instead of lists.

Here's a simple syntax for set comprehensions:

set_variable = {expression for item in iterable if condition}

expression is the operation or value to include in the set.
item is the variable representing each item in the iterable.
iterable is any iterable object like a list, tuple, or range.
condition is an optional filtering condition. The expression is only added to the set if the condition evaluates to True'''