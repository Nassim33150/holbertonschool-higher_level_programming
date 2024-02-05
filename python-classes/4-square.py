#!/usr/bin/python3
"""Defines a class Square"""
class Square:
     """
    Class that defines properties of square by: (based on 3-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        self.__size = size
     
     def area(self):
        return self.__size ** 2
    
    def size(self):
        return self.__size
    
    def size(self, value):

            if not isinstance(value, int):
                raise TypeError("size but be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            else :
                self.__size = value
