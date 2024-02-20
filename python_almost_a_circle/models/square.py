#!/usr/bin/python3

from models.rectangle import Rectangle

""" creates a class Square that inherits from class Rectangle"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square]({self.id}) {self.x}/{self.y} - {self.width}"
