import mysql.connector
import database_connection
import os
import sys
from prettytable import PrettyTable
from tkinter import *
from tkinter import messagebox
import main

## Query functions
def queryUser(loginID):
    database_connection.cursor.execute("select username from auth where username = %s", (loginID,))
    username_query = database_connection.cursor.fetchall()
    if len(username_query) == 0:
        messagebox.showwarning("No User Found", "No user with this username was found!")
        raise ValueError

def queryPass(loginID, password):
    database_connection.cursor.execute("select pass from auth where username = %s and pass = %s", (loginID, password))
    user_password = database_connection.cursor.fetchall()
    if len(user_password) == 0:
        messagebox.showwarning("Invalid Password", "Password for user '{loginID}' is invalid!")
        raise ValueError
    else:
        messagebox.showinfo("Success", "User has been successfully authenticated!")

def queryEntryID(entry_id):
    database_connection.cursor.execute("select id from vault where id = %s", (entry_id,))
    id_entries = database_connection.cursor.fetchone()
    return id_entries[0]

def queryEntry(loginID):
    database_connection.cursor.execute("""select id, username, pass, link, comment from vault
                                        where loginID = %s""", (loginID,))
    user_info = database_connection.cursor.fetchall()
    all_entries = PrettyTable()
    all_entries.field_names = ["id", "username", "pass", "link", "comment"]
    i = 0
    while i < len(user_info):
        for entry in user_info:
            all_entries.add_row(entry)
            i += 1
    print(all_entries)
    return all_entries.field_names

def querySingleEntry(loginID, selection):
    database_connection.cursor.execute("""select id, username, pass, link, comment from vault
                                        where loginID = %s and id = %s""", (loginID, selection))
    single_entry = database_connection.cursor.fetchall()
    entry = PrettyTable()
    entry.field_names = ["id", "username", "pass", "link", "comment"]
    entry.add_row(single_entry[0])
    print(entry)
    return entry.field_names

## User entry SQL statements
def newEntry(loginID, username, password, link, comment, modified_sql):
    database_connection.cursor.execute("insert into vault (loginID, username, pass, link, comment, modified) values (%s, %s, %s, %s, %s, %s)", (loginID, username, password, link, comment, modified_sql))
    database_connection.mydb.commit()
    
def modifyEntry(column, y, selection):
    sql = "update vault set {} = %s where id = %s".format(column)
    database_connection.cursor.execute(sql, (y, selection))
    database_connection.mydb.commit()

def removeEntry(loginID, id):
    database_connection.cursor.execute("""delete from vault
                                        where loginID = %s and id = %s""", (loginID, id))
    database_connection.mydb.commit()

## User administration SQL statements
def detectDuplicate(new_user):
    database_connection.cursor.execute("select * from auth where username = %s", (new_user,))
    new_user_check = database_connection.cursor.fetchall()
    if len(new_user_check) > 0:
        messagebox.showwarning("Duplicate User", "A user with this username already exists!")
        return 1
    else:
        messagebox.showinfo("Success", "User has been created, return to login screen to login.")
        return 0