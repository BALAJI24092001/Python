# %% [markdown]
# # SQLite
#
# <hr>

# %%
import sqlite3

# con = sqlite3.connect(":memory:") #To create a connection in the memory
con = sqlite3.connect("notes_customers.db")

# create a cursor
c = con.cursor()


# %%
# Create a table
c.execute(""" CREATE TABLE customers(
    first_name TEXT,
    last_name TEXT,
    email TEXT
) 
""")


# %% [markdown]
# ## DataTypes
#
# <hr>
# <b>
#
# NULL
#
# INTEGERS
#
# REAL
#
# TEXT
#
# BLOB
#
#
# #commit our command to the database
# con.commit()
# #colse our connection with the database and python
# con.close()
#
# commit and close functions should be used at the end of the program.</b>

# %%
# import sqlite3
# con = sqlite3.connect("customers.db")
# c = con.cursor()

# Use this execute statement to insert data into database.
c.execute("""
INSERT 
INTO customers 
VALUES("BALAJI", "DEGA", "dbalajivaraprasad@gmail.com"
) 
""")
# con.commit()
# con.close()

# %%
# To enter many entries at one time we can use the below method.

many_customers = [
    ("chak", "yedav", "cyed@yahoo.com"),
    ("abrahim", "moron", "abmoron@hotmail.com"),
    ("ramesh", "ango", "angoramesh@gmail.com"),
]

# We use executemany funcion to input multiple entries at once.
c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

# (?) is called a place holder, used when we are using/passing a variable to the commands

# %%
# Query out DATABASE

c.execute("SELECT * FROM customers")

print(c.fetchall())
print(c.fetchone())  ## To fetch first row of the table.
print(c.fetchmany(2))  ## To fetch 'number_of_entries's number of rows.


# %% [markdown]
# ## Fetch Fucntions
# <hr>
#
# <b>
#
# c.fetchone() ## To fetch first row of the table.
#
# c.fetchmany(number_of_entries) ## To fetch 'number_of_entries's number of rows.
#
# print(c.fetchall()) # To Print all the rows as a list of tuples.
#
# print(c.fetchone()) # once the Cursor selects all the rows it will return to the next fetch function available.
#
# print(c.fetchmany(2)) # so the remaining fetch functions will return either NULL or an empty tuple or list.  </b>

# %%

c.execute("SELECT * FROM customers")

print(c.fetchall()[0])
# we can fetch specific row using [] and a even specific value using [][].

# WE can use all the loops and control statements to structure the data while printing on console.

# %%
c.execute("""
UPDATE customers
SET first_name = "CHAKRADHAR",last_name = "GELLI"
WHERE first_name = "chak" AND last_name = "yedav"
""")
c.execute("""
UPDATE customers
SET first_name = "ABHIRAM",last_name = "AVALA"
WHERE first_name = "abrahim" AND last_name = "moron"
""")

# %%
c.execute("""
DELETE FROM customers
WHERE rowid = 4
""")

# %%
con.commit()
con.close()
