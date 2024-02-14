#!/usr/bin/python3
""" creates a class that herites form class list """


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """ sort list in ascending """
        n = len(self)
        for i in range(n):
            for j in range(i + 1, n):
                if self[i] > self[j]:
                    self[i], self[j] = self[j], self[i]
        return self
