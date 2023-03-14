import mysql.connector
import database_connection
import os
import sys
from prettytable import PrettyTable

def queryUser(loginID):
    database_connection.cursor.execute("select username from auth where username = %s", (loginID,))
    username_query = database_connection.cursor.fetchall()
    if len(username_query) == 0:
        os.system('clear')
        print("ERROR! Username not found!")
        raise ValueError

def queryPass(loginID, password):
    database_connection.cursor.execute("select pass from auth where username = %s and pass = %s", (loginID, password))
    user_password = database_connection.cursor.fetchall()
    if len(user_password) == 0:
        os.system('clear')
        print(f"ERROR! Password for user '{loginID}' is incorrect!")
        raise ValueError
    else:
        print("You have sucessfully authenticated!")

def queryEntryID(entry_id):
    database_connection.cursor.execute("select id from vault where id = %s", (entry_id,))
    id_entries = database_connection.cursor.fetchone()
    return id_entries[0]

def detectDuplicate(new_user):
    database_connection.cursor.execute("select * from auth where username = %s", (new_user,))
    new_user_check = database_connection.cursor.fetchall()
    if len(new_user_check) > 0:
        print(f"A user with the username '{new_user}' already exists!")
        choose_again = input("Choose another username?(y/n): ")
        if choose_again == 'y':
            os.system('clear')
            raise ValueError
        else:
            sys.exit()

def newEntry(loginID, username, password, link, comment, modified_sql):
    database_connection.cursor.execute("insert into vault (loginID, username, pass, link, comment, modified) values (%s, %s, %s, %s, %s, %s)", (loginID, username, password, link, comment, modified_sql))
    database_connection.mydb.commit()

def queryEntry(loginID):
    database_connection.cursor.execute("""select id, username, pass, link, comment from vault
                                        where loginID = %s""", (loginID,))
    user_info = database_connection.cursor.fetchall()
    all_entries = PrettyTable()
    all_entries.field_names = ["ID", "Username", "Password", "Link", "Comment"]
    i = 0
    while i < len(user_info):
        for entry in user_info:
            all_entries.add_row(entry)
            i += 1
    print(all_entries)
    
def modifyEntry(modified_entries):
    database_connection.cursor.execute("update vault set %s")