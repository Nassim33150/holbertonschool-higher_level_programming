#!/usr/bin/python3
""" creates a class that herites form class list """


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """ sort list in ascending """
        print(sorted(self))
