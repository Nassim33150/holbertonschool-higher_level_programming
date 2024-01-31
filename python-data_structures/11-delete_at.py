#!/usr/bin/python3
# deletes the item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in my_list:
        if i == idx:
            my_list.remove(idx+1)
    return my_list
