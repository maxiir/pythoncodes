from tkinter import*
from tkinter import messagebox


def calculo():
	
	area=(base.get()*altura.get())/2
	messagebox.showinfo("calculo de area","CALCULO TERMINADO!")
	area=areaRES.set(area) #set devuelve un valor para entry


root=Tk()
root.config(bg="#FF7043")
root.title("Calculadora de area de un triangulo")
root.geometry("340x180+0+0")
frame=Frame(root, bg="#FF7043")
frame.pack()

Label(frame,text="Calcula tu triangulo!",fg="black",bg="#FF7043",font=("lucida",15)).grid(row=0,column=1,padx=5,pady=5)


base=IntVar()#se guarda el valor del Entry 
textoBASE=Label(frame,text="Base:",width=10,height=0,bg="#FF7043",font=("lucida",15)).grid(row=2,column=0)
Entry(frame,textvariable=base,justify=CENTER,fg="black",bg="#F0B27A",font=("lucida",15)).grid(row=2,column=1) #no se asigna entry a una variable para obtener el valor da error

altura=IntVar()
textoALTURA=Label(frame,text="Altura:",width=5,height=0,bg="#FF7043",font=("lucida",15)).grid(row=3,column=0)
Entry(frame,textvariable=altura,justify=CENTER,bg="#F0B27A",font=("lucida",15)).grid(row=3,column=1,padx=5,pady=5)

areaRES=IntVar()
textoREST=Label(frame,text="Area=>",width=10,height=0,bg="#FF7043",font=("lucida",15)).grid(row=4,column=0)
result=Entry(frame,state="disable",textvariable=areaRES ,justify=CENTER,bg="#F0B27A",font=("lucida",15)).grid(row=4,column=1)


Boton_calculo=Button(frame,text="Calcular",width=10,height=0,command=calculo).grid(row=5,column=1,padx=5,pady=5)
#command llama a la funcion q necesitas para el boton
	





root.mainloop()