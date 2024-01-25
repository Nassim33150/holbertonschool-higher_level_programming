#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
# Import the add function from the file add_0.py
    from add_0 import add

# Use the variables a and b as arguments for the add function
    print("{} + {} = {}" .format (a, b, add(a, b)))

