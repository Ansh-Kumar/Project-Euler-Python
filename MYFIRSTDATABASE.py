import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('myFirstDataBase.db')
c = conn.cursor()

##def createTable():
##    c.execute('CREATE TABLE IF NOT EXISTS firstTable (unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
##
##createTable()
##
##def addData():
##    unix = time.time()
##    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H-%M-%S'))
##    keyword = 'Python'
##    value = random.randrange(0, 10)
##    c.execute("INSERT INTO firstTable (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
##              (unix, date, keyword, value))
##    conn.commit()    
##
##def readFromDB():
##    c.execute('SELECT datestamp, value FROM firstTable')
##    for row in c.fetchall():
##        print(row)
##    
##
##
##
##def del_update():
##
##    c.execute('SELECT * FROM firstTable')
##    [print(row) for row in c.fetchall()]
##
##    c.execute('DELETE FROM firstTable')
##    conn.commit()
####    c.execute("UPDATE firstTable SET value = 99 WHERE value = 8 AND keyword = 'Python'")
####    conn.commit()
####    print("Hi")
####    c.execute('SELECT * FROM firstTable')
####    [print(row) for row in c.fetchall()]
##    print(50*'*')
##    
##    c.execute('SELECT * FROM firstTable')
##    [print(row) for row in c.fetchall()]
##
##
####del_update()
##
#### Database is cleared. Going to start addData func for 10, 000
##
##
##
##
####c.execute('SELECT * FROM firstTable')
####[print(row) for row in c.fetchall()]
####
####print (75*'*')
####
####c.execute('SELECT datestamp, value FROM firstTable')
####[print(row) for row in c.fetchall()]
##
##
##
####for x in range(1):
####    addData()
####    time.sleep(2)
####    if x % 2500 == 0:
####        print(1/4)
####    elif x % 5000 == 0:
####        print(1/2)
####    elif x%7500 == 0:
####        print(3/4)
####c.close()
####conn.close()
##
##
##
##
##
##
##c.execute('UPDATE firstTable SET value = 26 WHERE value = 8 OR value < 3')
##c.execute('DELETE FROM firstTable WHERE value = 26')
##conn.commit()

























