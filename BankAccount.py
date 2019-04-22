import sqlite3
import time
import random
import math
import datetime
import sys

conn = sqlite3.connect('TheBestBankInTheWorld.db')
c = conn.cursor()
## Set Variables
startingBalance = 0
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS AccountLists (First_Name TEXT, Last_Name TEXT, Address TEXT, Account_Balance REAL, Password INT)')
    checkIfUserHasAccount()
def checkIfUserHasAccount():
    print("Hello! Welcome to the Best Bank in the World. Do you currently have an account open in this bank? (Reply with y or n)")
    Input = input()
    if Input == 'y':
        assumeUserHasAccount()
    elif Input == 'n':
        newAccount()
    else:
        sys.exit()
def assumeUserHasAccount():
    print("Let's make sure you do have an account. Please input the First Name on the Account")
    inputFName = input()
    print("Great. We just need a little more info. Please input the Last Name on the Account")
    inputLName = input()
    print("Thank you for this information. I will be going through the database to find your account.")
    lookForAccount(inputFName, inputLName)


def lookForAccount(FirstName, LastName):
    c.execute('SELECT * FROM AccountLists WHERE First_Name=? AND Last_Name=?', (FirstName, LastName))
    print(c.fetchall())
    c.execute('SELECT * FROM AccountLists WHERE First_Name=?', (FirstName, ))
    print(c.fetchall())
    c.execute('SELECT * FROM AccountLists WHERE First_Name=? AND Last_Name=?', (FirstName, LastName))
    fet = c.fetchall()
    print(fet)
    c.execute("SELECT Password FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstName, LastName))
    if len(fet) == 0:
        print("Sorry we could not find your account. 0")
        newAccount()
    elif len(fet) == 1:
        print("We have located your account. Could you please enter your password?")
        c.execute("SELECT Password FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstName, LastName))
        if str(hi[0]) == input():
            hi[0].strip("()")
            print(hi)
            deposit_or_withdrawl(FirstName, LastName)
        else:
            print("HI")
    else:
        print("Sorry we could not find your account. 2+")
        newAccount()

def newAccount():
    print("Please input the First Name on the Account.")
    inputFName = input()
    print("Please input the Last Name on the Account.")
    inputLName = input()
    print("Please input the Password you would like to use")
    inputPassword = input()
    print("Please input your address.")
    inputAddress = input()
    c.execute("INSERT INTO AccountLists (First_Name, Last_Name, Address, Account_Balance, Password) VALUES (?, ?, ?, ?, ?)",
              (inputFName, inputLName, inputAddress, startingBalance, inputPassword))
    conn.commit()
    deposit_or_withdrawl(inputFName, inputLName)
def deposit_or_withdrawl(FirstxName, LastxName):
    print("Now that we have your account what would you like to do? (Reply with 'd' for deposit and 'w' for withdrawl)")
    d_w = input()
    if (d_w == 'd'):
        deposit(FirstxName, LastxName)
    elif (d_w == 'w'):
        withdrawl(FirstxName, LastxName)
    else:
        print("I hate you")
def deposit(FirstxName, LastxName):
    print("How much money would you like to deposit?")
    amount = int(input())
    if (amount > 1000):
        print("You may not deposit more than $1000 Sry.")
        sys.exit()
    else:
        c.execute("SELECT Account_Balance FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
        oAmount = c.fetchall()
        oAmount = oAmount[0]
        amount = amount + float(oAmount[0])
        c.execute("UPDATE AccountLists SET Account_Balance = (?) WHERE First_Name = ? AND Last_Name = ?", (amount, FirstxName, LastxName))
        conn.commit()
        c.execute("SELECT Account_Balance FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
        print(c.fetchall())
        print('Great!')
def withdrawl(FirstxName, LastxName):
    c.execute("SELECT Account_Balance FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
    totalBalance1 = c.fetchall()
    c.execute("SELECT Account_Balance FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
    totalBalance2 = c.fetchall()
    totalBalance1 = totalBalance1[0]
    totalBalance2 = totalBalance2[0]
    print("You may withdraw any amount less than or equal to the total, ", totalBalance1, "or we will be forced to delete your entire account with all the $$$ in it.")
    askedTotal = input()
    if (int(askedTotal) <= int(totalBalance2[0])):
        totalBalance3 = float(totalBalance2[0]) - float(askedTotal)
        c.execute("UPDATE AccountLists SET Account_Balance = (?) WHERE First_Name = ? AND Last_Name = ?", (totalBalance3, FirstxName, LastxName))
        c.execute("SELECT * FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
        [print(row) for row in c.fetchall()]
        conn.commit()
        c.execute("SELECT * FROM AccountLists WHERE First_Name = ? AND Last_Name = ?", (FirstxName, LastxName))
        print(c.fetchall())
    else:
        print("Your account has now been deleted")
        c.execute('DELETE FROM AccountLists WHERE First_Name = ? AND Last_Name = ?', (FirstxName, LastxName))
        conn.commit()
lookForAccount('Ansh', 'Kumar')
##checkIfUserHasAccount()
'''
Logs for Progress

7/21/2018
created func "deposit", "withdrawl", deposit_or_withdrawl
edited errors found in lookForAccount
completed deposit
GOALS for Next Session:
    finsh func withdrawl (check)
    add more datapoints
    test with real life senarios
'''
















