import sqlite3

name = './Database/main.db'

con = sqlite3.connect(name)
cur = con.cursor()

cur.execute('''CREATE TABLE main (interpret,song,genre,stil,jahr,addedTime,tags)''')

con.commit()
con.close()