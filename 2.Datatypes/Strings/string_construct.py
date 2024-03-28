# Constructing Strings in Python

# Indexing, Slicing, Immutability
my_string = "Python"
print("Original String:", my_string)
print("First character:", my_string[0])  # Output: First character: P
print("Last character:", my_string[-1])  # Output: Last character: n
print("Slicing:", my_string[2:5])  # Output: Slicing: thon

# Immutability - Attempting to change a character will result in an error
try:
    my_string[0] = 'C'
except TypeError:
    print("Strings are immutable")  # Output: Strings are immutable

# Escaping using the \ character
escaped_string = "This is a \"quoted\" string."
print("Escaped String:", escaped_string)  # Output: Escaped String: This is a "quoted" string.

# Using \n for newline and \\ for backslash
multi_line_string = "Line 1\nLine 2\nLine 3"
print("Multi-line String:")
print(multi_line_string)
# Output:
# Multi-line String:
# Line 1
# Line 2
# Line 3

# Using triple quotes for multi-line strings
multi_line_string_alt = """Line 1
Line 2
Line 3"""
print("Alternative Multi-line String:")
print(multi_line_string_alt)
# Output:
# Alternative Multi-line String:
# Line 1
# Line 2
# Line 3
