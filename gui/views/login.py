import customtkinter

class LoginPage(customtkinter.CTkFrame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Login to PassMan")
        self.label.grid(row=0, column=0, columnspan=2)

        self.username_label = customtkinter.CTkLabel(self, text="Username")
        self.password_label = customtkinter.CTkLabel(self, text="Password")
        #self.password_verify_label = customtkinter.CTkLabel(self, text="Re-enter Password")
        self.username_entry = customtkinter.CTkEntry(self)
        self.password_entry = customtkinter.CTkEntry(self, show="*")

        self.username_label.grid(row=1, column=0)
        self.password_label.grid(row=2, column=0)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)
        #self.password_verify_label.grid(row=3, column=0)

        self.login_button = customtkinter.CTkButton(self, text="Login")
        self.login_button.grid(row=3, column=1)

        self.signup_option_label = customtkinter.CTkLabel(self, text="Don't have an account?")
        self.signup_option_label.grid(row=4, column=1)
        self.signup_btn = customtkinter.CTkButton(self, text="Sign Up")
        self.signup_btn.grid(row=5, column=1)
