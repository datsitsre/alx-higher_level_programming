#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(host="localhost", user=argv[1], db=argv[2]
                                 passwd=argv[3], port=3306)

    db_cur = db.cursor()
    db_cur.execute("SELECT * FROM states WHERE name LIKE
                   BINARY 'N%' ORDER BY states.id")
    rows = db_cur.fetchall()
    for row in rows:
        print(row)

    db_cur.close()
    db_connect.close()
