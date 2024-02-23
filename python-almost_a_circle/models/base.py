#!/usr/bin/python3
""" Creates a class """
import json
import csv
import os.path


class Base:
    """ Class Base """
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
        None.
    """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ serialization """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        js = json.dumps(list_dictionaries)
        return js

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save serialization to file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    def from_json_string(json_string):
        """deserialization"""
        if json_string is None or json_string == "":
            return []
        object = json.loads(json_string)
        return object

    def create(cls, **dictionary):
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance
