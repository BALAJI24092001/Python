import tkinter as tk
from PIL import ImageTk, Image
import os
from PyPDF2 import PdfMerger

root = tk.Tk()
root.geometry("400x400")
root.title("pdf file merger")
def merge():
    global inp1
    mer_dir = str(inp1.get())
    merger = PdfMerger()
    for item in os.listdir(mer_dir):
        if item.endswith("pdf"):
            merger.append(mer_dir + "/" + item)

    merger.write(mer_dir+"/merged.pdf")
    merger.close()

lab1 = tk.Label(root, text="Enter the location of all the pdf files in the below input box.", pady = 30)
but = tk.Button(root, text="submit", padx = 30, command = merge, pady=10, width=30)
inp1 = tk.Entry(root, width=50, borderwidth=2)

lab1.pack()
inp1.pack()
but.pack()

root.mainloop()
