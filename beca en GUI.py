from tkinter import*
from tkinter import messagebox
	
#beca=False
#ButtonACEPTAR=False
root=Tk()
root.title("Becas trelew by maxir")



	
def alerta():
	
	if tra2.get()==1 and dis3.get()==1 and opt2.get()==1:
		messagebox.showinfo("becas trelew by maxir","PUEDES OBTENER LA BECA")
	#else:
		#messagebox.showinfo("becas trelew by maxir","NO PUEDES OBTENER UNA BECA")



tra1=IntVar()
tra2=IntVar()

dis1=IntVar()
dis2=IntVar()
dis3=IntVar()

opt1=IntVar()
opt2=IntVar()



Label(root,text="***Programa de becas***\n\nSelecciones las opciones correspondientes:", width=80).pack() #width le da el tamaño a la ventana


Label(root,text='Trabaja en algun lugar?').pack()
Checkbutton(root,text='Si',onvalue=1,offvalue=0,command=tra1).pack()
Checkbutton(root,text='No',onvalue=1,offvalue=0,command=tra2).pack()
Label(root,text="Cual es la distancia a su institucion?").pack()
Checkbutton(root, text='5km',onvalue=1,offvalue=0,command=dis1).pack()
Checkbutton(root, text='2km',onvalue=1,offvalue=0,command=dis2).pack()
Checkbutton(root, text='Mas de 5km',onvalue=1,offvalue=0,command=dis3).pack()
Label(root,text='Recibe alguna otra beca?').pack()
Checkbutton(root, text='si', onvalue=1,offvalue=0,command=opt1).pack()
Checkbutton(root, text='no',onvalue=1,offvalue=0,command=opt2).pack()
Label(root,text='Desea dejar un comentario o aporte?').pack()
Entry(root).pack()



ButtonACEPTAR=Button(root,text="aceptar",command=alerta,width=5).pack()


root.mainloop()


#(funcion donde este el comentario .__doc__) ////te muestra el comentario q pusiste en esa funcion 