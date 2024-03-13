# Detector de sardinha
from tkinter import *
from PIL import ImageTk, Image  
def simsardinha():
    respostasardinha["text"] = simString

simString = ("Você é uma sardinha")

def naosardinha():
    respostasardinha["text"] = naoString

naoString = ("Você NÃO é uma sardinha")

janela = Tk()
janela.title("Detector de Sardinha")
janela.geometry("450x300")
titulosardinha = Label(janela, text="Você é uma sardinha?")
titulosardinha.grid(column=1, row=0, padx=5, pady=10)

botaosim = Button(janela, text="Sim", command=simsardinha)
botaonao = Button(janela, text="Não", command=naosardinha)
botaosim.grid(column=0, row=1, padx=20, pady=10)
botaonao.grid(column=2, row=1, padx=20, pady=10)

respostasardinha = Label(janela, text="")
respostasardinha.grid(column=1, row=2)

sardinhafoto = ImageTk.PhotoImage(Image.open("sardinha.jpg"))
imagemsardinha = Label(janela,image= sardinhafoto) 
imagemsardinha.grid(column=1 ,row=3)

janela.mainloop()