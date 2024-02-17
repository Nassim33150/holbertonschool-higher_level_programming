#!/usr/bin/python3
""" function that return the dictinnary description """


def class_to_json(obj):
    """ retuns the dictionary description
    with simple data structure """
    structure = {}
    if hasattr(obj, "__dict__"):
        strucutre = obj.__dict__.copy()
    return structure
