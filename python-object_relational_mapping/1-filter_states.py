#!/usr/bin/python3
"""
all states with a name starting with N
"""
import MySQLdb
import sys

def list_states_starting_with_n(username, password, database):
    """
    Connect to the MySQL database and list all states where the name starts with 'N'
    Results are sorted by id in ascending order.
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
    
    # Execute the SQL query to retrieve states where name starts with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all rows from the executed query
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
    
    # Call the function to list states starting with 'N'
    list_states_starting_with_n(username, password, database)
