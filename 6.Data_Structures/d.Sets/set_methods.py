# Creating a set
my_set = {1, 2, 3}

# Demonstrating set methods
# add(element): Adds an element to the set
my_set.add(4)
print("After adding 4:", my_set)  # Output: After adding 4: {1, 2, 3, 4}

# remove(element): Removes the specified element from the set
# Raises a KeyError if the element is not present
my_set.remove(2)
print("After removing 2:", my_set)  # Output: After removing 2: {1, 3, 4}

# discard(element): Removes the specified element from the set if it is present
my_set.discard(3)
print("After discarding 3:", my_set)  # Output: After discarding 3: {1, 4}

# clear(): Removes all elements from the set
my_set.clear()
print("After clearing the set:", my_set)  # Output: After clearing the set: set()

# Creating two sets for set operation methods
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union(other_set): Returns a new set containing all elements from both sets
union_set = set1.union(set2)
print("Union set:", union_set)  # Output: Union set: {1, 2, 3, 4, 5}

# intersection(other_set): Returns a new set containing only the elements that are present in both sets
intersection_set = set1.intersection(set2)
print("Intersection set:", intersection_set)  # Output: Intersection set: {3}

# difference(other_set): Returns a new set containing elements that are present in the first set but not in the second set
difference_set = set1.difference(set2)
print("Difference set:", difference_set)  # Output: Difference set: {1, 2}

# symmetric_difference(other_set): Returns a new set containing elements that are present in either set, but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference set:", symmetric_difference_set)  # Output: Symmetric Difference set: {1, 2, 4, 5}
