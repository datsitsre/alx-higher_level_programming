""" Import the module base """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Name : Square

        Method :

        Attributes :
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Construstor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Private class """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0.")
        self.__size = value
        self.__size = value

    def __str__(self):
        """ overloading method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)
