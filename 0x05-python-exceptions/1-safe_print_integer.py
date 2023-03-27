#!/usr/bin/python3

# safe_print_integer : print a safe inter
# value : value of the integer
# Return : integer or error

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("{} is not an integer".format(value))
        return (False)
