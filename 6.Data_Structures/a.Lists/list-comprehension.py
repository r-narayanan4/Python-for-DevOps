'''
List comprehensions are a concise way to create lists in Python.
They allow you to generate a new list by applying an expression to each item in an iterable.
List comprehensions consist of brackets containing an expression followed by a for clause,
then zero or more for or if clauses. The result will be a new list resulting from evaluating
the expression in the context of the for and if clauses which follow it.
'''

# Example 1: Squares of numbers using list comprehension
squares = [x * x for x in range(1, 6)]
print("Squares of numbers from 1 to 5:", squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Even numbers using list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers from 0 to 9:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# Example 3: Flatten a list of lists using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print("Flattened matrix:", flattened_matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 4: Convert strings to uppercase using list comprehension
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
