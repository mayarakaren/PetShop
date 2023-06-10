from tkinter import *
import mysql.connector
import tkinter as tk
import pandas as pd

#Configuração da window-----------------------------------------------------------------------------------------------------

window = Tk()
window.title("Consulta")

window.geometry("750x500")
window.resizable(True, True)
window.configure(background="#ffffff")
largura = 700
altura = 500

largura_screen= window.winfo_screenwidth()
altura_screen= window.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

window.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Consulta-------------------------------------------------------------------------------------------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

def consultar():
    cursor = db.cursor()
    query = "SELECT * FROM Clientes"
    cursor.execute(query)
    resultado = cursor.fetchall()

    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    for item in resultado:
        listbox.insert(tk.END, item)

    df = pd.DataFrame(resultado)
    table = tk.Frame(window)
    table.pack(fill=tk.BOTH, expand=True)
    for i, col in enumerate(cursor.column_names):
        tk.Label(table, text=col).grid(row=0, column=i)
    for i, row in df.iterrows():
        for j, val in enumerate(row):
            tk.Label(table, text=val).grid(row=i+1, column=j)

lbl_consultar = Label(window, text="Consultar:", bg="#ffffff").place(x=10, y=10)
txt_consultar = Entry(window, width=80, borderwidth=2, fg="black", bg="white")
txt_consultar.place(x=70, y=10)
txt_consultar.insert(0, "")

#Botões-----------------------------------------------------------------------------------------------------

btn_animais = Button(window, text="Consultar Animais", command=consultar, bg="#90EE90")
btn_animais.place(x=570, y=10)

window.mainloop()