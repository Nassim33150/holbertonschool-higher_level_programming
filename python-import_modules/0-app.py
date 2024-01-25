#!/usr/bin/python3
# Assign the value 1 to the variable a
a = 1
# Assign the value 2 to the variable b
b = 2
# Import the add function from the file add_0.py
from add_0 import add

# Use the variables a and b as arguments for the add function
print("{} + {} = {}" .format (a, b, add(a, b)))

