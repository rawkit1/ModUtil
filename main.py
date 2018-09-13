"""
ModUtil for 1.12
By enwash

Do distribute
"""
from tkinter import *
from libs.model_blockstate import main as mb
from libs.recipe import main as rg

master = Tk()
master.configure(background='dark slate blue')
master.minsize(300, 140)
master.title("ModUtil")

br = Label(master, text="\n", bg="dark slate blue")
b1 = Button(master, text="Recipe Generator", command=rg, bg="white", fg="dark slate blue", font=("Consolas", 12, "bold"))
b2 = Button(master, text="Model/Blockstate Generator", command=mb, bg="white", fg="dark slate blue", font=("Consolas", 12, "bold"))

br.pack()
b1.pack()
b2.pack()
br.pack()

mainloop()
