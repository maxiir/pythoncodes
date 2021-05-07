from tkinter import*
from tkinter import ttk

root=Tk()

box=ttk.Combobox(root)
box.place(x=50,y=100) #tamano
box['values']='auto','autobus','caminar','bici','tren' #agrega los valores q quieras al combobox
box.current(1) #por numero de indice ya deja visible una opcion
root.mainloop()