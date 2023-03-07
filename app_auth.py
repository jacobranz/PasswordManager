import mysql.connector
import maskpass


def promptCreds():
    print("Please enter credentials to continue...")
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password: ", mask="#")
    creds = [username, password]
    return creds

def appLogin(username, password):
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = username,
        password = password,
        database = "pass_manager"
    )
    return mydb
    
def testLogin(database):
    cursor = database.cursor()
    cursor.execute('''select * from vault''')
    test = cursor.fetchall()
    print(test)

def main():
    creds = promptCreds()
    databse = appLogin(creds[0], creds[1])
    testLogin(databse)

main()