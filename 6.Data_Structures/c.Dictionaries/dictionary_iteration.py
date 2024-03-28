# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Iterating through keys
print("Keys:")
for key in student:
    print(key)  # Output: name, age, grade

# Iterating through values
print("\nValues:")
for value in student.values():
    print(value)  # Output: Alice, 20, A

# Iterating through both keys and values
print("\nKeys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 20, grade: A


#Formatted strings, denoted by the f prefix before the string, allow for convenient string interpolation in Python. This means you can include variables, expressions, and even function calls directly within the string. Here's a simple example to illustrate their usage:
name = "Alice"
age = 20

# Using formatted string literal
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)

