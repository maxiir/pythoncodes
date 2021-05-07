from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from sqlite3 import*

def informacion():
    messagebox.showinfo("informacion","Version: 1.0 \nDesarrollador: Maximiliano Rucci\nContacto: maxiirucci@gmail.com\nano:2021") 



def cerrar_gestor():
    respuesta= messagebox.askquestion('cerrar gestor','El gestor se cerrar, desea hacerlo?')
    if respuesta=='yes':
        root.destroy()


def nuevas_tablas():
    conexion=sqlite3.connect("mis_tablas")
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE '"+nombre_tabla.get()+"'(ID INTEGER PRIMARY KEY AUTOINCREMENT,'"+nombre_campo.get()+"' '"+dato.get()+"' '"+capacidad.get()+"')")
    conexion.commit()
    nombre_tabla.set('')
    agregar_campos.set('')
    nombre_campo.set('')
    dato.set('')
    capacidad.set('')
    messagebox.showinfo("BBDD","Tabla '"+nombre_tabla.get()+"'creada exitosamente!")

def eliminar_tabla():
    conexion=sqlite3.connect("mis_tablas")
    cursor=conexion.cursor()
    respuesta=messagebox.askquestion('eliminar tabla','desea eliminar esta tabla?')
    if respuesta=='yes':
        cursor.execute("DROP TABLE '"+nombre_tabla.get()+"' ")
    conexion.commit()
    messagebox.showinfo("BBDD","La tabla '"+nombre_tabla.get()+"' fue eliminada con exito!")
    

def agregar_campo():
    conexion=sqlite3.connect("mis_tablas")
    cursor=conexion.cursor()
    cursor.execute("ALTER TABLE '"+agregar_campos.get()+"' ADD '"+nombre_campo.get()+"' '"+dato.get()+"' '"+capacidad.get()+"' ")
    conexion.commit()
    nombre_tabla.set('')
    agregar_campos.set('')
    nombre_campo.set('')
    dato.set('')
    capacidad.set('')

def agregar_registro(): #CHECKEAR
    conexion=sqlite3.connect("mis_tablas")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO '"+buscar_tabla.get()+"' VALUES(NULL,'"+reg.get()+"' )")
    conexion.commit()
    reg.set('')
    


class frames():
    def __init__(self):
        self.frame=Frame()
        self.frame.pack()


root=Tk()
root.title('gestor de tablas SQL')
#creacion de pestana root
pestana_root=ttk.Notebook()
pestana_root.pack(fill='both',expand='yes')
#creacion de las ventanas
pestana1=ttk.Frame(pestana_root)
pestana2=ttk.Frame(pestana_root)
pestana3=ttk.Frame(pestana_root)
pestana4=ttk.Frame(pestana_root)
#agregado de ventanas
pestana_root.add(pestana1,text='Agregar registros')
pestana_root.add(pestana2,text='creacion de tablas')
pestana_root.add(pestana3,text='eliminaciones')
pestana_root.add(pestana4,text='ver datos de tabla')

pes1=frames()
pes1.frame=Frame(pestana1)
pes1.frame.pack()

buscar_tabla=StringVar() #para agregar registros
reg=StringVar()
el_campo=StringVar()



Label(pes1.frame,text='tabla:').grid(row=0,column=0)
Entry(pes1.frame,textvariable=buscar_tabla).grid(row=0,column=1)
Label(pes1.frame,text='campo:').grid(row=1,column=0)
Entry(pes1.frame,textvariable=el_campo).grid(row=1,column=1)
Label(pes1.frame,text="registro:").grid(row=2,column=0) #AGREGA DE A UN REGISTRO
Entry(pes1.frame,textvariable=reg).grid(row=2,column=1)

Button(pes1.frame,text='AGREGAR',command=agregar_registro).grid(row=3,columnspan=4)
Button(pes1.frame,text='SALIR',command=cerrar_gestor).grid(row=4,columnspan=5)


#creacion de tablas----------------------------
nombre_tabla=StringVar()
agregar_campos=StringVar()
nombre_campo=StringVar()
dato=StringVar()
capacidad=StringVar()



pes2=frames()
pes2.frame=Frame(pestana2)
pes2.frame.pack()
Label(pes2.frame,text='crear tabla:').grid(row=0,column=0)
Entry(pes2.frame,textvariable=nombre_tabla).grid(row=0,column=1)
Label(pes2.frame,text='guardar en tabla:').grid(row=1,column=0)
Entry(pes2.frame,textvariable=agregar_campos).grid(row=1,column=1)
Label(pes2.frame,text='nombre de campo:').grid(row=2,column=0)
Entry(pes2.frame,textvariable=nombre_campo).grid(row=2,column=1)
Label(pes2.frame,text='tipo de dato:').grid(row=3,column=0)
Entry(pes2.frame,textvariable=dato).grid(row=3,column=1)
Label(pes2.frame,text='capacidad ( ):').grid(row=4,column=0)
Entry(pes2.frame,textvariable=capacidad).grid(row=4,column=1)

Button(pes2.frame,text='CREAR',command=nuevas_tablas).grid(row=5,column=3)
Button(pes2.frame,text='AGREGAR',command=agregar_campo).grid(row=5,columnspan=4)

pes3=frames()
pes3.frame=Frame(pestana3)
pes3.frame.pack()
Label(pes3.frame,text='eliminar tabla:').grid(row=0,column=0)
Entry(pes3.frame,textvariable=nombre_tabla).grid(row=0,column=1)
Button(pes3.frame,text='ELIMINAR',command=eliminar_tabla).grid(row=1,columnspan=3)

pes4=frames()
pes4.frame=Frame(pestana4)
pes4.frame.pack()
Label(pes4.frame,text='tabla:').grid(row=0,column=0)
Entry(pes4.frame,textvariable='').grid(row=0,column=1)
Label(pes4.frame,text='registros:').grid(row=1,column=0)
Entry(pes4.frame,textvariable='').grid(row=1,column=1)



menu_crud=Menu(root)
root.config(menu=menu_crud)
bbdd=Menu(menu_crud,tearoff=0)
bbdd.add_command(label='abrir nueva conexion')
bbdd.add_command(label='cerrar gestor',command=cerrar_gestor)
menu_crud.add_cascade(menu=bbdd,label='conexion')

acerca=Menu(menu_crud,tearoff=0)
acerca.add_command(label='informacion',command=informacion)
menu_crud.add_cascade(menu=acerca,label='acerca de...')



root.mainloop()

#libreria= import random
#generar numeros aleatoreo, random.redint(a,b) a= de donde b=hasta donde
#a=cierta cantidad de repeticiones range(a)