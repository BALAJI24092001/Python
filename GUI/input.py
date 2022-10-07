import tkinter as tkin
root = tkin.Tk()
import pandas as pd
tkin.Entry()
df = pd.DataFrame()


input1 = tkin.Entry(root, width = 50, borderwidth=2)
tkin.Entry()
print()

def click():
    mylab = tkin.Label(root, text=input1.get())
    mylab.pack()
butt = tkin.Button(root, text="Submit", command=click, padx=20)
butt.pack()


root.mainloop();
