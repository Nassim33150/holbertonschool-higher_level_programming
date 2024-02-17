#!/usr/bin/python3
"""Writes an Object to a text file, using
a JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    json_object = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_object)
