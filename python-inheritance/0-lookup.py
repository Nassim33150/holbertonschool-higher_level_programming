#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """ return all atributes and methodes of @obj """
    list = dir(obj)
    return list
