#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_replace = list(my_list)
    for i in range(len(list_replace)):
        if list_replace[i] == search:
            list_replace[i] = replace
    return list_replace
