# list_iteration_examples.py

# Example 1: Iterating through a list of strings and printing their lengths.

# List of strings
words = ["apple", "banana", "orange", "grape"]

# Iterate through the list and print the length of each string
print("Length of each word:")
for word in words:
    print(len(word))


# Example 2: Iterating through a list of numbers and calculating their squares.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate through the list and calculate the square of each number
print("\nSquare of each number:")
for num in numbers:
    print(num * num)


# Example 3: Iterating through a list of lists and printing each element.

# List of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterate through the list of lists and print each element
print("\nElements of the matrix:")
for row in matrix:
    for element in row:
        print(element)
