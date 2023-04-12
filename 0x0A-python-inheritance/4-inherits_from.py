#!/usr/bin/python3
''' return true '''


def inherits_from(obj, a_class):
    ''' Returns True if the object is an instance '''
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
