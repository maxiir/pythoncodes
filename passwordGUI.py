from tkinter import*
from tkinter import messagebox
import sqlite3

cont=0

def aceptar():
    global cont
        
    if password.get()!='maxi1234':                                          
        messagebox.showwarning('error','clave incorrecta')
        password.set('')      
        password.set('')
        cont=cont+1
    if password.get()=='maxi1234':
        messagebox.showinfo('validacion','validacion con exito!')

    while cont==3:
        respuesta=messagebox.askquestion('intentos agotados','se a bloqueado desea volver a intentarlo?')
        if respuesta=='yes':
            cont=0
        else:
            exit()

root=Tk()

password=StringVar()

Label(root,text='Password:').grid(row=0,column=0,columnspan=2)
Entry(root,textvariable=password,show="*").grid(row=1,column=0,columnspan=2) #show="*" esconde los caracteres
Button(root,text='Aceptar',command=aceptar).grid(row=2,column=0,columnspan=2)


root.mainloop()