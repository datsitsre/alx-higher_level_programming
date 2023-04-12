#!/usr/bin/python3
''' class empty class '''


class BaseGeometry:
    ''' Name:
            BaseGeometry
        Attributes:

        Method:
            Area
        def __init__(self, name, value):
        self.name = name
        self.value = value
    '''

    def area(self):
        ''' Method Aread '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Method to value date method '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
