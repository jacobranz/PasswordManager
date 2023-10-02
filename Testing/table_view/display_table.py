from tkinter import * 
from tkinter import ttk
import customtkinter

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