#!/usr/bin/python3
"""
This script lists all states hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    db_cur = db.cursor()
    db_cur.execute("SELECT * FROM states")
    rows = db_cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()
