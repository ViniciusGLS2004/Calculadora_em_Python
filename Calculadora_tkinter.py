from tkinter import *

#cores

cor1 = '#1E1E1E' #outro tipo de preto
cor2 = '#121212' #branco
cor3 = '#FFFFFF' #verde preto escuro
cor4 = '#383838'#cinza escuro
cor5 = '#ffb254' #laranja fraco
cor6 = '#fcfcfc' #branco

janela = Tk()
janela.title("Calculadora")
janela.geometry("449x560")
janela.config(bg=cor1)

# Criando frmaes
frame_tela = Frame(janela, width=449, height=100, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=449, height=560, bg=cor2)
frame_corpo.grid(row=1, column=0)

# variavel todos_valores

todos_valores = ''

#criando label
valor_texto = StringVar()

# criando função
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)

    #passando valor para a tela
    valor_texto.set(todos_valores)

# função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

# função para limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial 32 '), bg=cor3)
app_label.place(x=0,y=0)

# Criando botões
b1 = Button(frame_corpo, command=limpar_tela, text="C", width=20, height=3, bg=cor4, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=10,y=20)
b2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=9, height=3, bg=cor4, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=230,y=20)
b3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=9, height=3, bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=340,y=20)

b4 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=10,y=110)
b5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=120,y=110)
b6 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=230,y=110)
b7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=9, height=3, bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=340,y=110)


b8 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=10,y=200)
b9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=120,y=200)
b10 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=230,y=200)
b11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="_", width=9, height=3, bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=340,y=200)


b12 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=10,y=290)
b13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=120,y=290)
b14 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=230,y=290)
b15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=9, height=3, bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=340,y=290)



b16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=20, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=10,y=380)
b17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=9, height=3, bg=cor4,fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=230,y=380)
b18 = Button(frame_corpo, command = calcular, text="=", width=9, height=3, bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=340,y=380)

janela.mainloop()

#python -m tkinter
#sudo apt-get install python3-tk
#relief: puxar o botão para frente
#overrelief: ação de quando passa o mause por cima
# não tem botão para reverter