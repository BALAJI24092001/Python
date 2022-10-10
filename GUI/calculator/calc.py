import tkinter as tk
root = tk.Tk()
root.title('CALCULATOR')

in1 = tk.Entry(root, width=30)
in1.grid(row=0, column=0, columnspan=4)
i = 0
evaluate = str()
def evalu(inp):
    val = str(in1.get())
    in1.delete(0, tk.END)
    in1.insert(0, val+inp)

def equals():
    val = in1.get()
    in1.delete(0, tk.END)
    in1.insert(0, eval(val))

def clear():
    in1.delete(0, tk.END)

wid = 3
hei = 2

butClear = tk.Button(root, text = 'C', width=wid, height=hei, command= lambda: evalu("clear"))
butDiv = tk.Button(root, text = '/', width=wid, height=hei, command= lambda: evalu("/"))
butMul = tk.Button(root, text = '*', width=wid, height=hei, command= lambda: evalu("*"))
butSub = tk.Button(root, text = '-', width=wid, height=hei, command= lambda: evalu("-"))

but7 = tk.Button(root, text = '7', width=wid, height=hei, command= lambda: evalu("7"))
but8 = tk.Button(root, text = '8', width=wid, height=hei, command= lambda: evalu("8"))
but9 = tk.Button(root, text = '9', width=wid, height=hei, command= lambda: evalu("9"))
butPlus = tk.Button(root, text = '+', width=wid, height=5, command= lambda: evalu("+"))

but4 = tk.Button(root, text="4", width=wid, height=hei, command= lambda: evalu("4"))
but5 = tk.Button(root, text="5", width=wid, height=hei, command= lambda: evalu("5"))
but6 = tk.Button(root, text="6", width=wid, height=hei, command= lambda: evalu("6"))

but1 = tk.Button(root, text="1", width=wid, height=hei, command= lambda: evalu("1"))
but2 = tk.Button(root, text="2", width=wid, height=hei, command= lambda: evalu("2"))
but3 = tk.Button(root, text="3", width=wid, height=hei, command= lambda: evalu("3"))
butMod = tk.Button(root, text="mod", width=wid, height=hei+3, command= lambda: evalu("%"))

but0 = tk.Button(root, text="0", width=wid, height=hei, command= lambda: evalu("0"))
bute = tk.Button(root, text="=", width=wid*3, height=hei, command= equals)
#butBack = tk.Button(root, text="clr", width=wid, height=hei, command= lambda: evalu("back"))

butClear.grid(row=1, column=0)
butDiv.grid(row=1, column=1)
butMul.grid(row=1, column=2)
butSub.grid(row=1, column=3)

but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)
butPlus.grid(row=2, column=3, rowspan=2)

but4.grid(row=3, column=0)
but5.grid(row=3, column=1)
but6.grid(row=3, column=2)

but1.grid(row=4, column=0)
but2.grid(row=4, column=1)
but3.grid(row=4, column=2)
butMod.grid(row=4, column=3, rowspan=2)

but0.grid(row=5, column=0)
bute.grid(row=5, column=1, columnspan=2)
#butBack.grid(row=5, column=2)

root.mainloop()

