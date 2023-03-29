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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        self.__position = value
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for num in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for rows in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
