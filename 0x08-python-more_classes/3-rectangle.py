#!/usr/bin/python3

'''
Rectangle

 Attributes:
    nothing
'''


class Rectangle:
    '''
       Rectangle class

    '''

    def __init__(self, width=0, height=0):
        ''' optional instantiation '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' return private attribute width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter private class for width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' return the height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' set the height class '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Area '''
        return self.height * self.width

    def perimeter(self):
        ''' Perimeter of the rectangle '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)

    def __str__(self):
        ''' print the rectangle as a ## '''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for row in range(self.height):
                for col in range(self.width):
                    print("#", end="")
                print("")
        return ''
