import tkinter as tkin
root = tkin.Tk()
import pandas as pd
tkin.Entry()
df = pd.DataFrame()


input1 = tkin.Entry(root, width = 50, borderwidth=2)
input1.pack()
print()

#def click():
#    mylab = tkin.Label(root, text=input1.get())
#    mylab.pack()

i = 0;
def but1En():
    global i
    input1.insert(i, '1')
    i+=1;
but = tkin.Button(root, text="Submit", command=but1En, padx=20)
but.pack()


root.mainloop();
