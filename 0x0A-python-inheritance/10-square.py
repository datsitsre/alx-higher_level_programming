#!/usr/bin/python3
''' A sqaure class '''

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    '''
        Name: Square
        Methdod: area
        Atrributes: size
    '''
    def __init__(self, size):
        ''' Defualt Construtor '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' Area Method '''
        return self.__size * self.__size

    def __str__(self):
        '''Square print '''
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
