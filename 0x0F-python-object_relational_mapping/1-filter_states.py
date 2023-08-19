#!/usr/bin/python3
""" listing all states with a name starting with N from the db hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",  port=3306,
                        user=sys.argv[1], password=sys.argv[2],
                        database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
