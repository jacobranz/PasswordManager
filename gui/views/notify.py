import customtkinter

class NotifyView():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = customtkinter.CTkLabel(self, text="Notification")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.close_button = customtkinter.CTkButton(self, text="Close")
        self.close_button.grid(row=2, column=0, padx=10, pady=10)