#!/usr/bin/python3
''' create an inheritance '''

class MyList(list):
    ''' create an inheritance list '''
    
    def print_sorted(self):
        return self.sort()
