from tkinter import *
from tkinter import messagebox

operador=""
operador2=""

def clear():
	global operador
	operador=("")
	input_text.set("0")
		
def clear2():
	global operador2
	operador2=("")
	input_text2.set("0")
			
def btnClik(num):
	global operador
	operador=operador+str(num)
	input_text.set(operador) #VISUALIZAR LA OPERACION EN LA PANTALLA
	
def btnClik2(num):
	global operador2
	operador2=operador2+str(num)
	input_text2.set(operador2) #VISUALIZAR LA OPERACION EN LA PANTALLA
		
def final():
	global operador
	global operador2
	
	try:
		opera=str(eval(operador))
		opera2=str(eval(operador2))#REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
	except:
		clear()
		clear2()
		opera=("ERROR")
		opera2=("ERROR")
	input_text.set(opera)
	input_text2.set(opera2)
	
	if opera>opera2:
		messagebox.showinfo("Fin del juego!","EL GANADOR ES EL JUGADOR 1!")
	else:
		messagebox.showinfo("Fin del juego!","EL GANADOR ES EL JUGADOR 2!")
#---------------------------------------------------------------G.U.I----------------------------------------------------
root=Tk()
frame=Frame(root,bg="#17A589") #color de frame (medio)
frame.pack()
root.title("Puntuacion total del AS")
root.config(bg="#17A589",curso="heart") #color de la raiz (marco)
root.geometry("800x410+0+0")#tamaño de la ventana TOTAL
foto=PhotoImage(file="carta.gif")
Label(frame,bg="silver",image=foto, bd=0).grid(row=4,column=1) 
root.resizable(False,False) #permitir ajustar la ventana
titulo=Label(frame, text="Contador de puntajes!")
titulo.grid(row=0,column=1)    
titulo.config(fg="#F4D03F",bg="#17A589",font=("Lucida",20))
EntryJU1=Entry(frame)
EntryJU1.grid(row=1,column=0, padx=5,pady=5) 
EntryJU1.config(justify="center" ,bg="#D1F2EB", fg="#34495E", font=("Lucida",20))
label1=Label(frame, text="\nJUGADOR 1:")
label1.grid(row=0, column=0) 
label1.config(fg="white",bg="#17A589",font=("Verdana",15))
EntryJU2=Entry(frame)
EntryJU2.grid(row=1,column=3)
EntryJU2.config(justify="center", bg="#D1F2EB",fg="#34495E",font=("Lucida",20))
label2=Label(frame, text="\nJUGADOR 2:")
label2.grid(row=0,column=3) 
label2.config(fg="white",bg="#17A589",font=("verdana",15))
#--------------------------------------------------jugador1
input_text=StringVar()
puntajeJU1=Entry(frame,textvariable=input_text)
puntajeJU1.grid(row=2 ,column=0)
#--------------------------------------------------jugador2
input_text2=StringVar()
puntajeJU2=Entry(frame,textvariable=input_text2)
puntajeJU2.grid(row=2,column=3)
#-----------------------------------------------------BOTONES--------------------------------------------------------
boton1002=Button(frame, fg="black",text="100",width=10,height=2,command=lambda:btnClik2(100)).grid(row=4,column=3)
boton100=Button(frame, fg="black",text="100",width=10,height=2,command=lambda:btnClik(100)).grid(row=4,column=0,padx=5,pady=5)  #0=iz 1=med 3=der
boton102=Button(frame,text="10",width=10,height=2,command=lambda:btnClik2(10)).grid(row=5,column=3)
boton10=Button(frame,text="10",width=10,height=2,command=lambda:btnClik(10)).grid(row=5,column=0)
botonDEL2=Button(frame,fg="black",text="DEL",width=10,height=2,command=clear2).grid(row=7,column=3,padx=5,pady=5)
botonDEL=Button(frame,fg="black",text="DEL",width=10,height=2,command=clear).grid(row=7,column=0,padx=5,pady=5)
botonSUMA2=Button(frame,fg="black",text="+",width=10,height=2,command=lambda:btnClik("+")).grid(row=6,column=0)
botonSUMA=Button(frame,fg="black",text="+",width=10,height=2,command=lambda:btnClik2("+")).grid(row=6,column=3,padx=5,pady=5)
botonTOTAL=Button(frame,text="TOTAL",width=10,height=2,command=final).grid(row=6,column=1)

root.mainloop()						