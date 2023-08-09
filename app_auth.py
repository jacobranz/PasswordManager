import maskpass
import database_connection
import database_commands


def signUp():
    while True:
        try:
            print("\n===============Sign Up===============\n")
            new_user = input("Please choose a username: ")
            database_commands.detectDuplicate(new_user)
            new_user_pass = maskpass.askpass("Please enter a password: ")
            database_connection.cursor.execute("insert into auth values (%s, %s)", (new_user, new_user_pass))
            database_connection.mydb.commit()
        except:
            continue
        break

def signUp_graphical(new_user, new_user_pass):

    database_commands.detectDuplicate(new_user)
    database_connection.cursor.execute("insert into auth values (%s, %s)", (new_user, new_user_pass))
    database_connection.mydb.commit()

def promptCreds():
    while True:
        try:
            print("\n===============Login===============\n")
            global loginID
            loginID = input("Username: ")
            database_commands.queryUser(loginID)
            password = maskpass.askpass(prompt="Password: ")
            database_commands.queryPass(loginID, password)
            creds = [loginID, password]
        except:
            continue
        break

def getLoginID():
    return loginID

#def main():
    #signUp()
    #creds = promptCreds()
    #appLogin(creds[0], creds[1])
    #password_manager.mainMenu()

#main()