#!/usr/bin/python3
""" Students to json """


class Student:
    """
        Name : Student
        Method :
        Atrributes : first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """ instance the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json class """
        object_type = self.__dict__
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__
            dictionary = {}
            for len_attrub in range(len(attrs)):
                for data_dic in object_type:
                    if attrs[len_attrub] == data_dic:
                        dictionary[data_dic] = object_type[data_dic]

            return dictionary

        return self.__dict__

    def reload_from_json(self, json):
        """ replace all attributes """
        for key, value in json.items():
            setattr(self, key, value)
