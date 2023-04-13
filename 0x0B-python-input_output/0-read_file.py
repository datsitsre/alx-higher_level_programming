#!/usr/bin/python3
""" Read a text from a file """


def read_file(filename=""):
    """
        Name : read_file
        Method : read a  text from a file
    """
    with open(filename, encoding="utf-8") as file_text:
        read_data = file_text.read()
        print(read_data, end="")
