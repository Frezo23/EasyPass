import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Menu
from tkinter import ttk
import os
import glob, os
import os.path
from os import path
import datetime
from tkinter import messagebox
from cryptography.fernet import Fernet
import smtplib
import image

# password = password1.encode()
# encr = Fernet(key)
# encryptedpass = encr.encrypt(password)


email = ''
email1 =''
email2 = ''
password = ''
password1 = ''
password2 = ''
save = False
key = ''
keyuse = ''
log = False

try:
    f = open("save.save")
    key = f.read()
    f.close()
except IOError:
    newkey = Fernet.generate_key() ### generates new key
    f = open('save.save', 'wb')
    f.write(newkey)
    f.close()
    f = open("save.save")
    key = f.read()
    f.close()

def note():
    wronglbl.configure(text='',bg="#00fffb")

def login():
    global email, password, save, key, keyuse, password1, email1, password2, email2, log
    try:
        f = open('user.data', 'rb')
        email1 = f.read()
        f.close()
        f = open('user.info', 'rb')
        password1 = f.read()
        f.close()
        keyuse = Fernet(key)

        email = loginent.get()
        password = passent.get()
        email2 = keyuse.decrypt(email1)
        password2 = keyuse.decrypt(password1)
        email2 = str(email2)
        password2 = str(password2)
        email2 = email2.replace("'",'')
        email2 = email2.replace("b",'')
        password2 = password2.replace("'",'')
        password2 = password2.replace("b",'')

        if email2 == email and password2 == password:
            log = True
            cleanlog()
        else:
            pass
    except IOError:
        wronglbl.configure(text='Ops.. Something went wrong!',bg='#ff3c3c')
        wronglbl.place(x=170,y=350)
        wronglbl.after(5000, note)

def register():
    global email, password, save, key, keyuse, password1, email1, password2, email2, log

    f = open('user.data', 'w+')
    f.close()
    f = open('user.data', 'wb')

    email = loginent.get()
    email1 = email.encode()
    keyuse = Fernet(key)

    email2 = keyuse.encrypt(email1)

    f.write(email2)
    f.close()

    email = ''
    email1 = ''
    email2 = ''

    f = open('user.info', 'w+')
    f.close()
    f = open('user.info', 'wb')

    password = passent.get()
    password1 = password.encode()
    password2 = keyuse.encrypt(password1)

    f.write(password2)
    f.close()
    password = ''
    password1 = ''
    password2 = ''

def zapamietaj():
    global save
    save = True

def cleanlog():
    logolbl.destroy()
    registerbtn.destroy()
    loginlbl.destroy()
    loginent.destroy()
    loginbtn.destroy()
    passent.destroy()
    passlbl.destroy()
    forgotbtn.destroy()
    saverad.destroy()

root = Tk()
root.title('EasyPass')
root.geometry('500x500')
root.resizable(False,False)
root.iconphoto(False, tk.PhotoImage(file='logo.png'))

logo = tk.PhotoImage(file='logo.png')
bg = tk.PhotoImage(file='bg.png')
labelbg= Label(root, image=bg)
labelbg.place(x=0,y=0)

wronglbl = tk.Label(root,borderwidth=0,bg="#00fffb")
wronglbl.place(x=170,y=350)

titlelbl = tk.Label(root, text='EasyPass',font=('Helvetica',30),bg='#29c054')
titlelbl.place(x=160,y=10)

logolbl = tk.Label(root,image=logo,bg="#00fffb")
logolbl.place(x=210,y=65)

loginlbl = tk.Label(root, text='Email/Login',font=('Arial',15),bg="#00fffb")
loginlbl.place(x=50,y=150)

passlbl = tk.Label(root, text='Password',font=('Arial',15),bg="#00fffb")
passlbl.place(x=50,y=190)

loginent = tk.Entry(root,font=('Arial',12),width=30,bg="gray")
loginent.place(x=170,y=155)

passent = tk.Entry(root,font=('Arial',12),width=30,bg="gray")
passent.place(x=170,y=195)

saverad = tk.Checkbutton(root,variable=save,text='Remember me',borderwidth=0,bg="#00fffb",font=('Arial',10),command=zapamietaj)
saverad.place(x=320,y=230)

loginbtn = tk.Button(root, text='Login',font=('Arial',15),width=10,bg="gray",command=login)
loginbtn.place(x=190,y=230)

registerbtn = tk.Button(root, text='Register',font=('Arial',15),width=10,bg="gray",command=register)
registerbtn.place(x=190,y=270)

forgotbtn = tk.Button(root,text='Forgot password',font=('Arial',10,'underline'),borderwidth=0,bg="#00fffb")
forgotbtn.place(x=200,y=390)

conlbl = tk.Label(root,text='Contact: \nEmail: wilczewski.dominik@gmail.com \nDiscord: Frezo#4111 \nGithub: Frezo23',bg='#29c054')
conlbl.place(x=140,y=430)

root.mainloop()