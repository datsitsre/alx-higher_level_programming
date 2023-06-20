#!/usr/bin/python3

"""
List states from the database
"""

import MySQLdb
from sys import argv

if __name__ = '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    connet = db.cursor()
    connet.execute("SELECT * FROM states")
    row_fetch = connet.fetchall()
    for row in row_fetch:
        print(row)
    connet.close()
    db.close()
