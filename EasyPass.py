import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import ttk
import os
import datetime
from tkinter import messagebox
from cryptography.fernet import Fernet
import smtplib

root = Tk()
root.title('EasyPass')
root.geometry('500x500')

titlelbl = tk.Label(root, text='EasyPass',font=('Helvetica',30))
titlelbl.place(x=160,y=10)

loginlbl = tk.Label(root, text='Email/Login',font=('Arial',15))
loginlbl.place(x=80,y=150)

passlbl = tk.Label(root, text='Password',font=('Arial',15))
passlbl.place(x=80,y=190)

loginent = tk.Entry(root,font=('Arial',15))
loginent.place(x=200,y=150)

passent = tk.Entry(root,font=('Arial',15))
passent.place(x=200,y=190)

root.mainloop()