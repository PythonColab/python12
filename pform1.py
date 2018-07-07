# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 18:58:14 2018

@author: SURAJ
"""
#Main Page
from tkinter import *

root=Tk()
root.title("Welcome To Library Managment")
root.geometry("500x200")
root.configure(background='green')

b1=Button(text="STUDENT", activebackground="red" , bd=10 , height=5 ,width=20, command=gort).place(x=70,y=50)
b2=Button(text="ADMIN",activebackground="red", bd=10 , height=5 ,width=20).place(x=270,y=50)
root.mainloop()

def gort():
    from tkinter import filedialog
    from os import path
    import tkinter as t
    file = filedialog.askopenfilename(initialdir= path.dirname("C:\\Users\\SURAJ\\.spyder-py3\\pforms.py"))

    sw=t.Tk()
    sw.title("second screen")

    # file = filedialog.askopenfilename(initialdir= path.dirname(""))
    sw.mainloop() 
