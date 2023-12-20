import sqlite3
con = sqlite3.connect('./Database/main.db')

cur = con.cursor()

#for row in cur.execute('SELECT * FROM main ORDER BY jahr'):
#        print(row)

for row in cur.execute('SELECT * FROM main'):
        print(row)

con.close()