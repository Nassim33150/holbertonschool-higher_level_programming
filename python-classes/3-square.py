#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 2-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates a square of a given size

        Size of the square is hidden

        Args:
            size (int): length of the sides

        Raises:
            TypeError: size is not an integer
            ValueError: size is negative

        """

        if not isinstance(size, int):
            raise TypeError("size but be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the size of square

        Returns:
            size squared for area

        """

        return self.__size ** 2
