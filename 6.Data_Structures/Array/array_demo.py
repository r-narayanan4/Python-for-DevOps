# Declaration and Initialization of an array
array = [5, 3, 1, 4, 2]

# Printing the original array
print("Original Array:", array)

# Accessing elements of the array using indexing
print("Element at index 0:", array[0])
print("Element at index 2:", array[2])
print("Last element:", array[-1])

# Deleting an element at index 2
del array[2]
print("Array after deleting element at index 2:", array)

# Reversing the array
reversed_array = array[::-1]
print("Reversed Array:", reversed_array)

# Sorting the array in ascending order
ascending_sorted_array = sorted(array)
print("Array sorted in ascending order:", ascending_sorted_array)

# Sorting the array in descending order
descending_sorted_array = sorted(array, reverse=True)
print("Array sorted in descending order:", descending_sorted_array)

# Adding an element to the array
array.append(6)
print("Array after adding element 6:", array)
