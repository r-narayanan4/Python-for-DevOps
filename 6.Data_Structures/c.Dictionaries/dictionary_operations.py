# Building a Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print("Dictionary:", student)  # Output: Dictionary: {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Indexing and Accessing Values from a Dictionary
print("Name:", student["name"])  # Output: Name: Alice
print("Age:", student["age"])    # Output: Age: 20
print("Grade:", student["grade"])  # Output: Grade: A

# Adding Keys to a Dictionary
student["city"] = "New York"
print("Updated Dictionary:", student)  # Output: Updated Dictionary: {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'New York'}

# Removing Keys from a Dictionary
del student["grade"]
print("Dictionary after removing grade:", student)  # Output: Dictionary after removing grade: {'name': 'Alice', 'age': 20, 'city': 'New York'}
