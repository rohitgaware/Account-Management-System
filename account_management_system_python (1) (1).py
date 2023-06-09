# -*- coding: utf-8 -*-
"""Account_Management_System_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DQy8ouH7QgaBovVrbumEEXcdgGgMBKvp
"""

# Account Management System 

print("****************************************\n  Welcome To Account Management system\n****************************************")

# defining the functions
def connect():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    print("Account Database Created Sucessfully..!")
    db.close()
    
# creating Table     
def create():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    sql = "create table Account(Account_ID int,Account_Name varchar,Account_Size int,Account_Budget int,Account_Duration int,Account_status varchar)"
    db.execute(sql)
    print("Account Table Created Sucessfully..!")
    db.close()
    
# inserting Value into table
def insert():
    import sqlite3
    count = 1
    while count <=10:
        db = sqlite3.Connection("Account.db")
        ID = int(input("Please Enter Your Account ID : "))
        Name = input("Please Enter Your Account Name : ")
        Size = int(input("Please Enter Your Account size(No.of.Resources) : "))
        Budget = int(input("Please Enter Your Account Budget : "))
        Duration = int(input("Please Enter Your Account Duration(In Months) : "))
        Status = input("Please Enter Your Account Status(Active/Inactive) : ")
        
        sql = "insert into Account values(%d,'%s',%d,%d,%d,'%s')"%(ID,Name,Size,Budget,Duration,Status)
        
        try :
            db.execute(sql)
            db.commit()
        except Exception as e :
            print('Error :',e)
            db.rollback()
        db.close()
        count += 1
        print("Please Enter Next Entry")
    print("Sorry, Entry Limit is Reached")
    
# read the values into the table
def read():
    import sqlite3 
    db = sqlite3.Connection("Account.db")
    cursor = db.execute("select Account_ID,Account_Name,Account_Size,Account_Budget,Account_Duration,Account_Status from Account")
    data = cursor.fetchall()
    for d in data:
        print(d)
        
    db.close()
    
# update values into table
def update():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    ID = int(input("Please Enter Your Account ID : "))
    Name = input("Please Enter Your Account Name : ")
    Size = int(input("Please Enter Your Account size : "))
    Budget = int(input("Please Enter Your Account Budget : "))
    Duration = int(input("Please Enter Your Account Duration : "))
    Status = input("Please Enter Your Account Status : ")
    
    sql = f"insert into Account values('{ID}','{Name}','{Size}','{Budget}','{Duration}','{Status}')"
    
    try :
        db.execute(sql)
        print("Account Status Update Sucessfully..!")
        db.commit()
    except Exception as e :
        print('Error :',e)
        db.rollback()
    db.close()
    
# delete values into table
def delete():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    ID = int(input("Enter Account ID Which You Want To Delete :"))
    sql = "DELETE FROM Account WHERE Account_ID="+str(ID)
    
    try :
        db.execute(sql)
        print("Data Delete Sucessfully..!")
        db.commit()
    except Exception as e :
        print('Error :',e)
        db.rollback()
    db.close()
    
# createing class and connect and call the functions 
class Account :
    while True :
        print("          :: MAIN MENU ::          \n\n[1] To Establist Database Connection \n[2] To Create Table \n[3] Insert Value Into Table \n[4] Read Value From Table \n[5] Update value Into The Table \n[6] Delete Value From Table \n[7] Exite \n Please Select Your Option (1-7) ")
        check = int(input("Pleaes Enter Your Choise : "))
        if check == 1:
            connect()
        elif check == 2:
            create()
        elif check == 3:
            insert()
        elif check == 4:
            read()
        elif check == 5:
            update()
        elif check == 6:
            delete()
        elif check == 7:
            print("Exit")
            break
        else :
            pass
        
# defining the functions for fetching Active and Inactive Account
def active():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    cursor = db.execute("select * from Account where Account_Status = 'Active'")
    data = cursor.fetchall()
    print("**************************************\n         Active Accounts Are\n**************************************")
    for d in data :
        print(d)
        
    db.close()
active()

def inactive():
    import sqlite3
    db = sqlite3.Connection("Account.db")
    cursor = db.execute("select * from Account where Account_Status = 'Inactive' ")
    data = cursor.fetchall()
    print("**************************************\n        Inactive Accounts Are\n**************************************")
    for d in data :
        print(d)
        
    db.close()
inactive()

import csv
import sqlite3
db = sqlite3.Connection('Account.db')
cursor = db.execute("select * from Account where Account_status='Active'")
data = cursor.fetchall()
for d in data:
    with open('Account.csv', 'w', newline='') as file:
        w = csv.writer(file)
        w.writerows(data)
        
cursor = db.execute("select * from Account where Account_status='Inactive'")
data = cursor.fetchall()
for d in data:
    data1 = d
    import csv
    with open('Account.csv','a') as file:
        w = csv.writer(file)
        w.writerow(data1)
            
db.close()

import pandas as pd

df = pd.read_csv('/content/Account.csv')
df

