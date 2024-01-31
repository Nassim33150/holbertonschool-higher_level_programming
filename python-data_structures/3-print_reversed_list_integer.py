#!/usr/bin/python3

# Print all integers of a list
def print_reversed_list_integer(my_list=[]):
    for x in my_list[::-1]:
        print("{:d}".format(x))
