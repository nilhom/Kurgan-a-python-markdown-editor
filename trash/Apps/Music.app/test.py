import sqlite3
con = sqlite3.connect('./Database/main.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE main (artist,song,genres,style,year)''')

# Insert a row of data
cur.execute("INSERT INTO main VALUES ('Texas','Summer Son','tes2','tewst23',1999)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()