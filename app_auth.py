import maskpass
import database_connection
import database_commands

def signUp_graphical(new_user, new_user_pass):

    database_commands.detectDuplicate(new_user)
    database_connection.cursor.execute("insert into auth values (%s, %s)", (new_user, new_user_pass))
    database_connection.mydb.commit()

def login_graphical(loginID, password):
    database_commands.queryUser(loginID)
    database_commands.queryPass(loginID, password)
    return loginID

#def main():
    #signUp()
    #creds = promptCreds()
    #appLogin(creds[0], creds[1])
    #password_manager.mainMenu()

#main()