from tkinter import*

root=Tk()
root.title("indice de masa corporal (I.M.C)")
root.config(bg="#2ECC71")
root.geometry("280x400+0+0")
root.resizable(False,False)
frame=Frame(root,bg="#2ECC71",width=500,height=500)
frame.pack()
imagen=PhotoImage(file="imc3.gif")
Label(frame,image=imagen,bg="#2ECC71").grid(row=1,column=1)


def cal():
	
	mult=altura.get()*altura.get()
	imc=peso.get()/mult
	print(imc)
	
	
	if peso.get()<=0 or peso.get()>=500:
		imc="peso incorrecto"
		imc=Imc.set(imc)
		
	elif altura.get()<=0 or altura.get()>=3.00:
		imc="altura incorrecta"
		imc=Imc.set(imc)
	
	elif imc<18.50:
		imc="usted esta por debajo del peso normal"
		imc=Imc.set(imc)
	
	elif imc>18.50 and imc<25.00:
		imc="usted tiene un peso normal"
		imc=Imc.set(imc)
	
	elif imc>25.00:
		imc="usted esta con sobre peso"
		imc=Imc.set(imc)
		
	
def delete():
	altura.set(0)
	peso.set(0)
	Imc.set(0)
	
	


Label(frame,text="CALCULE SU I.M.C",bg="#2ECC71",font=("lucida",15)).grid(row=0,column=1,padx=5,pady=5)

peso=IntVar()
Label(frame,text="Peso:",bg="#2ECC71",font=("lucida",15)).grid(row=2,column=0,padx=5,pady=5)
Entry(frame,textvariable=peso).grid(row=2,column=1)

altura=IntVar()
Label(frame,text="Altura:",bg="#2ECC71",font=("lucida",15)).grid(row=3,column=0,padx=5,pady=5)
Entry(frame,textvariable=altura).grid(row=3,column=1)

Imc=StringVar()
Label(frame,text="I.M.C",bg="#2ECC71",font=("lucida",15)).grid(row=4,column=0,padx=5,pady=5)
Entry(frame,textvariable=Imc,state="disable",fg="black").grid(row=4,column=1)

Button(frame,text="calcular",width=10,height=2,bg="#2ECC71",command=cal).grid(row=5,column=1,padx=10,pady=10)
Button(frame,text="DEL",width=10,height=2,bg="#2ECC71",command=delete).grid(row=6,column=1,padx=10,pady=10)







root.mainloop()