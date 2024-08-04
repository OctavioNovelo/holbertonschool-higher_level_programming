#!/usr/bin/python3
"""
connect database to python and list all states
"""
import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connect to the database and list all states in ascending order by id
    """
    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()
    
    # Execute the SQL query to retrieve all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows from the executed query
    query_rows = cur.fetchall()
    
    # Iterate through the rows and print each one
    for row in query_rows:
        print(row)
    
    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the function to list states
    list_states(username, password, database)
