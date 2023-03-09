import mysql.connector
import maskpass
import database_connection
import database_commands
import password_manager


def signUp():
    print("\n===============Sign Up===============\n")
    new_user = input("Please choose a username: ")
    new_user_pass = input("Please enter a password: ")
    database_connection.cursor.execute("insert into auth values (%s, %s)", (new_user, new_user_pass))
    database_connection.mydb.commit()
    promptCreds()

def promptCreds():
    print("\n===============Login===============\n")
    username = input("Username: ")
    database_commands.queryUser(username)
    password = maskpass.askpass(prompt="Password: ", mask="#")
    database_commands.queryPass(username, password)
    creds = [username, password]
    return creds

def appLogin(username, password):
    """
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = username,
        password = password,
        database = "pass_manager"
    )
    return mydb
    """
    password_manager.success()
    
def testLogin(database):
    cursor = database.cursor()
    cursor.execute('''select * from vault''')
    test = cursor.fetchall()
    print(test)

def main():
    creds = promptCreds()
    appLogin(creds[0], creds[1])

main()