from tkinter import * 
from tkinter import ttk
import customtkinter

class Table(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label = customtkinter.CTkLabel(self, text="Table View")
        label.grid(row=0, column=1)


        root = customtkinter.CTk()

        tree = ttk.Treeview(root, column=("First", "Last", "Age"))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="First")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Last")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Age")

        tree.insert('', 'end', text="1", values=("Jake", "Ranz", "21"))

        tree.pack()

        root.mainloop()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = Table(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()