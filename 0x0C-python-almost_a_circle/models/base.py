class Base:
    '''
        Class Name: Base

        Methods :

        Atributes :
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        """ Default Construtor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
