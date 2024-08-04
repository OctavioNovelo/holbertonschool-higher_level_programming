#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the results
    results = cursor.fetchall()
    
    # Print each row
    for row in results:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # List states
    list_states(username, password, database)
