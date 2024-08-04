#!/usr/bin/python3
"""Conect data base to python"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    connect_db = MySQLdb.connect(host="localhost", port=3066, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])


    cursor_obj = connect_db.cursor()


    cursor_obj.execute("SELECT * FROM states ORDER BY states.id ASC;")


    query_rows = cursor_obj.fetchall()

    for row in query_rows:
        print(row)


    cursor_obj.close
    connect_db.close