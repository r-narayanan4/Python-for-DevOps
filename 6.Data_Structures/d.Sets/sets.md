# Sets in Python

In Python, a set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from them. Sets are commonly used for membership testing, removing duplicates from a sequence, and performing mathematical set operations.

## Basic Concepts

### Creating a Set

Sets in Python can be created using curly braces `{}` or the `set()` constructor.

### Indexing

Sets are unordered collections, so they do not support indexing. You cannot access individual elements of a set using indexing like you would with lists or tuples.

### Adding and Removing Elements

You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods.

### Looping Over Sets

You can loop over the elements of a set using a `for` loop.

### Set Operations

Sets support various mathematical operations such as union, intersection, difference, and symmetric difference.

## Set Methods

### `add(element)`

Adds an element to the set.

### `remove(element)`

Removes the specified element from the set. Raises a KeyError if the element is not present.

### `discard(element)`

Removes the specified element from the set if it is present.

### `clear()`

Removes all elements from the set.

### `union(other_set)`

Returns a new set containing all elements from both sets.

### `intersection(other_set)`

Returns a new set containing only the elements that are present in both sets.

### `difference(other_set)`

Returns a new set containing elements that are present in the first set but not in the second set.

### `symmetric_difference(other_set)`

Returns a new set containing elements that are present in either set, but not in both.

## Set Comprehensions

Set comprehensions provide a concise way to create sets in Python.


