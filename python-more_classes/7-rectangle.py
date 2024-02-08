#!/usr/bin/python3
"""Square Class

defining the rectangle

"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init for Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Rectangle area getter"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the Rectangle,
        or nothing if height/width are 0"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += Rectangle.print_symbol * self.__width + '\n'
        return rectangle_str.strip()

    def __repr__(self):
        """return the representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    """delete a rectangle"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
