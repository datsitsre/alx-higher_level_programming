''' import super class '''
from models.base import Base


class Rectangle(Base):
    """
        Class Rectangle

        Method :

        Atrributes : width, height
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Defualt Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Private class """
        return self.__width

    @property
    def height(self):
        """Private class """
        return self.__height

    @property
    def x(self):
        """ Private class """
        return self.__x

    @property
    def y(self):
        """ Private class """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("height be an integer")
        if value < 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value
