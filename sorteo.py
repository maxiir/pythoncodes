from random import*
from tkinter import*
from tkinter import messagebox

def sortear():
    	
	sorteo=str(randint(0,10))
	messagebox.showinfo('sorteo','salio el numero: "'+sorteo+'"')

root=Tk()
root.title("sorteo")

frame=Frame(root)
frame.pack()

Label(frame,text="Sorteo",fg="black",bg="#FF7043",font=("lucida",15)).grid(row=0,column=1,padx=5,pady=5)
Button(frame,text="Sortear!",width=10,height=0,command=sortear).grid(row=2,column=1,padx=5,pady=5)
root.mainloop()	

#nunca poner los parentesis adelante de la funcion a llamar para q no salte primero la funcion