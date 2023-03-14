import os
import app_auth
import database_commands
from datetime import datetime

def mainMenu():
    os.system('clear')
    print("""
    \n\n
--------------------------------------------
----- Welcome to Password Manager 1.0! -----
--------------------------------------------
""")
    print("""
1. Sign up
2. Login
\n""")

    answer = int(input(">> "))
    match answer:
        case 1:
            app_auth.signUp()
        case 2:
            app_auth.promptCreds()
        case _:
            print("Invalid option selected")

def userOptions():
    os.system('clear')
    print("""
---------------------------------------------
1. Create new entry
2. Modify entry
3. Delete entry
4. View existing entry
---------------------------------------------""")
    user_choice = int(input(">> "))
    match user_choice:
        case 1:
            print("You have selected to create a new entry.")
            loginID = app_auth.loginID
            username = str(input("Enter username: "))
            password = str(input("Enter password: "))
            link = str(input("Enter link: "))
            comment = str(input("Comments: "))
            modified_python = datetime.now()
            modified_sql = modified_python.strftime("%Y-%m-%d")
            database_commands.newEntry(loginID, username, password, link, comment, modified_sql)
        case 2: 
            os.system('clear')
            print(">> What entry would you like to modify?\n")
            loginID = app_auth.getLoginID()
            database_commands.modifyEntry(loginID)
            user_selection = input(">> ").split(",")
            for selection in user_selection:
                is_valid = database_commands.queryEntryID(selection)
                if int(selection) == is_valid:
                    print(">> You have selected a valid id")
                else:
                    print(f"Entry with the id '{selection}' is not a valid entry!")
                
        case 3:
            print("You have chosen to delete an existing entry.")
        case 4:
            print("You have chosen to view an existing entry.")
        case _:
            print("You have not selected a valid option.")

def main():
    mainMenu()
    userOptions()

main()