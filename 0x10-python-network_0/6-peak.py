#!/usr/bin/python3

"""
Find the peak list of unsorted integers
"""


def find_peak(list_of_integers):
    """Find a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lower = 0
    higher = len(list_of_integers)
    mid = ((higher - lower) // 2) + lower
    mid = int(mid)
    if higher == 1:
        return list_of_integers[0]
    if higher == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
