import mysql.connector
from .database_connection import *
import os
import sys
from prettytable import PrettyTable
from tkinter import *
from tkinter import messagebox
#import passman_gui

## Query functions
def queryUser(loginID):
    cursor.execute("select username from auth where username = %s", (loginID,))
    username_query = cursor.fetchall()
    if len(username_query) == 0:
        messagebox.showwarning("No User Found", "No user with this username '" + loginID + "' was found!")
        raise ValueError

def queryPass(loginID, password):
    cursor.execute("select pass from auth where username = %s and pass = %s", (loginID, password))
    user_password = cursor.fetchall()
    if len(user_password) == 0:
        messagebox.showwarning("Invalid Password", "Password for user '" + loginID + "' is invalid!")
        raise ValueError
    else:
        messagebox.showinfo("Success", "User has been successfully authenticated!")

def queryEntryID(entry_id):
    cursor.execute("select id from vault where id = %s", (entry_id,))
    id_entries = cursor.fetchone()
    return id_entries[0]

def queryEntry(loginID):
    cursor.execute("""select id, username, pass, link, comment from vault
                                        where loginID = %s""", (loginID,))
    user_info = cursor.fetchall()
    return user_info

def querySingleEntry(loginID, selection):
    cursor.execute("""select id, username, pass, link, comment from vault
                                        where loginID = %s and id = %s""", (loginID, selection))
    single_entry = cursor.fetchall()
    entry = PrettyTable()
    entry.field_names = ["id", "username", "pass", "link", "comment"]
    entry.add_row(single_entry[0])
    print(entry)
    return entry.field_names

## User entry SQL statements
def newEntry(loginID, username, password, link, comment, modified_sql):
    cursor.execute("insert into vault (loginID, username, pass, link, comment, modified) values (%s, %s, %s, %s, %s, %s)", (loginID, username, password, link, comment, modified_sql))
    mydb.commit()
    
def modifyEntry(column, y, selection):
    sql = "update vault set {} = %s where id = %s".format(column)
    cursor.execute(sql, (y, selection))
    mydb.commit()

def removeEntry(loginID, id):
    cursor.execute("""delete from vault
                                        where loginID = %s and id = %s""", (loginID, id))
    mydb.commit()

## User administration SQL statements
def detectDuplicate(new_user):
    cursor.execute("select * from auth where username = %s", (new_user,))
    new_user_check = cursor.fetchall()
    if len(new_user_check) > 0:
        messagebox.showwarning("Duplicate User", "A user with this username already exists!")
        return 1
    else:
        messagebox.showinfo("Success", "User has been created, return to login screen to login.")
        return 0