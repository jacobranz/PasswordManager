import mysql.connector
import database_connection
import os
import sys

def queryUser(username):
    database_connection.cursor.execute("select username from auth where username = %s", (username,))
    username_query = database_connection.cursor.fetchall()
    if len(username_query) == 0:
        os.system('clear')
        print("ERROR! Username not found!")
        raise ValueError

def queryPass(username, password):
    database_connection.cursor.execute("select pass from auth where username = %s and pass = %s", (username, password))
    user_password = database_connection.cursor.fetchall()
    if len(user_password) == 0:
        os.system('clear')
        print(f"ERROR! Password for user '{username}' is incorrect!")
        raise ValueError

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
