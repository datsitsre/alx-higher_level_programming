#!/usr/bin/python3
"""
List `cities` from `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name FROM states
                    cities INNER JOIN states ON states.id=cities.state_id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
