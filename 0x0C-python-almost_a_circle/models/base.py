import json


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

    def to_json_string(list_dictionaries):
        """ Json data representation """
        if list_dictionaries is None or list_dictionaries == 0:
            return []
        return json.dumps(list_dictionaries)
