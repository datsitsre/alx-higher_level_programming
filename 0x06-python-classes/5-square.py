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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for num in range(self.__size):
            for rows in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
