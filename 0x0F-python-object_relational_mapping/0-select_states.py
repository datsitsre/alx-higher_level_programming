#!/usr/bin/python3
"""
List states from thr database
"""
import MySQLdb
import sys 

if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    connet = db.cursor()
    connet.execute("SELECT * FROM states ORDER BY id ASC")
    row_fetch = connet.fetchall()
    for row in row_fetch:
        print(row)
    connet.close()
    db.close()
