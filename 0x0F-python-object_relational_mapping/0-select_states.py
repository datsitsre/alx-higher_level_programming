#!/usr/bin/python3

"""lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    """ the main code """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur_db = db.cursor()
    cur_db.execute("SELECT * FROM states")
    rows = cur_db.fetchall()
    for row in rows:
        print(row)

    cur_db.close()
    db.close()
