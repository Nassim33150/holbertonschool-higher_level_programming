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
        self._width = value

    @property
    def get_height(self):
        return self.__height

    @height.setter
    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @x.setter
    def set_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    @y.setter
    def set_y(self, value):
        self.__y = value
