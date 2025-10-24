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

for item in my_list:
    print(f"Item: {item}, Type: {type(item)}")