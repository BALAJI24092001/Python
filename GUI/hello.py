import tkinter as tk

root = tk.Tk();

# Creating a label widget
mylabel = tk.Label(root, text="Hello World!");

# shoving it onto the screen
mylabel.pack()

root.mainloop()
