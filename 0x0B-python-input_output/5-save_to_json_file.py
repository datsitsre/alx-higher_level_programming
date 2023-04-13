#!/usr/bin/python3
""" Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ Write to a file """
    file_json = json.dumps(my_obj)
    with open(filename, "w") as file_text:
        file_text.write(file_json)
