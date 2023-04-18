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

    def from_json_string(json_string):
        """ Json list reprensation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
