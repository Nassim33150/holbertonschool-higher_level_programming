#!/usr/bin/python3

from models.base import Base

""" creates a class Rectangle that inherits from class Base"""


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        return self.__width

    @width.setter
    def set_width(self, value):
        if not instance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an > 0")
        self._width = value

    @property
    def get_height(self):
        return self.__height

    @height.setter
    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be an > 0")
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @x.setter
    def set_x(self, value):
        if not instance(x, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    @y.setter
    def set_y(self, value):
        if not instance(y, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height
