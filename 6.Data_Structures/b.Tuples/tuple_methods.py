# Tuple Methods Demo

# Define a tuple
my_tuple = (1, 2, 3, 4, 5, 2)

# Method: count(value)
count_of_2 = my_tuple.count(2)
print("Count of 2 in the tuple:", count_of_2)  # Output: 2

# Method: index(value, start=0, stop=len(tuple))
index_of_4 = my_tuple.index(4)
print("Index of 4 in the tuple:", index_of_4)  # Output: 3

# Using optional parameters in index()
index_of_2_after_index_2 = my_tuple.index(2, 3)
print("Index of 2 after index 2:", index_of_2_after_index_2)  # Output: 5


'''
We define a tuple my_tuple containing integers from 1 to 5, with an additional occurrence of 2.
We use the count() method to count the occurrences of the value 2 in the tuple.
We use the index() method to find the index of the value 4 in the tuple.
We use the optional parameters start in the index() method to find the index of the value 2 after index 2.

'''
"""
Tuple Definition:

my_tuple = (1, 2, 3, 4, 5, 2)
Here, my_tuple is defined as a tuple containing the values (1, 2, 3, 4, 5, 2).

Index Method Call:

index_of_2_after_index_2 = my_tuple.index(2, 3)
The index() method is called on my_tuple to find the index of the first occurrence of the value 2. Additionally, the optional parameter 3 is provided, which specifies that the search should start from index 3.

Search Start Index:
The start parameter specifies the index in the tuple from where the search for the value 2 should begin. In this case, 3 indicates that the search should start from index 3.

Search for Value 2 after Index 3:
The index() method searches for the value 2 in the tuple my_tuple, starting from index 3 onwards. This means it skips the first three elements (1, 2, 3) and starts searching from the fourth element (4).

Result:
The index() method finds the next occurrence of 2 starting from index 3. It finds 2 at index 5, which is the sixth element in the tuple (2).

Assignment:
The index of the first occurrence of 2 found after index 3 is stored in the variable index_of_2_after_index_2. In this case, index_of_2_after_index_2 will have the value 5.

So, in summary, index_of_2_after_index_2 will store the index of the first occurrence of the value 2 that is found after index 3 in the tuple my_tuple.
"""
