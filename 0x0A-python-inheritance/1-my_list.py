#!/usr/bin/python3
''' create an inheritance '''

class MyList(list):
    ''' create an inheritance list '''
   
    def __init__(self):
        list.__init__(self)


    def print_sorted(self):
        print(sorted(self))
