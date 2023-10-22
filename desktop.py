import tkinter as tk
from tkinter import messagebox
from tkinter import *
#teste

class Login:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('ENTRAR')
        #self.janela.iconbitmap('icone.ico')
        self.janela['background'] = ('#72F2EB')
        self.janela.geometry('350x150+450+100')
        self.janela.resizable(width=False, height=False)

        self.login=tk.Label(self.janela, text='Login * ', font='verdana 12 bold', background='#72F2EB')
        self.login.grid(column=0, row=0, padx=(70,20), pady=(10))

        self.senha = tk.Label(self.janela, text='Senha * ', font='verdana 12 bold', background='#72F2EB')
        self.senha.grid(column=0, row=1,padx=(70, 20) )

        self.campo1 = tk.Entry(self.janela)
        self.campo1.grid(column=1, row=0)
        self.campo2 = tk.Entry(self.janela)
        self.campo2.grid(column=1, row=1)

        self.botao1 = tk.Button(self.janela, text='Entrar', width=15, command=self.verifica)
        self.botao1.grid(column=1, row=2, pady=25)


    def verifica(self):
        nome = self.campo1.get()
        senha=self.campo2.get()

        if nome == 'joao' and senha == 'maria':
            self.iniciar()
        elif nome == '' or senha == '':
            messagebox.showinfo('Caixa de Mensagem', 'Preencha os campos obrigatórios')
        else:
            messagebox.showwarning('Erro', 'Email ou senha errado')

    def iniciar(self):
        self.janela1 = Tk()
        #self.janela1 = self.janela1
        self.janela1['background'] = ('#008F8C')
        self.janela1.geometry('800x500+320+100')
        self.janela1.resizable(width=False, height=False)
        self.janela1.focus_force()  # dando foco na tela
        self.janela.destroy()
        self.janela1.mainloop()


janela = tk.Tk()
objeto = Login(janela)
janela.mainloop()
