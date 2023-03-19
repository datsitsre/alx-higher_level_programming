#!/usr/bin/python3

def delete_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        del my_list[idx]
        return (my_list)
