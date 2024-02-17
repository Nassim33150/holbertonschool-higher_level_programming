#!/usr/bin/python3
"""Writes an Object to a text file, using
a JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    ''' writes Object to a text file, using JSON representation '''
    json_object = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_object)
