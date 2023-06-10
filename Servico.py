from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
import subprocess
import mysql.connector
from io import BytesIO
from tkinter import MessageBox

#Configuração da window-----------------------------------------------------------------------------------------------------

window = Tk()
window.title("Gestão de Serviços")

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
lbl_tit = Label(window, text="Gestão de Serviços", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

def create():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    tipo = comboservico.get()
    valor = txt_valor.get()
    tempo = txt_tempo.get()
    desc = text_area.get("1.0", END)

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    comboservico.set("")
    txt_valor.delete(0, tk.END)
    txt_tempo.delete(0, tk.END)
    text_area.delete('1.0', tk.END)

    if(codigo == "" or nome == "" or tipo == "" or valor == "" or tempo == "" or desc == ""):
        MessageBox.showinfo("Erro", "Há campos em branco")
        window.destroy()
    else:
        conectar = mysql.connect(host= "localhost", user="root", password="", database="petshop")
        cursor = conectar.cursor()
        cursor.execute("INSERT INTO Servico VALUES('" + codigo + "', '" + nome + "','" + tipo + "', '" + valor + "','" + tempo + "','" + desc + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Cadastro Realizado com sucesso!")
        conectar.close()

def delete():
    if(txt_codigo.get() == ""):
        MessageBox.showinfo("ALERT", "Digite o código para deletar")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM Servico WHERE cod='"+ txt_codigo.get() +"'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação Excluída com Sucesso!")
        conectar.close()

def update():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    tipo = comboservico.get()
    valor = txt_valor.get()
    tempo = txt_tempo.get()
    desc = text_area.get("1.0", END)

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    comboservico.set("")
    txt_valor.delete(0, tk.END)
    txt_tempo.delete(0, tk.END)
    text_area.delete('1.0', tk.END)

    if(codigo == "" or nome == "" or tipo == "" or valor == "" or tempo == "" or desc == ""):
        MessageBox.shoinfo("ALERT", "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conectar.cursor()
        cursor.execute("UPDATE Servico SET nome = '"+ nome + "', tipo = '" + tipo + "', valor = '" + valor + "', tempo = '" + tempo + "', descricao = '" + desc + "' WHERE codigo='"+ codigo + "'")
        cursor.execute("commit")

    MessageBox.showinfo("Status", "Atualização feita com sucessão!")
    conectar.close()

def abrir_consultaServico():
    subprocess.run(["python", "ConsultarServico.py"])

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

#Serviços estéticos: banhos, hidratação, tosa na máquina, tosa na tesoura, tosa higiênica, desembaraçamento, tingimento #dos pelos, escovação de dentes, limpeza de ouvido e corte de unhas.
#Bem estar: dog walker/passeador, prática de esportes guiada como natação e corridas, ioga, acupuntura e fitoterápicos 
#(sessões de relaxamento).
#Serviços Médicos: consultas clínicas gerais e especialidades, atendimento domiciliar, vacinação, preventivos e cirurgias.
#Educação: adestramento e hospedagem (aprendizagem de convívio com outros animais).

#Tipo de Serviço-----------------------------------------------------------------------------------------------------

lbl_servico = Label(window, text="Tipo:", bg="#ffffff").place(x=130, y=200)
comboservico = ttk.Combobox(window, 
                            values=[
                                    "Serviços Estéticos", 
                                    "Bem-Estar",
                                    "Serviços Médicos",
                                    "Educação"],)

comboservico.grid(column=0, row=1)
comboservico.place(x=190 , y=200)

#Valor-----------------------------------------------------------------------------------------------------
lbl_valor = Label(window, text="Valor:", bg="#ffffff").place(x=130, y=230)
txt_valor = Entry(window, width=40, borderwidth=2, fg="black", bg="white")
txt_valor.place(x=190, y=230)
txt_valor.insert(0, "valor")

#Tempo de duração-----------------------------------------------------------------------------------------------------
lbl_tempo = Label(window, text="Tempo de Duração:", bg="#ffffff").place(x=130, y=260)
txt_tempo = Entry(window, width=40, borderwidth=2, fg="black", bg="white")
txt_tempo.place(x=240, y=260)
txt_tempo.insert(0, "")

#Descrição-----------------------------------------------------------------------------------------------------

lbl_desc = Label(window, text="Descrição:", bg="#ffffff").place(x=130, y=290)
text_area = tk.Text(window, height=5, width=45, font=('Arial', 12),
                    fg='black', bg='white')
text_area.pack()
text_area.place(x=190, y=290)

#Imagem-----------------------------------------------------------------------------------------------------

pasta_inicial = PhotoImage(file = r"")

def escolher_imagem():

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg; *.jpeg; *.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(window, image=imagem_tk)
    lbl_imagem.image= imagem_tk
    lbl_imagem.place(x=10, y=50)

    try:
        conexao = mysql.connector.connect(host="localhost", user="root", password="", database="petshop")
        cursor = conexao.cursor()

        # Converter a imagem para bytes
        stream = BytesIO()
        imagem_pil.save(stream, format="JPEG")
        imagem_bytes = stream.getvalue()

        # Inserir a imagem na tabela do banco de dados
        cursor.execute("INSERT INTO imagem (imagem_servico) VALUES (%s)", (imagem_bytes,))
        conexao.commit()

        cursor.close()
        conexao.close()

        MessageBox("Informação", "Imagem salva com sucesso no banco de dados!")

    except mysql.connector.Error as erro:
         MessageBox("Informação","Erro ao salvar a imagem no banco de dados:", erro)

#Botões-----------------------------------------------------------------------------------------------------

btn_escolher = Button(window, text="Escolher imagem", command=escolher_imagem, bg="#90EE90")
btn_escolher.place(x=10, y=200)

#Ícones-----------------------------------------------------------------------------------------------------

foto_salvar = PhotoImage(file=r"img\save.png")
foto_excluir = PhotoImage(file=r"img\delete.png")
foto_alterar = PhotoImage(file=r"img\edit.png")
foto_consultar = PhotoImage(file=r"img\search.png")
foto_sair = PhotoImage(file=r"img\logout.png")

#Botões-----------------------------------------------------------------------------------------------------

btn_salvar = Button(window, text="Salvar", image= foto_salvar, compound= TOP, bg="#90EE90",command=create).place(x=130, y=410)
btn_alterar = Button(window, text="Alterar", image= foto_alterar, compound= TOP, bg="#6495ED", command=update).place(x=200, y=410)
btn_consultar = Button(window, text="Consultar", image= foto_consultar, compound= TOP, bg="#F0E68C", command=abrir_consultaServico).place(x=270, y=410)
btn_excluir = Button(window, text="Excluir", image= foto_excluir, compound= TOP, bg="#FF6347", command=delete).place(x=340, y=410)
btn_sair = Button(window, text="Sair", image= foto_sair, compound= RIGHT, bg="#000000", fg="white", height=40, width=70, anchor="center", command=window.quit).place(x=620, y=440)

window.mainloop()