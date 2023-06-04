from tkinter import * 
import tkinter as tk 
import bcrypt
from tkinter import messagebox
import subprocess
import mysql.connector as mysql

tela = Tk()
tela.title("Sofisticão")

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela.geometry("750x500")
tela.resizable(True,True)
tela.configure(background='#ffffff')
largura = 300
altura = 120

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Configuração da tela-----------------------------------------------------------------------------------------------------

Logo = PhotoImage(file= r"views/imgs/logo.png")
LogoLabel = Label(bg="#FFF", image=Logo, compound="top")
LogoLabel.grid(column= 0, row=0, padx = 60, pady=60)

tela.mainloop()