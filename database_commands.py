import mysql.connector
import database_connection

def queryUser(username):
    database_connection.cursor.execute("select username from auth where username = %s", (username,))
    username_query = database_connection.cursor.fetchall()
    if len(username_query) == 0:
        print("ERROR! Username not found!")

def queryPass(username, password):
    database_connection.cursor.execute("select pass from auth where username = %s and pass = %s", (username, password))
    user_password = database_connection.cursor.fetchall()
    if len(user_password) == 0:
        print("ERROR! Password for user '%s' is incorrect!", username)