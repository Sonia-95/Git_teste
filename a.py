import tkinter as tk
from tkinter import *

janela = Tk()
janela.title('ENTRAR')
janela['background'] = ('#72F2EB')
janela.geometry('350x150+450+100')


texto = tk.Text(janela, width=20, height=5)
texto.pack()

janela.mainloop()

#ok
