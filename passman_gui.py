from tkinter import * 
from tkinter import messagebox
from app_auth import *
import customtkinter

user_entries = ()

def append_to_list(entry):
    global user_entries
    for i in list(entry):
        user_entries += i

def view_list(entry):
    global user_entries
    for i in list(entry):
        print(i)

class PassMan(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PassMan")

        container = customtkinter.CTkFrame(self, height=500, width=500)
        container.grid(row=0, column=0)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, SignUp, MainPage, TestLoggedIn, Table):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Login to PassMan")
        label.grid(row=0, column=1)

        global loginID

        loginID = StringVar()
        password = StringVar()

        username_label = customtkinter.CTkLabel(self, text="Username")
        password_label = customtkinter.CTkLabel(self, text="Password")
        username_entry = customtkinter.CTkEntry(self, textvariable=loginID)
        password_entry = customtkinter.CTkEntry(self, textvariable=password)

        username_label.grid(row=1, column=0)
        password_label.grid(row=2, column=0)
        username_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)

        login_button = customtkinter.CTkButton(self, text="Login", command=lambda: [login_graphical(loginID.get(), password.get()), controller.show_frame(MainPage)])
        login_button.grid(row=7, column=1)
        switch_window_button = customtkinter.CTkButton(self, text="Sign Up", command=lambda: controller.show_frame(SignUp))
        switch_window_button.grid(row=6, column=1)
        test_button = customtkinter.CTkButton(self, text="Test", command=lambda: [append_to_list(database_commands.queryEntry(loginID.get())) ,view_list(user_entries)])
        test_button.grid(row=8, column=1)
        # command=lambda: [append_to_list(database_commands.queryEntry(loginID.get())), print(user_entries)]

class SignUp(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Sign Up for PassMan")
        label.grid(row=0, column=1)

        new_user = StringVar()
        new_user_pass = StringVar()

        username_label = customtkinter.CTkLabel(self, text="Username")
        password_label = customtkinter.CTkLabel(self, text="Password")
        password_verify_label = customtkinter.CTkLabel(self, text="Re-enter Password")
        username_entry = customtkinter.CTkEntry(self, textvariable=new_user)
        password_entry = customtkinter.CTkEntry(self, textvariable=new_user_pass)

        username_label.grid(row=1, column=0)
        password_label.grid(row=2, column=0)
        username_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)
        password_verify_label.grid(row=3, column=0)

        signup_button = customtkinter.CTkButton(self, text="Sign Up", command=lambda: signUp_graphical(new_user.get(), new_user_pass.get()))
        signup_button.grid(row=7, column=1)
        switch_window_button = customtkinter.CTkButton(self, text="Back to Login", command=lambda: controller.show_frame(LoginPage))
        switch_window_button.grid(row=6, column=1)

class MainPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Welcome to PassMan!")
        label.grid(row=0, column=1)

        view_entries = customtkinter.CTkButton(self, text="View Entries", command=lambda: [controller.show_frame(Table), Table.populate(data=user_entries)])
        view_entries.grid(row=1, column=1)
        modify_entries = customtkinter.CTkButton(self, text="Modify Entries")
        modify_entries.grid(row=2, column=1)
        add_entries = customtkinter.CTkButton(self, text="Add Entries")
        add_entries.grid(row=3, column=1)

class TestLoggedIn(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="You are now logged in!")
        label.grid(row=0, column=1)

class Table(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Table View")
        label.grid(row=0, column=1)
        
    def populate(self, data):
        # code for creating table
        for i in range(len(data)):
            for j in range(len(data[0])):
                
                e = customtkinter.CTkEntry(self)
                
                e.grid(row=i, column=j)
                e.insert(END, data[i][j])

if __name__ == "__main__":
    test = PassMan()
    test.mainloop()