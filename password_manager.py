import os
import app_auth
from database_commands import *
from encryption import *
from datetime import datetime
import maskpass

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

def homePage():
        os.system('clear')
        print("""
---------------------------------------------
1. Create new entry
2. Modify entry
3. Delete entry
4. View all entries
5. Exit
---------------------------------------------""")

def userOptions():
    while True: ## Look into changing this loop so it does not overwrite screen output 
        homePage()
        user_choice = int(input(">> "))
        match user_choice:
            case 1:
                while True:
                    print("You have selected to create a new entry.")
                    
                    loginID = app_auth.loginID
                    username = str(input("Enter username: "))
                    password = maskpass.askpass(prompt="Enter password: ")
                    #encryptString(password)
                    link = str(input("Enter link: "))
                    comment = str(input("Comments: "))
                    modified_python = datetime.now()
                    modified_sql = modified_python.strftime("%Y-%m-%d")

                    newEntry(loginID, username, password, link, comment, modified_sql)
                    create_new_entry = 'y'
                    while create_new_entry == 'y':
                        print("\n>> Would you like to create another entry? [y/n]\n")
                        case_1_input = input(">> ")
                        if case_1_input == 'y':
                            os.system('clear')
                            break
                        elif case_1_input == 'n':
                            create_new_entry = 'n'
                        else:
                            print(">> You have not selected a valid option.")
                            continue
                    break
            case 2: 
                os.system('clear')
                print(">> What entry would you like to modify?\n")
                loginID = app_auth.getLoginID()
                queryEntry(loginID)
                user_selection = input(">> ").split(",")
                if user_selection == "exit":
                    break
                modify_options = {}

                for selection in user_selection:
                    is_valid = queryEntryID(selection)

                    if int(selection) == is_valid:
                        print(">> You have selected a valid id")
                        get_column_names = queryEntry(loginID)
                        os.system('clear')

                        querySingleEntry(loginID, selection)
                        i = 1
                        while i < len(get_column_names):
                            for column in get_column_names:
                                print(f"{i}. {column}")
                                modify_options[i]=column
                                i += 1
                        test = input(f"\n>> What value would you like to modify for selection '{selection}'?\n>> ").split(",")
                        if test == "exit":
                            break

                        for x in test:
                            y = str(input(f">> Update '{modify_options[int(x)]}': "))
                            modifyEntry(modify_options[int(x)], y, selection)
                    else:
                        print(f"Entry with the id '{selection}' is not a valid entry!")
                    
            case 3:
                print("You have chosen to delete an existing entry.")
                os.system('clear')
                print(">> What entry would you like to remove?\n")
                loginID = app_auth.getLoginID()
                queryEntry(loginID)
                user_delete_selection = input(">> ").split(",")
                if user_delete_selection == "exit":
                    break

                for selection in user_delete_selection:
                    is_valid = queryEntryID(selection)

                    if int(selection) == is_valid:
                        print(">> You have selected a valid id")
                        get_column_names = queryEntry(loginID)
                        os.system('clear')

                        querySingleEntry(loginID, selection)
                        delete_verify = str(input(f"\n>> Are you sure you want to remove selection '{selection}'? (y/n)\n>> "))
                        if delete_verify.lower() == 'y':
                            removeEntry(loginID, selection)
                        else:
                            break
                    else:
                        print(f"Entry with the id '{selection}' is not a valid entry!")
            case 4:
                os.system('clear')
                loginID = app_auth.loginID
                queryEntry(loginID)
                while True:
                    test = input(">> ")
                    if test == "home":
                        break
            case 5: 
                sys.exit()
            case _:
                print("You have not selected a valid option.")

def main():
    mainMenu()
    userOptions()

main()