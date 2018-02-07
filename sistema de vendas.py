from tkinter import* 
import random
import time;
import datetime

#https://www.youtube.com/watch?v=gVi7mm51cBU&list=PL2Dw5PtrD32zzkQ1OQyN4gz3I_8G1MMHl&index=5
root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema de vendas")
root.configure(background= 'grey')

#INTERFASE PROGRAMA JANELA ETC...

#FRAME TOPO
Tops = Frame (root, width=1350 , height=100 , bd= 9 , relief= "raise")
Tops.pack(side = TOP)

#FRAME DA ESQUERDA
framef1 = Frame (root, width=900 , height=650 , bd= 8 , relief= "raise")
framef1.pack(side=LEFT)

#FRAMDE DA DIREITA
framef2 = Frame (root, width=440 , height=650 , bd= 8 , relief= "raise")
framef2.pack(side=RIGHT)

#TROCANDO COR DO FUNDO
framef1.configure(background = 'gray')

#ROTULO CABEÇALHO
lblInfo = Label(Tops, font =('arial', 50, 'bold'), text = 'SISTEMA CAFÉ', bd = 8, width=20)
lblInfo.grid(row=0,column=0)

 
# FRAME SECUNDARIOS
frameft2 = Frame (framef2, width=440 , height=650 , bd= 2 , relief= "raise")
frameft2.pack(side=TOP)

framefb2 = Frame (framef2, width=440 , height=50 , bd= 2 , relief= "raise")
framefb2.pack(side=BOTTOM)

framefla = Frame (framef1, width=900 , height=330 , bd= 2 , relief= "raise")
framefla.pack(side=TOP)

framef2a = Frame (framef1, width=900 , height=320 , bd= 2 , relief= "raise")
framef2a.pack(side=BOTTOM)

framef1aa = Frame (framef1a, width=450 , height=330 , bd= 2 , relief= "raise")
framef1aa.pack(side=LEFT)

framef1ab = Frame (framef1a, width=450 , height=330 , bd= 2 , relief= "raise")
framef1ab.pack(side=RIGHT)

#declarando as primeiras variaveis

val1=IntVar()
val1.set("0")
Latta = Checkbutton(framef1aa, text = 'Latta \t', variable=val1, onvalue = 1, offvalue = 0,
                    font =('arial', 18,'bold')).grid(row=0,column=0)


root.mainloop()
