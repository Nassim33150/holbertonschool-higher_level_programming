#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" create subclass from BaseGeometry """


class Rectangle(BaseGeometry):
    """initializes attributes : width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
