#!/usr/bin/python3
""" list all states with name starting with N from hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ the mysql code """
    db_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                 passwd=argv[2], port=3306)

    db_cur = db.cursor()
    db_cur.execute("SELECT * FROM states WHERE name LIKE
                   BINARY 'N%' ORDER BY states.id")
    rows = db_cur.fetchall()
    for row in rows:
        print(row)

    db_cur.close()
    db_connect.close()
