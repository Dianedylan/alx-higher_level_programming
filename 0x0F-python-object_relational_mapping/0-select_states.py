#!/usr/bin/python3
"""
Task 0:
0-select_states.py
Lists all states from the database hbtn_0e_0_usa
Uses:
0-select_states.sql
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cur = db.cursor()
    amount = cur.execute("SELECT * FROM states ORDER BY states.id;")

    for i in range(amount):
        results = cur.fetchone()
        print(results)

    db.close()
