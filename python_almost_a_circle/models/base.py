#!/usr/bin/python3
""" Creates a class """


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
    Constructor for the Base class.

    Args:
        id (int, optional): The ID to assign to the object. If not provided,
        an ID will be automatically generated.

    Attributes:
        id (int): The unique identifier for the object.

    Raises:
        None

    Returns:
        None
    """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
