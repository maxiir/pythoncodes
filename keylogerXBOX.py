
import sqlite3
import random
from tkinter import*
from tkinter import messagebox
'''
cod_full=""

def salir():
    root.destroy()


def keys():
    global cod_full
    
    #caracteres=['a','b','c','d','e','f','g','h','i','j','k','n','l','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','N','L','O','P','Q','R','S','T','U','V','W','X','Y','Z','L','2','3','4','5','6','7','8','9']
    caracteres=['C','D','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y','Z','2','3','4','6','7','9']#MICROSOFT
    #caracteres=['B','C','D','F','G','H','J','K','M','N','P','Q','R','T','V','W','X','Y','Z','2','3','4','6','7','8','9'] #COMPLETO

    cod="" #key de 5 caracteres
    cod2=""
    cod3=""
    cod4=""
    cod5=""
    
    for i in range(5): #tamano de cada texto
        cod=cod+random.choice(caracteres)

        cod2=cod2+random.choice(caracteres)

        cod3=cod3+random.choice(caracteres)

        cod4=cod4+random.choice(caracteres)

        cod5=cod5+random.choice(caracteres)
        
        cod_full=cod+'-'+cod2+'-'+cod3+'-'+cod4+'-'+cod5 #guarda todo en una variable
        mostrar_cod.set(cod_full)

def borrar():
    mostrar_cod.set('')



root=Tk()
root.title('keyloger xbox')
root.geometry('300x200')
root.config(bg='green')
frame=Frame(root)
frame.pack()
frame.config(bg='green',width=490,height=390)
frame2=Frame(root)
frame2.pack()
frame2.config(bg='green',width=200,height=100)

mostrar_cod=StringVar()

Label(frame,text='codigo XBOX:').grid(row=0,column=0)
Entry(frame,textvariable=mostrar_cod).grid(row=0,column=1)
Button(frame2,text='GENERAR',command=keys).grid(row=0,columnspan=2)
Button(frame2,text='BORRAR',command=borrar).grid(row=1,columnspan=2)
Button(frame2,text='salir',command=salir).grid(row=2,columnspan=2)

     


root.mainloop()
'''
codigo_generado=''
 
def mensaje_mail():
    global codigo_generado
    caracteres=['C','D','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y','Z','2','3','4','6','7','9']
    for i in range(5):
        codigo_generado=codigo_generado+random.choice(caracteres)
    print(codigo_generado)
    
mensaje_mail()
    



