""" Base Class """
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Json data representation """
        if list_dictionaries is None or list_dictionaries == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Json string to file """
        fileClassJson = cls.__name__ + ".json"
        with open(fileClassJson, "w") as typeJson:
            if list_objs is None:
                return typeJson.write("[]")
            else:
                list_objs = [list_dict.to_dictionary()
                             for list_dict in list_objs]
                typeJson.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Json list reprensation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Files to instance """
        refer_file = str(cls.__name__) + ".json"
        try:
            with open(refer_file, "r") as file_json:
                list_dicts = Base.from_json_string(file_json.read())
                return [cls.create(**data) for data in list_dicts]
        except IOError:
            return []

