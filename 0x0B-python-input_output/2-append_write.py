#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """
        Name : 2-append_write.py
        Method : append_write
    """
    with open(filename, "a", encoding="utf-8") as file_text:
        count = 0
        for numb in text:
            count += 1
        file_text.write(text)
        return count
