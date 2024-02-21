#!/usr/bin/python3

from models.rectangle import Rectangle

""" creates a class Square that inherits from class Rectangle"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square]({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @set.setter
    def set_size(self, value):
        if not instance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be an > 0")
        self.width = value
        self.height = value
