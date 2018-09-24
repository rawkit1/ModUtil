# UI System for Model/Blockstate Generator
import time
import os
from os.path import join as pjoin
from tkinter import *
from model_blockstate import main

master = Tk()
master.configure(background='dark slate blue')
master.minsize(300, 140)
master.title("ModUtil")
arg1 = ""
arg2 = ""
br = Label(master, text="\n", bg="dark slate blue")
text_1 = Entry(master, textvariable=arg1)
text_2 = Entry(master, textvariable=arg2)
br.pack()
text_1.pack()
text_2.pack()
mb=main(arg1,arg2)
b2 = Button(master, text="Generate", command=mb, bg="white", fg="dark slate blue", font=("Consolas", 12, "bold"))
b2.pack()
br.pack()

mainloop()
