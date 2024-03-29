#!/usr/bin/python3

'''
 Square create and empty square

 Attributes:
     size (int): Description of size
 Returns:
    Nothing
'''


class Square:
    '''
        Sqaure class
        Atrributes:
            size (int)
    '''
    def __init__(self, size=0):
        self.__size = int(size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
