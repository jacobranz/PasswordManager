import customtkinter

class SignUp(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Sign Up for PassMan")
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

        self.has_agreed = customtkinter.BooleanVar()
        self.agreement = customtkinter.CTkCheckBox(
            self,
            text="I have agreed to the Terms & Conditions",
            variable=self.has_agreed,
            onvalue=True,
            offvalue=False
        )
        self.agreement.grid(row=4, column=1, padx=0, sticky="w")
        
        self.signup_button = customtkinter.CTkButton(self, text="Sign Up")
        self.signup_button.grid(row=5, column=1)

        self.signin_option_label = customtkinter.CTkLabel(self, text="Already have an account?")
        self.signin_option_label.grid(row=6, column=1)
        self.signin_button = customtkinter.CTkButton(self, text="Login")
        self.signin_button.grid(row=7, column=1)