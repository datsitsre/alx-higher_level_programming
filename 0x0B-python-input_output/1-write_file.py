#!/usr/bin/python3
""" Write text to a file """


def write_file(filename="", text=""):
    """
        Name : write_file
        Method : write text to a file
    """
    with open(filename, "w", encoding="utf-8") as file_text:
        count = 1
        for data in text:
            count += 1
        file_text.write(text)
    return count
