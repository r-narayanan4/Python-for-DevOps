# Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: combines elements from both sets
union_set = set1 | set2
print("Union set:", union_set)
# Output: Union set: {1, 2, 3, 4, 5}

# Intersection: finds common elements in both sets
intersection_set = set1 & set2
print("Intersection set:", intersection_set)
# Output: Intersection set: {3}

# Difference: finds elements in set1 but not in set2
difference_set = set1 - set2
print("Difference set:", difference_set)
# Output: Difference set: {1, 2}

# Symmetric Difference: finds elements in either set but not in both
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference set:", symmetric_difference_set)
# Output: Symmetric Difference set: {1, 2, 4, 5}
