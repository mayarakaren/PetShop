from tkinter import *
import tkinter as tk
import bcrypt
import subprocess
import mysql.connector as mysql
from tkinter import messagebox

window = Tk()
window.title("Petz")

#-----------------------------------------------------------------------------------------------------

window.geometry("750x500")
window.resizable(True,True)
window.configure(background='#ffffff')
largura = 300
altura = 120

largura_screen= window.winfo_screenwidth()
altura_screen= window.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

window.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#-----------------------------------------------------------------------------------------------------------------------------

lbl_user = Label(window, text="Usuário:", bg="#ffffff").place(x=10, y=10)
txt_user = Entry(window, width=35, borderwidth=3)
txt_user.place(x=60, y=10)
txt_user.insert(0, "")

lbl_password = Label(window, text="Senha:", bg="#ffffff").place(x=10, y=40)
txt_password = Entry(window)
txt_password = tk.Entry(window, show="*", width=35, borderwidth=3)
txt_password.place(x=60, y=40)
txt_password.insert(0, "")

label_result = tk.Label(window, text="")

database = {}

def cadastro():
    username = txt_user.get()
    password = txt_password.get()

    hash_senha = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if username == "" or hash_senha == "":
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conectar.cursor()
        cursor.execute("INSERT INTO User (username, password) VALUES(%s, %s)", (username, hash_senha.decode('utf-8')))
        conectar.commit()
        messagebox.showinfo("Mensagem", "Cadastro Realizado com sucesso!")
        conectar.close()

def abrir_principal():
    subprocess.run(["python", "Principal.py"])

def login():
    username = txt_user.get()
    password = txt_password.get()

    conectar = mysql.connect(host="localhost", user="root", password="", database="petshop")
    cursor = conectar.cursor()
    cursor.execute("SELECT password FROM User WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]

        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            label_result.config(text="Login realizado com sucesso!")
            window.after(1000, abrir_principal)
        else:
            label_result.config(text="Senha incorreta!")
    else:
        label_result.config(text="Usuário não encontrado!")

login_button = Button(window, text="Login", bg="#6495ED")
login_button.place(x=180, y=80)
login_button.config(command=login)

cad_button = Button(window, text="Cadastrar", bg="#6495ED")
cad_button.place(x=80, y=80)
cad_button.config(command=cadastro)

window.mainloop()