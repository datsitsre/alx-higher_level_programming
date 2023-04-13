#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """ print a pascal triangle """
    if n <= 0:
        return []

    pascal_st = []
    for i in range(n):
        pascal_st.append([])
        pascal_st[i].append(1)
        for j in range(1, i):
            pascal_st[i].append(pascal_st[i - 1][j - 1]+pascal_st[i - 1][j])
        if (n != 0):
            pascal_st[i].append(1)

    return pascal_st
