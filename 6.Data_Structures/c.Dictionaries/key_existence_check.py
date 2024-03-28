# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Check if a key exists
key_to_check = "age"
if key_to_check in student:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

# Output: The key 'age' exists in the dictionary.

# Check for non-existent key
key_to_check = "city"
if key_to_check in student:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

# Output: The key 'city' does not exist in the dictionary.

# Using get() method to check for key existence
key_to_check = "name"
if student.get(key_to_check) is not None:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

# Output: The key 'name' exists in the dictionary.
