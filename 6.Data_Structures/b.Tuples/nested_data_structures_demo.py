# Lists inside Tuples and Tuples inside Lists

# Define a tuple with a list inside
tuple_with_list = (1, 2, [3, 4, 5])

# Define a list with a tuple inside
list_with_tuple = [1, 2, (3, 4, 5)]

# Accessing elements
print("Tuple with List:", tuple_with_list)
print("List with Tuple:", list_with_tuple)

# Accessing elements inside the tuple with list
print("First element of the list inside the tuple:", tuple_with_list[2][0])  # Output: 3
print("Second element of the list inside the tuple:", tuple_with_list[2][1]) # Output: 4

# Accessing elements inside the list with tuple
print("Tuple inside the list at index 2:", list_with_tuple[2])                 # Output: (3, 4, 5)
print("Second element of the tuple inside the list:", list_with_tuple[2][1])   # Output: 4

