from tkinter import * 
from tkinter import messagebox
from app_auth import *

class PassMan(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("PassMan")

        container = Frame(self, height=500, width=500)
        container.grid(row=0, column=0)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, SignUp):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Login to PassMan")
        label.grid(row=0, column=1)

        loginID = StringVar()
        password = StringVar()

        username_label = Label(self, text="Username")
        password_label = Label(self, text="Password")
        username_entry = Entry(self, textvariable=loginID)
        password_entry = Entry(self, textvariable=password)

        username_label.grid(row=1, column=0)
        password_label.grid(row=2, column=0)
        username_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)

        login_button = Button(self, text="Login", command=lambda: login_graphical(loginID.get(), password.get()))
        login_button.grid(row=7, column=1)
        switch_window_button = Button(self, text="Sign Up", command=lambda: controller.show_frame(SignUp))
        switch_window_button.grid(row=6, column=1)

class SignUp(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Sign Up for PassMan")
        label.grid(row=0, column=1)

        new_user = StringVar()
        new_user_pass = StringVar()

        username_label = Label(self, text="Username")
        password_label = Label(self, text="Password")
        password_verify_label = Label(self, text="Re-enter Password")
        username_entry = Entry(self, textvariable=new_user)
        password_entry = Entry(self, textvariable=new_user_pass)

        username_label.grid(row=1, column=0)
        password_label.grid(row=2, column=0)
        username_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)
        password_verify_label.grid(row=3, column=0)

        signup_button = Button(self, text="Sign Up", command=lambda: signUp_graphical(new_user.get(), new_user_pass.get()))
        signup_button.grid(row=7, column=1)
        switch_window_button = Button(self, text="Back to Login", command=lambda: controller.show_frame(LoginPage))
        switch_window_button.grid(row=6, column=1)


if __name__ == "__main__":
    test = PassMan()
    test.mainloop()