#!/usr/bin/python3
""" insert into a file """


def append_after(filename="", search_string="", new_string=""):
    """ Append to a file """
    empty_string = ""
    with open(filename, encoding="utf-8") as file_text:
        for line in file_text:
            empty_string += line
            if search_string in line:
                empty_string += search_string
    with open(filename, "w") as file_write:
        file_write.write(empty_string)
