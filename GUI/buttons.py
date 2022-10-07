import tkinter as tk
root = tk.Tk();

def doSome():
    LabelClick = tk.Label(root, text="Some text")
    LabelClick.pack()

button1 = tk.Button(root, text="Click me!!", padx=30, command=doSome, fg='blue', bg='grey')
# command - to perform action, after button click
# padx - padding in x axis
# pady - padding in y axis
# fg - forground color(text color)
# bg - background color
button1.pack()

root.mainloop()
