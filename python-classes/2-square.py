#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size = 0):
            if not isinstance(size, int):
                raise TypeError("size but be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else :
                self.__size = size