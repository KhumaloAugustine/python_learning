"""
Date: 2025-10-23
Author: Augustine Khumalo
Description: A simple Python scripts with a function that takes a name as an argument and prints a welcome message to that name.
"""
def welcome_message(name):
    print(f"Hi {name}, welcome to the Python programming world!")

if __name__ == "__main__":
    user_name = "Augustine"
    welcome_message(user_name)