#!/usr/bin/python3
''' Rectangle class '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A class Rectangle

        Method:
            __init__ : defualt instance
        Attributes:
            width, height
    '''
    def __init__(self, width, height):
        ''' instance of child class '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        ''' Calculate the Area '''
        return self.__width * self.__height

    def __str__(self):
        ''' print the area '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
