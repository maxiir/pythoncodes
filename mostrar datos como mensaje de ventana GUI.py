from tkinter import*
from tkinter import messagebox

def Saludar():
	"""Extrae lo que se escribe en el campo de texto
	   y lo muestra con un cuadro de diálogo"""
	_nombre=nombre.get()
	messagebox.showinfo("mensaje", "Hola %s"%_nombre)

root=Tk()
nombre=StringVar()#almacena los datos que se escriben en caja_texto
etiqueta = Label(root, text="Cuál es tu nombre? ").grid(row=0, column=0, padx=10, pady=50)
caja_texto = Entry(root, bd =5, textvariable=nombre).grid(row=0, column=1)
boton=Button(root, text="PULSAR", command=Saludar).grid(row=0, column=2, padx=10)




root.mainloop()