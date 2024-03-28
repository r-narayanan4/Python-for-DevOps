# Create a sample list
my_list = [1, 2, 3]

# append(): Adds an element to the end of the list
my_list.append(4)
print("After append(4):", my_list)  # Output: [1, 2, 3, 4]

# insert(): Inserts an element at a specified index
my_list.insert(1, 5)
print("After insert(1, 5):", my_list)  # Output: [1, 5, 2, 3, 4]

# index(): Returns the index of the first occurrence of the specified element
print("Index of 3:", my_list.index(3))  # Output: 3

# remove(): Removes the first occurrence of the specified element
my_list.remove(2)
print("After remove(2):", my_list)  # Output: [1, 5, 3, 4]

# pop(): Removes and returns the element at the specified index (default is the last element)
popped_element = my_list.pop(1)
print("Popped element:", popped_element)  # Output: 5
print("After pop(1):", my_list)  # Output: [1, 3, 4]

# extend(): Adds the elements of another list to the end of the current list
my_list.extend([6, 7])
print("After extend([6, 7]):", my_list)  # Output: [1, 3, 4, 6, 7]

# count(): Returns the number of occurrences of a specified element in the list
print("Count of 3:", my_list.count(3))  # Output: 1

# reverse(): Reverses the order of the elements in the list
my_list.reverse()
print("After reverse():", my_list)  # Output: [7, 6, 4, 3, 1]

# sort(): Sorts the elements of the list in ascending order
my_list.sort()
print("After sort():", my_list)  # Output: [1, 3, 4, 6, 7]

# len(): Returns the number of elements in the list
print("Length of list:", len(my_list))  # Output: 5

# del: Deletes the element at a specified index
del my_list[2]
print("After del my_list[2]:", my_list)  # Output: [1, 3, 6, 7]

# clear(): Removes all elements from the list
my_list.clear()
print("After clear():", my_list)  # Output: []

# copy(): Returns a shallow copy of the list
original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Copied list:", copied_list)  # Output: [1, 2, 3]
print("Are they same?", original_list is copied_list)  # Output: False


# Create a sample list
my_list1 = [1, 2, 3, 4]

# __getitem__(): Gets the element at the specified index
element_at_index_1 = my_list1[1]
print("Element at index 1:", element_at_index_1)  # Output: 2

# __setitem__(): Sets the element at the specified index
my_list1[1] = 5
print("After setting element at index 1 to 5:", my_list1)  # Output: [1, 5, 3, 4]


'''
del:

del is a keyword in Python used to remove an element from a list at a specified index.
It does not return the removed element but directly modifies the original list.
You can use del to remove elements, slices, or even entire lists.

pop():

pop() is a method in Python used to remove and return an element from a list at a specified index.
It takes an optional index as an argument. If no index is provided, it removes and returns the last element of the list.
pop() modifies the original list and returns the removed element.

remove():

remove() is a method in Python used to remove the first occurrence of a specified value from the list.
It takes the value to be removed as an argument.
If the specified value is not found in the list, it raises a ValueError.
remove() modifies the original list.

clear():

clear() is a method in Python used to remove all elements from the list, leaving it empty.
It does not take any arguments.
clear() modifies the original list and returns None.
'''

new_list = [1, 2, 3, 4, 5]

# del: Removes element at index 2
del new_list[2]
print("After del new_list[2]:", new_list)  # Output: [1, 2, 4, 5]

# pop(): Removes and returns the element at index 2
popped_element = new_list.pop(2)
print("Popped element:", popped_element)  # Output: 4
print("After pop(2):", new_list)  # Output: [1, 2, 5]

# remove(): Removes the first occurrence of value 2
new_list.remove(2)
print("After remove(2):", new_list)  # Output: [1, 5]

# clear(): Removes all elements from the list
new_list.clear()
print("After clear():", new_list)  # Output: []


