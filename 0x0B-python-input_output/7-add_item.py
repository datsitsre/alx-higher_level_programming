#!/usr/bin/python3
""" Load, add, save """
import json
import os.path
import sys

""" load the files """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" check for conditionality """
if os.path.isfile("add_item.json"):
    json_file = load_from_json_file("add_item.json")
else:
    json_file = []

json_file.extend(sys.argv[1:])
save_to_json_file(json_file, "add_item.json")
