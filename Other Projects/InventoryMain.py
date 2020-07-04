import sqlite3
import time
import datetime
import time
import random


conn = sqlite3.connect('InventoryDB.db')
c = conn.cursor()

def CreateMain():
    c.execute("CREATE TABLE IF NOT EXISTS mainTable (Week_Number INTEGER, Date TEXT, Vendor TEXT, Item_Number INTEGER, Name_of_Product TEXT, Amount_Total REAL,  Amount_Sold REAL, Price_Ordered REAL, Price_Selling REAL, Status TEXT)")

def InputBasedData():
    dateandtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weekInput = input("What is the week number of this data input?")
    vendorInput = input("What is the vendor if this data input?")
    itemNumInput = input("What is the item number for this paticular input?")
    productNameInput = input("What is the full name of this product")
    amountTotalInput = input("What is the total amount we have of this item?")
    amountSoldInput = input("How much have we sold this week?")
    priceOrdered = input("How much did it cost from the vendor?")
    priceSelling = input("What is the price of the item when we are selling?")
    statusInput = input("What is the stutus of this item?")
    c.execute('INSERT INTO mainTable (Week_Number, Date, Vendor, Item_Number, Name_of_Product, Amount_Total, Amount_Sold, Price_Ordered, Price_Selling, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (weekInput, dateandtime, vendorInput, itemNumInput, productNameInput, amountTotalInput, amountSoldInput, priceOrdered, priceSelling, statusInput))
    conn.commit()

    
CreateMain()
InputBasedData()
