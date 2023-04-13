#!/usr/bin/python
""" Class to Json """


def class_to_json(obj):
    """ convert a class to json """
    return obj.__dict__
