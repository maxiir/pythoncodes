from translate import Translator
from tkinter import*

root=Tk()
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

def traductor():
    idioma= Translator(to_lang="es")
    lo_traducido= idioma.translate(traducir.get())
    traduccion.set(lo_traducido)

traducir=StringVar()
traduccion=StringVar()

Label(frame1,text='Que desea traducir?:').grid(row=0,column=0)
Entry(frame1,textvariable=traducir).grid(row=0,column=1)

Entry(frame1,textvariable=traduccion).grid(row=1,column=1)
Button(frame2,text='traducir',command=traductor).grid(row=0,columnspan=3)


root.mainloop()