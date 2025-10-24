"""
Date: 2025-10-24
Author: Augustine Khumalo
Description: A simple Python script that defines a function that receives two numbers as parameters and returns the maximum of the two numbers.
"""

def return_maximum(num1, num2):
    """Returns the maximum of two numbers."""
    if num1 > num2:
        return num1
    else:
        return num2
    
maximum_value = return_maximum(10, 10)
print("The maximum value is:", maximum_value)