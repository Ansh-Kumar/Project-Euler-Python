import sqlite3
import datetime
import random
import time

conn = sqlite3.connect('simpleDataBase')
c = conn.cursor()
date = datetime.datetime.now()


c.execute('CREATE TABLE IF NOT EXISTS secondDataBase (datestamp TEXT, value REAL)')
def addData():
    num = random.randrange(0, 100)
    c.execute("INSERT INTO secondDatabase (datestamp, value) VALUES (?, ?)",
          (date, num))
    conn.commit()



for x in range(777):
    addData()
    time.sleep(0.5)
c.execute('SELECT * FROM secondDataBase')
[print(row) for row in c.fetchall()]

