# Basic String Functions and Methods

# Length of a string
my_string = "Hello, World!"
print("Length of the string:", len(my_string))  # Output: Length of the string: 13

# Convert string to uppercase
print("Uppercase:", my_string.upper())  # Output: Uppercase: HELLO, WORLD!

# Convert string to lowercase
print("Lowercase:", my_string.lower())  # Output: Lowercase: hello, world!

# Splitting a string into a list of substrings
words = my_string.split(", ")
print("Split:", words)  # Output: Split: ['Hello', 'World!']

# Joining a list of strings into one string
new_string = "-".join(words)
print("Joined:", new_string)  # Output: Joined: Hello-World!

# Finding the index of a substring
print("Index of 'World':", my_string.find("World"))  # Output: Index of 'World': 7

# Replacing occurrences of a substring
replaced_string = my_string.replace("World", "Universe")
print("Replaced:", replaced_string)  # Output: Replaced: Hello, Universe!

# Stripping leading and trailing whitespace
whitespace_string = "   Hello, World!   "
print("Stripped:", whitespace_string.strip())  # Output: Stripped: Hello, World!
