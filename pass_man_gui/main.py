from tkinter import * 

class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        login_frame = Frame(self)
        login_frame.pack(fill=BOTH, expand=True)

        login_button = Button(login_frame, text="Login")
        signin_button = Button(login_frame, text="Sign In")
        login_button.pack(side=TOP)
        signin_button.pack(side=TOP)