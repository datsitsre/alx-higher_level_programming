#!/usr/bin/python3
''' create an inheritance '''


class MyList(list):
    ''' create an inheritance list '''

    def __init__(self):
        ''' the instance of the main class '''
        list.__init__(self)

    def print_sorted(self):
        ''' the sorted list '''
        print(sorted(self))
