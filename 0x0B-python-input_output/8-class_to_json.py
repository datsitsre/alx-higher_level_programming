#!/usr/bin/python
""" Class to Json """
import json
""" Import the module """


def class_to_json(obj):
    """ convert a class to json """
    return json.dumps(obj.__dict__)
