# dictionary_methods_demo.py

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Using keys() method to get dictionary keys
print("Keys:")
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

# Using items() method to get key-value pairs
print("\nItems:")
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

# Using values() method to get dictionary values
print("\nValues:")
print(student.values())  # Output: dict_values(['Alice', 20, 'A'])

# Using get() method to access value by key
print("\nAccessing value by key using get():")
print("Name:", student.get("name"))  # Output: Name: Alice

# Using pop() method to remove an item
print("\nRemoving 'age' using pop():")
removed_value = student.pop("age")
print("Removed Value:", removed_value)  # Output: Removed Value: 20
print("Updated student dictionary:", student)
# Output: Updated student dictionary: {'name': 'Alice', 'grade': 'A'}

# Using popitem() method to remove and return an arbitrary item
print("\nRemoving an arbitrary item using popitem():")
removed_item = student.popitem()
print("Removed Item:", removed_item)  # Output: Removed Item: ('grade', 'A')
print("Updated student dictionary:", student)
# Output: Updated student dictionary: {'name': 'Alice'}

# Using setdefault() method to set a default value for a key
print("\nSetting default value for 'age' using setdefault():")
default_age = student.setdefault("age", 25)
print("Default Age:", default_age)  # Output: Default Age: 25
print("Updated student dictionary:", student)
# Output: Updated student dictionary: {'name': 'Alice', 'age': 25}

# Using update() method to merge dictionaries
new_data = {"city": "New York", "age": 21}  # Note: 'age' key is updated
student.update(new_data)
print("\nUpdated student dictionary:")
print(student)
# Output: {'name': 'Alice', 'age': 21, 'city': 'New York'}

# Using clear() method to remove all items from the dictionary
student.clear()
print("\nCleared student dictionary:")
print(student)  # Output: {}
