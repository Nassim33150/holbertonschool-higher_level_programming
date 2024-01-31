#!/usr/bin/python3
# replaces an element of a list at a specific position.
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if my_list[i] == element:
            my_list[idx] = idx
            return my_list
