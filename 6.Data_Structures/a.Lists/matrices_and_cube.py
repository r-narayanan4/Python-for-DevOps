# Lists in Python can contain elements of any data type, including other lists.
# Lists within lists can be used to represent multi-dimensional data structures like matrices and cubes.

# Example 1: Creating a matrix using lists in lists
matrix = [
    [1, 2, 3],   # First row
    [4, 5, 6],   # Second row
    [7, 8, 9]    # Third row
]

# Accessing elements in the matrix
print("Element at row 2, column 3:", matrix[1][2])  # Output: 6

# Example 2: Creating a cube using lists in lists
cube = [
    [   # Layer 1
        [1, 2, 3],  # First row
        [4, 5, 6],  # Second row
        [7, 8, 9]   # Third row
    ],
    [   # Layer 2
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [   # Layer 3
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

# Accessing elements in the cube
print("Element at layer 2, row 3, column 1:", cube[1][2][0])  # Output: 16

# Modifying elements in the cube
cube[0][1][2] = 100  # Changing an element
print("Modified element at layer 1, row 2, column 3:", cube[0][1][2])  # Output: 100
