#!/usr/bin/python3

from models.rectangle import Rectangle

""" creates a class Square that inherits from class Rectangle"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_square + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """ update arguments """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def to_dictionary(self):
            """ Returns a dictionary """
            list = ['id', 'size', 'x', 'y']
            dict = {}

            for key in list:
                if key == 'size':
                    dict[key] = getattr(self, 'width')
                else:
                    dict[key] = getattr(self, key)

            return dict
