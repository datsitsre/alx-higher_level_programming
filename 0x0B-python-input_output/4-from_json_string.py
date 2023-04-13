#!/usr/bin/python3
""" Json string to Object """
import json


def from_json_string(my_str):
    """ Json string to Object """
    return json.loads(my_str)
