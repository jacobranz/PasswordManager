import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class PassMan(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("PassMan")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)