import tkinter as tk
root = tk.Tk()
root.title('CALCULATOR')

in1 = tk.Entry(root, width=30)
in1.grid(row=0, column=0, columnspan=4)
i = 0
def test(num) -> None:
    global i
    in1.insert(i, num)
    i+= 1

butClear = tk.Button(root, text = 'C', width=3, height=2)
butDiv = tk.Button(root, text = '/', width=3, height=2)
butMul = tk.Button(root, text = '*', width=3, height=2 )
butSub = tk.Button(root, text = '-', width=3, height=2 )


but7 = tk.Button(root, text = '7', width=3, height=2 )
but8 = tk.Button(root, text = '8', width=3, height=2 )
but9 = tk.Button(root, text = '9', width=3, height=2, command= lambda: test(9))
butPlus = tk.Button(root, text = '+', width=3, height=5, command= lambda: test('+'))

but4 = tk.Button(root, text="4", width=3, height=2)
but5 = tk.Button(root, text="5", width=3, height=2)
but6 = tk.Button(root, text="6", width=4, height=2)

but1 = tk.Button(root, text="1", width=3, height=2)
but2 = tk.Button(root, text="2", width=3, height=2)
but3 = tk.Button(root, text="3", width=3, height=2)
butMod = tk.Button(root, text="mod", width=3, height=5 )

but0 = tk.Button(root, text="0", width=11, height=2)
butBack = tk.Button(root, text="clr", width=3, height=2)

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

but0.grid(row=5, column=0, columnspan=2)
butBack.grid(row=5, column=2)

root.mainloop()

