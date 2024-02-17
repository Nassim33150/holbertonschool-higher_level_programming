#!/usr/bin/python3
""" function that retrieves a dictionnary representation for JSON """


class Student:
    """ defines new class with attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            at = {}
            for i in attrs:
                if i in self.__dict__:
                    at[i] = self.__dict__[i]
            return at
        return self.__dict__
    
    def reload_from_json(self, json):
        ''' Replaces all attributes of the Student instance '''
        for attr in json:
            self.__dict__[attr] = json[attr]
