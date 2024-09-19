import tkinter as tk
root = tk.Tk()

myLabel1 = tk.Label(root, text="This is smaple text.")
myLabel2 = tk.Label(root, text="This is another sample text.")
myLabel3 = tk.Label(root, text="        space         ")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)

root.mainloop();

