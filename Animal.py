from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
import subprocess
import mysql.connector
import cv2
import numpy as np
from io import BytesIO
from tkinter import messagebox

#Configuração da window-----------------------------------------------------------------------------------------------------

window = Tk()
window.title("Gestão dos Donos")


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

#Título-----------------------------------------------------------------------------------------------------
lbl_tit = Label(window, text="Gestão de Animais", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

#Código-----------------------------------------------------------------------------------------------------
lbl_codigo = Label(window, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)
txt_codigo.insert(0, "Código")

#Nome-----------------------------------------------------------------------------------------------------
lbl_nome = Label(window, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry(window, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "Digite o nome")

#Idade-----------------------------------------------------------------------------------------------------
lbl_idade = Label(window, text="Idade:", bg="#ffffff").place(x=480, y=170)
txt_idade = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=520, y=170)
txt_idade.insert(0, "")

#Sexo-----------------------------------------------------------------------------------------------------
Label(window, text="Sexo:", bg="#ffffff").place(x=130, y=200)

sexo = StringVar()
sexo.set("m")

rdb_buttonm = Radiobutton(window, text="M", variable="var_radio", value="m", bg="#ffffff")
rdb_buttonf = Radiobutton(window, text="F", variable="var_radio", value="f", bg="#ffffff")
rdb_buttonm.place(x=165 , y=200)
rdb_buttonf.place(x=200 , y=200)

#Raça-----------------------------------------------------------------------------------------------------

lbl_raca = Label(window, text="Raça:", bg="#ffffff").place(x=250, y=200)
txt_raca = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_raca.place(x=290, y=200)
txt_raca.insert(0, "Não Definido")

#Peso-----------------------------------------------------------------------------------------------------

lbl_peso = Label(window, text="Peso:", bg="#ffffff").place(x=420, y=200)
txt_peso = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_peso.place(x=460, y=200)
txt_peso.insert(0, "Kg")

#Espécie-----------------------------------------------------------------------------------------------------

lbl_especie = Label(window, text="Espécie:", bg="#ffffff").place(x=130, y=230)
comboEspecie = ttk.Combobox(window, 
                            values=[
                                    "Cachorro", 
                                    "Gato",
                                    "Passáro",
                                    "Roedores"],)

comboEspecie.grid(column=0, row=1)
comboEspecie.place(x=180 , y=230)

#Data de nascimento-----------------------------------------------------------------------------------------------------

lbl_data = Label(window, text="Data de nascimento:", bg="#ffffff").place(x=330, y=230)
txt_data = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_data.place(x=450, y=230)
txt_data.insert(0, "Data")

#Data de Cadastro-----------------------------------------------------------------------------------------------------

lbl_cad = Label(window, text="Data de cadastro:", bg="#ffffff").place(x=130, y=260)
txt_cad = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_cad.place(x=230, y=260)
txt_cad.insert(0, "Data")

#Data de Atulização-----------------------------------------------------------------------------------------------------

lbl_at = Label(window, text="Data de atulização:", bg="#ffffff").place(x=380, y=260)
txt_at = Entry(window, width=20, borderwidth=2, fg="black", bg="white")
txt_at.place(x=490, y=260)
txt_at.insert(0, "Data")

#Descrição-----------------------------------------------------------------------------------------------------

lbl_desc = Label(window, text="Descrição:", bg="#ffffff").place(x=130, y=290)
text_area = tk.Text(window, height=5, width=50, font=('Arial', 12),
                    fg='black', bg='white')
text_area.pack()
text_area.place(x=200, y=290)

#Imagem-----------------------------------------------------------------------------------------------------

def Simples(rotacao_image, angulo):
    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]
    y, x = altura / 2, largura / 2
    rotacao_matriz = cv2.getRotationMatrix2D((x, y), angulo, 1.0)
    rotacionando_image = cv2.warpAffine(rotacao_image, rotacao_matriz, (largura, altura))
    return rotacionando_image

lbl_imagem = None
imagem_original = None

def escolher_imagem():
    global lbl_imagem, imagem_original
    pasta_inicial = PhotoImage(file=r"")

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg; *.jpeg; *.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_original = Image.open(caminho_imagem)
    largura, altura = imagem_original.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_original = imagem_original.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_original)
    
    if lbl_imagem is None:
        lbl_imagem = Label(window, image=imagem_tk)
        lbl_imagem.image = imagem_tk
        lbl_imagem.place(x=10, y=50)
    else:
        lbl_imagem.configure(image=imagem_tk)
        lbl_imagem.image = imagem_tk

