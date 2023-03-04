import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL statement to create a table
cursor.execute('''CREATE TABLE product
                  (
                    id INTEGER PRIMARY KEY, 
                    name TEXT(100) UNIQUE, 
                    description TEXT(200),
                    price REAL,
                    qty INTEGER
                    )
                    ''')

# Commit the changes
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
