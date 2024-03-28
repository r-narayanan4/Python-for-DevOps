# Tuple demonstration

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Indexing: Accessing elements of a tuple
print("Indexing:")
print("First element:", my_tuple[0])  # Output: 1
print("Third element:", my_tuple[2])  # Output: 3
print()

# Slicing: Extracting a subset of elements from a tuple
print("Slicing:")
print("Slice 1:", my_tuple[1:4])  # Output: (2, 3, 4)
print("Slice 2:", my_tuple[:3])   # Output: (1, 2, 3)
print("Slice 3:", my_tuple[3:])   # Output: (4, 5)
print()

# Building: Creating a tuple
print("Building:")
new_tuple = (6, 7, 8)
print("New tuple:", new_tuple)
print()

# Immutability: Attempting to modify a tuple (will raise an error)
print("Immutability:")
try:
    my_tuple[0] = 10  # Trying to modify the first element
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment

# Attempting to append to a tuple (will raise an error)
try:
    my_tuple.append(6)  # Trying to append an element
except AttributeError as e:
    print("Error:", e)  # Output: 'tuple' object has no attribute 'append'


'''
This script demonstrates various aspects of tuples in Python:

Indexing: Accessing individual elements of a tuple using indexing.
Slicing: Extracting subsets of elements from a tuple using slicing.
Building: Creating a new tuple.
Immutability: Attempting to modify elements of a tuple, which results in an error due to its immutability.


'''