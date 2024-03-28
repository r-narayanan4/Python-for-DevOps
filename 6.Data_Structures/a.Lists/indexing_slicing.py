# Indexing and slicing
vector = [1, 2, 3, 4, 5]

# Indexing
print("First element:", vector[0])  # Accessing the first element
print("Last element:", vector[-1])   # Accessing the last element

# Slicing
print("Slicing from index 1 to 3:", vector[1:4])  # Slicing from index 1 to 3 (exclusive)

# Other possible slicing operations:
print("Slicing from the beginning to index 3:", vector[:3])    # Slicing from the beginning to index 3 (exclusive)
print("Slicing from index 2 to the end:", vector[2:])         # Slicing from index 2 to the end
print("Slicing with step 2:", vector[::2])                    # Slicing with step 2
print("Reversing the vector:", vector[::-1])                  # Reversing the vector

# Define a sample list
vector2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Start: The starting index of the slice (inclusive)
start_slice = vector2[2:]  # Starting from index 2 to the end
print("Start slice:", start_slice)  # Output: [3, 4, 5, 6, 7, 8, 9, 10]

# End: The ending index of the slice (exclusive)
end_slice = vector2[:6]  # Starting from the beginning to index 5 (exclusive)
print("End slice:", end_slice)  # Output: [1, 2, 3, 4, 5, 6]

# Step: Optional. The step or interval between elements to include in the slice
step_slice = vector2[1::2]  # Starting from index 1 to the end with step 2
print("Step slice:", step_slice)  # Output: [2, 4, 6, 8, 10]

'''
In Python, the colon (:) is used to denote slicing. In the context of slicing a list, the colon separates the start index from the end index within square brackets ([]). The general syntax for slicing is list[start:end:step], where:

start: The starting index of the slice (inclusive).
end: The ending index of the slice (exclusive).
step: Optional. The step or interval between elements to include in the slice.

'''