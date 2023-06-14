from tkinter import * 

class PassMan(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("PassMan")

        container = Frame(self, height=300, width=300)
        container.pack(side="top", fill="both", expand=True)
        
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
        label.pack(padx=10, pady=10)

        username_label = Label(self, text="Username")
        password_label = Label(self, text="Password")
        username_entry = Entry(self)
        password_entry = Entry(self)

        username_label.pack(side="left")
        password_label.pack(side="left")
        username_entry.pack(side="left")
        password_entry.pack(side="left")

        switch_window_button = Button(self, text="Sign Up", command=lambda: controller.show_frame(SignUp))
        switch_window_button.pack(side="bottom", fill=X)

class SignUp(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Sign Up for PassMan")
        label.pack(padx=10, pady=10)

        switch_window_button = Button(self, text="Back to Login", command=lambda: controller.show_frame(LoginPage))
        switch_window_button.pack(side="bottom", fill=X)

if __name__ == "__main__":
    test = PassMan()
    test.mainloop()