def rotacionar_imagem(imagem_pil, angulo):
    imagem_cv2 = cv2.cvtColor(np.array(imagem_pil), cv2.COLOR_RGB2BGR)
    imagem_rotacionada = Simples(imagem_cv2, angulo)
    imagem_pil_rotacionada = Image.fromarray(cv2.cvtColor(imagem_rotacionada, cv2.COLOR_BGR2RGB))
    return imagem_pil_rotacionada

def salvar_imagem_rotacionada(imagem_pil_rotacionada):
    try:
        conexao = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conexao.cursor()

        # Converter a imagem para bytes
        stream = BytesIO()
        imagem_pil_rotacionada.save(stream, format="JPEG")
        imagem_bytes = stream.getvalue()

        # Rotacionar a imagem em 90 graus
        imagem_rotacionada = rotacionar_imagem(imagem_pil_rotacionada, angulo=180)

        # Converter a imagem rotacionada para bytes
        stream_rotacionada = BytesIO()
        imagem_rotacionada.save(stream_rotacionada, format="JPEG")
        imagem_rotacionada_bytes = stream_rotacionada.getvalue()

        # Inserir a imagem rotacionada na tabela do banco de dados
        cursor.execute("INSERT INTO imgAnimal (imagem_animal) VALUES (%s)", (imagem_rotacionada_bytes,))
        conexao.commit()

        cursor.close()
        conexao.close()

        messagebox.showinfo("Informação", "Imagem salva com sucesso no banco de dados!")

    except mysql.connector.Error as erro:
        messagebox.showinfo("Informação", "Erro ao salvar a imagem no banco de dados:", erro)

def rotacionar_e_salvar_imagem(imagem_pil_rotacionada):
    angulo = 180
    imagem_rotacionada = rotacionar_imagem(imagem_pil_rotacionada, angulo)
    salvar_imagem_rotacionada(imagem_rotacionada)

    # Atualizar a imagem no widget lbl_imagem
    imagem_tk_rotacionada = ImageTk.PhotoImage(imagem_rotacionada)
    lbl_imagem.configure(image=imagem_tk_rotacionada)
    lbl_imagem.image = imagem_tk_rotacionada

def btn_rotacao_click():
    global lbl_imagem, imagem_original
    pasta_inicial = PhotoImage(file=r"")
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg; *.jpeg; *.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_original = Image.open(caminho_imagem)
    largura, altura = imagem_original.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_original = imagem_original.resize((110, nova_altura))
    imagem_pil_rotacionada = rotacionar_imagem(imagem_original, angulo=180)
    rotacionar_e_salvar_imagem(imagem_pil_rotacionada)

def alterar_imagem(id_animal, nova_imagem_pil):
    try:
        conexao = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conexao.cursor()

        # Converter a nova imagem para bytes
        stream = BytesIO()
        nova_imagem_pil.save(stream, format="JPEG")
        nova_imagem_bytes = stream.getvalue()

        # Atualizar a imagem do cliente no banco de dados
        cursor.execute("UPDATE imgAnimal SET imagem_animal = %s WHERE idImg = %s", (nova_imagem_bytes, id_animal))
        conexao.commit()

        cursor.close()
        conexao.close()

        messagebox.showinfo("Informação", "Imagem do Animal alterada com sucesso!")

    except mysql.connector.Error as erro:
        messagebox.showinfo("Informação", "Erro ao alterar a imagem do Animal:", erro)

def excluir_imagem(id_animal):
    try:
        conexao = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conexao.cursor()

        # Excluir a imagem do cliente do banco de dados
        cursor.execute("UPDATE imgAnimal SET imagem_animal = NULL WHERE idImg = %s", (id_animal,))
        conexao.commit()

        cursor.close()
        conexao.close()

        messagebox.showinfo("Informação", "Imagem do Animal excluída com sucesso!")

    except mysql.connector.Error as erro:
        messagebox.showinfo("Informação", "Erro ao excluir a imagem do Animal:", erro)

#Botões-----------------------------------------------------------------------------------------------------

btn_escolher = Button(window, text="Escolher imagem", command=escolher_imagem, bg="#90EE90")
btn_escolher.place(x=10, y=200)

btn_rotacao = Button(window, text="Rotacionar imagem", command=btn_rotacao_click, bg="#90EE90")
btn_rotacao.place(x=10, y=250)

btn_alter = Button(window, text="Alterar imagem", command=alterar_imagem, bg="#90EE90")
btn_alter.place(x=10, y=300)

