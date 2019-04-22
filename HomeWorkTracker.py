import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("HomeworkAssignment.db")
c = conn.cursor()

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS mainTable (NameOfClass TEXT, AssignmentName TEXT, DateReceived TEXT, DateDue TEXT, InPowerSchool TEXT, AssignmentAmount INTEGER, PointsRecieved INTEGER)")
def addData():
    print("Which class are we talking about?")
    className = input()
    print("What is the Assignment Name?")
    amount = input()
    print("When did you get it?")
    datereceived = input()
    print("When is it due?")
    datedue = input()
    print("Is it going to be entered in POWER SCHOOl?")
    entered = input()
    if (entered == '?' or entered == '0'):
        print("Ok. Your Homework has been entered if you need to change the status of this assignment you know what you need to do!")
        c.execute("INSERT INTO mainTable (NameOfClass, AssignmentName, DateReceived, DateDue, InPowerSchool) VALUES (?, ?, ?, ?, ?)",
              (className, amount, datereceived, datedue, entered))
        conn.commit()
    elif (entered == '1'):
        print("How much is the entire assignment worth?")
        gradeTotal = int(input())
        print("How much did you receive?")
        gradeReceived = int(input())
        c.execute("INSERT INTO mainTable (NameOfClass, AssignmentName, DateReceived, DateDue, InPowerSchool, AssignmentAmount, PointsReceived) VALUES (?, ?, ?, ?, ?)",
              (className, amount, datereceived, datedue, entered, gradeTotal, gradeReceived))
        conn.commit()

createTable()
total = int(input("How many hw assignments do you need to enter for today?"))
for i in range(total + 1):
    addData()
# Create code to be able to change the status of assignments
