#!/usr/bin/python3
""" Students to json """


class Student:
    """
        Name : Student
        Method :
        Atrributes : first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """ instance the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to json class """
        return self.__dict__
