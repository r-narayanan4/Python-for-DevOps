# Creating a Set
my_set = {1, 2, 3}

# Printing the set
print("Set:", my_set)  # Output: Set: {1, 2, 3}

# Sets do not support indexing
# Trying to access an element using indexing will result in an error
try:
    print(my_set[0])  # This line will raise a TypeError
except TypeError:
    print("Sets do not support indexing")  # Output: Sets do not support indexing

# Adding elements to a set
my_set.add(4)
print("After adding:", my_set)  # Output: After adding: {1, 2, 3, 4}

# Removing elements from a set
my_set.remove(2)  # Removing element 2 from the set
print("After removing:", my_set)  # Output: After removing: {1, 3, 4}
