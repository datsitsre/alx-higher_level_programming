#!/usr/bin/python3
''' Class MyInt from Int class '''


class MyInt(int):
    '''
	    Name : Myint rebell class
        Method : ne, eq
	'''

    def __ne__(self, value):
        ''' Not equal operator  to equal operator'''
        return self.real == value


    def __eq__(self, value):
        '''  Equal operator  to no equal operator'''
        return self.real != value
