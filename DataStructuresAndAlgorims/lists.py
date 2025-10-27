"""
Date: 2025-10-24
Author: Augustine Khumalo
Description: List is a built-in dynamic array which can store elements of different data types.
- ordered collection of item, meaning elements are stored in the same order as they came into the list. 
- stores references to the objects (elements) rather than storing the actual data itself.

NB: Lists are mutable, meaning their elements can be changed after the list is created.
"""
# Creating a list and assigning it to variables of different data types
my_list = [1, "Hello", 3.14, True, [5, 6, 7]]

#Searching Algorithms
print(6 in my_list) # Output: False because 6 is not an element of my_list however 6 is an element of the nested list [5, 6, 7]
print(6 in my_list[4]) # Output: True because 6 is an element of the nested list [5, 6, 7]