#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the results
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
