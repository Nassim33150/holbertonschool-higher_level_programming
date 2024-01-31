#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result_dictionary = a_dictionary.copy()
    for key in result_dictionary:
        result_dictionary[key] *= 2
    return result_dictionary