btn_delete = Button(window, text="Excluir imagem", command=excluir_imagem, bg="#90EE90")
btn_delete.place(x=10, y=350)

#Ícones-----------------------------------------------------------------------------------------------------

foto_salvar = PhotoImage(file=r"img\save.png")
foto_excluir = PhotoImage(file=r"img\delete.png")
foto_alterar = PhotoImage(file=r"img\edit.png")
foto_consultar = PhotoImage(file=r"img\search.png")
foto_sair = PhotoImage(file=r"img\logout.png")

#Banco-----------------------------------------------------------------------------------------------------

def create():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexy = sexo.get()
    raca = txt_raca.get()
    peso = txt_peso.get()
    especie = comboEspecie.get()
    data = txt_data.get()
    cad = txt_cad.get() 
    at = txt_at.get()
    desc = text_area.get()

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_raca.delete(0, tk.END)
    txt_peso.delete(0, tk.END)
    comboEspecie.set("")
    txt_data.delete(0, tk.END)
    txt_cad.delete(0, tk.END)
    txt_at.delete(0, tk.END)
    text_area.delete('1.0', tk.END)
    sexo.set("")

    if(codigo == "" or nome == "" or idade == "" or sexy == "" or raca == "" or peso == "" or especie == "" or data == "" or cad == "" or at == "" or desc == ""):
        messagebox.showinfo("Erro", "Há campos em branco")
        window.destroy()
    else:
        conectar = mysql.connect(host= "localhost", user="root", password="", database="petshop")
        cursor = conectar.cursor()
        codigo = str(codigo)
        idade = str(idade)
        cursor.execute("INSERT INTO Animais VALUES('" + codigo + "', '" + nome + "',  '" + idade + "',  '" + sexy + "',  '" + raca + "',  '" + peso + "',  '" + especie + "',  '" + data + "',  '" + cad + "',  '" + at + "',  '" + desc + "')")
        cursor.execute("commit")
        messagebox.showinfo("Mensagem", "Cadastro Realizado com sucesso!")
        conectar.close()

def delete():
    if(txt_codigo.get() == ""):
        messagebox.showinfo("ALERT", "Digite o código para deletar")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")

        cursor = conectar.cursor()
        cursor.execute("DELETE FROM Clientes WHERE cod='"+ txt_codigo.get() +"'")
        cursor.execute("commit")
        messagebox.showinfo("Mensagem", "Informação Excluída com Sucesso!")
        conectar.close()

def update():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexy = sexo.get()
    raca = txt_raca.get()
    peso = txt_peso.get()
    especie = comboEspecie.get()
    data = txt_data.get()
    cad = txt_cad.get() 
    at = txt_at.get()
    desc = text_area.get()

    if(codigo == "" or nome == "" or idade == "" or sexy == "" or raca == "" or peso == "" or especie == "" or data == "" or cad == "" or at == "" or desc == ""):
        messagebox.shoinfo("ALERT", "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")

        cursor = conectar.cursor()
        cursor.execute("UPDATE Animais SET nome = '"+ nome + "', idade= '"+ idade + "', sexo= '"+ sexy + "', raca= '"+ raca + "',  peso= '"+ peso + "',  especie= '"+ especie + "',  data= '"+ data + "',  cadastro= '"+ cad + "', atualizacao= '"+ at + "',  descricao= '"+ desc + "', WHERE codigo='"+ codigo + "'")
        cursor.execute("commit")

    messagebox.showinfo("Status", "Atualização feita com sucessão!")
    conectar.close()

def abrir_consultaAnimais():
    subprocess.run(["python", "windowConsultaAnimais.py"])

#Botões-----------------------------------------------------------------------------------------------------

btn_salvar = Button(window, text="Salvar", image= foto_salvar, compound= TOP, bg="#90EE90", command=create).place(x=130, y=410)
btn_alterar = Button(window, text="Alterar", image= foto_alterar, compound= TOP, bg="#6495ED", command=update).place(x=200, y=410)
btn_consultar = Button(window, text="Consultar", image= foto_consultar, compound= TOP, bg="#F0E68C", command=abrir_consultaAnimais).place(x=270, y=410)
btn_excluir = Button(window, text="Excluir", image= foto_excluir, compound= TOP, bg="#FF6347", command=delete).place(x=340, y=410)
btn_sair = Button(window, text="Sair", image= foto_sair, compound= RIGHT, bg="#000000", fg="white", height=40, width=70, anchor="center", command=window.quit).place(x=620, y=440)

window.mainloop()