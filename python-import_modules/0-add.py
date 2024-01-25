#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from the file ad_0.py
    from add_0 import add
    a = 1
    b = 2
    # Use the variables a and b as arguments for the add function
    print("{} + {} = {}".format(a, b, add(a, b)))
