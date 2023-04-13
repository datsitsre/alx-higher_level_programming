#!/usr/bin/python3
""" Create Object from  a JSON file """
import json


def load_from_json_file(filename):
    """ Create an object from a JSON file """
    with open(filename) as file_text:
        data = json.load(file_text)
    return data
