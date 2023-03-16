import mysql.connector

mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "ctu1234",
        database = "pass_manager"
    )

cursor = mydb.cursor()