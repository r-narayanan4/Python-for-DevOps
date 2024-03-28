from copy import deepcopy

# Original list
original_list = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = original_list[:]

# Deep copy
deep_copy = deepcopy(original_list)

# Modify the copies
shallow_copy[0][0] = 0
deep_copy[0][0] = 0

# Check the original list and copies
print("Original list:", original_list)  # Output: [[1, 2], [3, 4]]
print("Shallow copy:", shallow_copy)    # Output: [[0, 2], [3, 4]]
print("Deep copy:", deep_copy)          # Output: [[0, 2], [3, 4]]

'''
Explanation:
In Python, the terms "clone" and "copy" are often used interchangeably, but they have distinct meanings when it comes to dealing with lists.

Copy:
- When we talk about copying in Python, we often refer to creating a shallow copy of a list. This means that the new list contains references to the original objects in the list, rather than creating new copies of those objects.
- Changes made to the copied list may affect the original list if the elements are mutable (e.g., lists or dictionaries). This is because both the original list and the copied list share references to the same objects.
- In Python, list slicing (list[:]) or the copy() method can be used to create shallow copies of lists.

Clone:
- Cloning, on the other hand, typically refers to creating a deep copy of a list. A deep copy creates a completely independent copy of the original list and all its nested elements.
- Changes made to the cloned list will not affect the original list, regardless of whether the elements are mutable or not.
- To create a deep copy in Python, you need to use the deepcopy() function from the copy module.
- In summary, while both copying and cloning involve creating duplicates of a list, copying usually refers to shallow copying, where changes to the copied list may affect the original list, while cloning refers to deep copying, where changes to the cloned list do not affect the original list.
'''
