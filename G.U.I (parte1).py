from tkinter import*

prim_ventana=Tk()
prim_ventana.title("  maxi rucci")   #titulo de la ventana
prim_ventana.resizable(True,True) #dimensionarla o no

miframe=Frame(prim_ventana,width=500,height=500)
miframe.pack()
Label(miframe,text="mi primera ventana gorditaa",fg="green").place(x=150,y=200)  #ubicacion del texto en la ventana. x e y 







prim_ventana.mainloop()