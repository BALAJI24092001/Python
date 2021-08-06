import sqlite3

# con = sqlite3.connect(":memory:") #To create a connection in the memory
con = sqlite3.connect("customers.db")

# Create a cursor
c = con.cursor()
# create a table
c.execute(""" CREATE TABLE customers(
    first_name TEXT,
    last_name TEXT,
    email TEXT
) 

""")


# commit our command
con.commit()

# colse our connection
con.close()
