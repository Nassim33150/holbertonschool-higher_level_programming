#!/usr/bin/python3
""" function that retrieves a dictionnary representation for JSON """


class Student:
    """ defines new class with attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_json = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_json
