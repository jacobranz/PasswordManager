from tkinter import * 
from tkinter import ttk
import customtkinter

class Table(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label = customtkinter.CTkLabel(self, text="Table View")
        label.grid(row=0, column=0, columnspan=2, pady=10)


        root = customtkinter.CTk()

        label_id = customtkinter.CTkLabel(root, text="ID").grid(row=1, column=0)

        root.mainloop()
t = Table()
t.mainloop()