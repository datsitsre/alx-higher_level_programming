#!/usr/bin/python3

# safe_print_list : use exceptions
# my_list : list to use
# x: the number of elements
# Return : print a returned list


def safe_print_list(my_list=[], x=0):
    for num in range(x + 1):
        try:
            print("{:d}".format(my_list[num]), end="")
        except IndexError:
            break
    print("")
    return (num)
