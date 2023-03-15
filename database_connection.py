import mysql.connector

mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "spades299",
        database = "password_manager"
    )

cursor = mydb.cursor()