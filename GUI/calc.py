import tkinter as tk
root = tk.Tk()
root.title('CALCULATOR')

inp1 = tk.Entry(root, width = 50)
inp1.grid(columnspan=4)


but1 = tk.Button(root, text = 'C', background='grey', foreground='black', padx=30, pady = 15)
but1.grid(row=1, column=0)

but2 = tk.Button(root, text = '/', background='grey', foreground='black', padx=30, pady = 15)
but2.grid(row=1, column=1)

but3 = tk.Button(root, text = '*', background='grey', foreground='black', padx=30, pady = 15)
but3.grid(row=1, column=2)

but4 = tk.Button(root, text = '-', background='grey', foreground='black', padx=30, pady = 15)
but4.grid(row=1, column=3)

root.mainloop()
