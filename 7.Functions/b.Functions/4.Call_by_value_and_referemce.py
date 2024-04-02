'''What is Call by Value and Call by Reference in Python?

# Call by Value

It is a way of passing arguments to a function in which the arguments get copied to the formal parameters of a function and are stored in different memory locations. In short, Any changes made within the function are not reflected in the actual parameters of the function when called.

# Call by Reference

It is a way of passing arguments to a function call in which both the actual argument and formal parameters refer to the same memory locations, and any changes made within the function are reflected in the actual parameters of the function when called.

If we consider call by value and call by reference in Python, then we must keep in mind that,

Python variables are not storage containers. Rather Python’s variables are like memory references. They refer to the memory address where the value is stored.

Hence, we should know about Mutable and Immutable Objects.

Mutable objects
An object whose internal state can be changed is called a mutable object. Examples of Mutable objects are Lists, Sets, Dictionaries, bytes and arrays. User-defined classes can be mutable or immutable, depending on whether we can change their internal state.

Note- All operations using mutable objects may or may not change the object.

Immutable objects
An object whose internal state cannot be changed is called an immutable object. Examples of immutable objects are Numbers(int, float, bool, etc), Strings, Tuples, Frozen sets(mutable version of sets are termed as Frozen sets)

Note-All operations using immutable objects make copies.
'''
# Code Snippet explaining mutable and immutable objects

List1 = [2, 4, 6]
List2 = List1
List1.append(8) #Both List1 and List2 are changed
print ("New List 1 after append: ",List1)
print ("New List 2 after append: ",List2)
print("We see that changes are reflected in both List1 and List2")
List1= List1 + [10]
print ("New List 1 after 10 is added",List1) #List 1 is changed
print ("New List2 after 10 is added to List1",List2) #List 2 remains same, since copy of List 1 is only made
print("When a new value is added to List 1, then List 2 remains the same since copy of List1 is made")

# output
'''
New List 1 after append:  [2, 4, 6, 8]
New List 2 after append:  [2, 4, 6, 8]
We see that changes are reflected in both List1 and List2
New List 1 after 10 is added [2, 4, 6, 8, 10]
New List2 after 10 is added to List1 [2, 4, 6, 8]
When a new value is added to List 1, then List 2 remains the same since copy of List1 is made
'''
'''Call by Value in Python
When Immutable objects such as whole numbers, strings, etc are passed as arguments to the function call, then it can be considered as Call by Value.

This is because when the values are modified within the function, then the changes do not get reflected outside the function.
'''
# Example showing Call by Value in Python

def myFunc(a):
 print("Value received in 'a' =", a)
 a+=2
 print("Value of 'a' changes to :",a)
 
num=13
print("Initial number: ", num)
myFunc(num)
print("Value of number= ", num)

# Output

'''
Initial number:  13
Value received in 'a' = 13
Value of 'a' changes to : 15
Value of number=  13
'''
# Explanation:

# As we can see here, the value of the number changed from 13 to 15, inside the function, but the value remained 13 itself outside the function. Hence, the changes did not reflect in the value assigned outside the function.

''' Call by Reference in Python

When Mutable objects such as list, dict, set, etc., are passed as arguments to the function call, it can be called Call by reference in Python. When the values are modified within the function, the change also gets reflected outside the function.
'''
# Example 1 showing Call by reference in Python

def myFunc(myList):
 print("List received: ",myList)
 myList.append(3)
 myList.extend([7,1])
 print("List after adding some elements:", myList)
 myList.remove(7)
 print("List within called function:", myList)
 return
 
List1=[1]
print("List before function call :",List1)
myFunc(List1)
print("List after function call: ",List1)


# output

'''
List before function call : [1]
List received:  [1]
List after adding some elements: [1, 3, 7, 1]
List within called function: [1, 3, 1]
List after function call:  [1, 3, 1]

'''
# Explanation: 

# Here we can see that the list value within the function changed from [1] to [1, 3, 1] and the changes got reflected outside the function.

# But, Consider this example-

# Example 2 showing Call by reference in Python

def myFunc(myList):
 print("List received: ",myList)
 myList.append(3)
 myList.extend([7,1])
 print("List after adding some elements:", myList)
 myList.remove(7)
 myList=[3, 4, 6]
 print("List within called function:", myList)
 return
 
List1=[1]
print("List before function call :",List1)
myFunc(List1)
print("List after function call: ",List1)

# Output:

# List before function call : [1]
# List received:  [1]
# List after adding some elements: [1, 3, 7, 1]
# List within called function: [3, 4, 6]
# List after function call:  [1, 3, 1]

# Unlike previous example above, new values are assigned to myList but after function call we see that all the changes do not get reflected outside the function.

# Then, is it Call by reference?

# Lets take a look into the memory environment for both the examples. We'll print the address of the list before calling the function and after calling the function.

# For example 1

def myFunc(myList):
 print("List received: ",myList)
 myList.append(3)
 myList.extend([7,1])
 print("List after adding some elements:", myList)
 myList.remove(7)
 print("Address within function:", (id(myList)))
 print("List within called function:", myList)
 return
 
List1=[1]
print("Address before calling:",(id(List1)))
print("List before function call :",List1)
myFunc(List1)
print("List after function call: ",List1)
print("Address after calling:",(id(List1)))

# Output:

# Address before calling: 139822236006656
# List before function call : [1]
# List received:  [1]
# List after adding some elements: [1, 3, 7, 1]
# Address within function: 139822236006656
# List within called function: [1, 3, 1]
# List after function call:  [1, 3, 1]
# Address after calling: 139822236006656


# Explanation: Here we see the value of the list before calling the function, within the function and after calling the function gets stored in the same memory address. Hence, changes made within function gets reflected outside the function as well.

# Lets consider Example 2 now:

def myFunc(myList):
 print("List received: ",myList)
 myList.append(3)
 myList.extend([7,1])
 print("List after adding some elements:", myList)
 myList.remove(7)
 myList=[3, 4, 6]
 print("Address within function:")
 print((id(myList)))
 print("List within called function:", myList)
 return
 
List1=[1]
print("Address before calling:",(id(List1)))
print("List before function call :",List1)
myFunc(List1)
print("List after function call: ",List1)
print("Address after calling:",(id(List1)))

# Output:

# Address before calling: 139959649811456
# List before function call : [1]
# List received:  [1]
# List after adding some elements: [1, 3, 7, 1]
# Address within function:
# 139959647464768
# List within called function: [3, 4, 6]
# List after function call:  [1, 3, 1]
# Address after calling: 139959649811456

# Explanation: Here we see that, the address of the list changes when new values are assigned to it within the function but outside the function, the value still refers to the previous memory allocation.Hence, the changes made within the function do not get reflected outside the function.

# What do we infer? Well, we see that when mutable objects are passed as arguments to a function then there are two cases:

'''
a.) Change is reflected outside function This is when a mutable object is passed as argument and no new value is assigned to it, ie.,the values refer to the same memory address.

b.) Change is not reflected outside function This is when a mutable object is passed as argument and new values or datatype is assigned to it within the function,ie. when the values outside the function and the values assigned within function refer to different memory addresses.
'''

'''
Note:
In python the changes in values before and after function call solely depends on the memory address.There is object reference depending on memory environment.

Arguments are passed by assignment in Python. Since, assignment just creates references to objects, there’s no alias between an argument name in the caller and callee.

'''