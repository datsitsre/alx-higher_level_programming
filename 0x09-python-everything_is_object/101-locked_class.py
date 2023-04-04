#!/usr/bin/python3
'''
class : LockedClass
'''


class LockedClass:
    '''
        Locked class
        prevent user from dynamically creating new instance
    '''
    __slots__ = ['first_name']
