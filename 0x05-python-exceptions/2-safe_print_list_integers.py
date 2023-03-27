#!/usr/bin/python3

# safe_print_list_integer : print a safe inter
# x=0 : value of the integer
# my_list : a list
# Return : integer or error

def safe_print_list_integers(my_list=[], x=0):
    for num in range(x + 1):
        try:
            print("{:d}".format(my_list[num]), end="")
        except (TypeError, ValueError):
            pass
    print("")
    return (num)
