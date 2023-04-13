#!/usr/bin/python3
''' Class MyInt from Int class '''


class MyInt(int):
    ''' Myint rebell class '''
    def __ne__self(self, value):
        ''' Not equal operator  to equal operator'''
        return self.real == value


    def __eq__self(self, value):
        '''  Equal operator  to no equal operator'''
        return self.real != value
