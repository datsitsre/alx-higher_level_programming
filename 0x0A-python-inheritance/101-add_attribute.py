#!/usr/bin/python3
""" Adds attributes to an object """


def add_attribute(type_object, type_attribute, type_value):
    """
        Add a new attribute to an atrributes
        Attributes : type_object, type_attribute, type_value
    """
    if not hastattr(type_object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(type_object, type_attribute, type_value)
