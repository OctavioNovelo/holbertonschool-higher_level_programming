#!/usr/bin/python3
"""
Script to list all states with names starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print("({}, '{}')".format(row[0], row[1]))
    except MySQLdb.Error as e:
        print("Error fetching data:", e)
    finally:
        cur.close()
        conn.close()
