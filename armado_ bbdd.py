import sqlite3
from tkinter import messagebox, ttk
from tkinter import*
from sqlite3 import*

def guardado_cliente():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO CLIENTES VALUES(NULL,'"+cliente_nombre.get()+"','"+cliente_direccion.get()+"','"+cliente_telefono.get()+"')")
    conexion.commit()
    cliente_nombre.set('')
    cliente_direccion.set('')
    cliente_telefono.set('')
    messagebox.showinfo('BBDD','Guardado con exito!')

def guardado_proveedor():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO PROVEEDORES VALUES(NULL,'"+proveedor_nombre.get()+"','"+proveedor_direccion.get()+"','"+proveedor_telefono.get()+"')")
    conexion.commit()
    proveedor_nombre.set('')
    proveedor_direccion.set('')
    proveedor_telefono.set('')
    messagebox.showinfo('BBDD','Guardado con exito!')

def guardado_producto():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'"+producto_desc.get()+"','"+producto_precio.get()+"')")
    cursor.execute("INSERT INTO CATEGORIAS VALUES(NULL,'"+categoria_desc.get()+"')")
    conexion.commit()
    categoria_desc.set('')
    producto_desc.set('')
    producto_precio.set('')
    messagebox.showinfo('BBDD','Guardado con exito!')


def tablas():
    conexion=sqlite3.connect('BBDD')
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE CLIENTES(ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE CHAR(20), DIRECCION VARCHAR(50),TELEFONO INTEGER(50))")
    cursor.execute("CREATE TABLE FACTURAS(ID_FACTURA INTEGER PRIMARY KEY AUTOINCREMENT,FECHA DATE, FOREIGN KEY(ID_FACTURA) REFERENCES CLIENTES(ID_CLIENTE))") #MARCO LA CLAVE FORANEA CUAL VA A SER Y HACE REFERENCIA A UNA TABLA Y UN CAMPO
    cursor.execute("CREATE TABLE VENTAS (ID_VENTA INTEGER PRIMARY KEY AUTOINCREMENT,FOREIGN KEY(ID_VENTA) REFERENCES FACTURAS(ID_FACTURA),FOREIGN KEY(ID_VENTA) REFERENCES PRODUCTOS(ID_PRODUCTO))")
    cursor.execute("CREATE TABLE PRODUCTOS(ID_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT, DESCRISPCION VARCHAR(50), PRECIO INTEGER(50),FOREIGN KEY (ID_PRODUCTO) REFERENCES CATEGORIAS(ID_CATEGORIA),FOREIGN KEY (ID_PRODUCTO) REFERENCES PROVEEDORES(ID_PROVEEDOR))")
    cursor.execute("CREATE TABLE CATEGORIAS(ID_CATEGORIA INTEGER PRIMARY KEY AUTOINCREMENT,DESCRIPCION VARCHAR(50))")
    cursor.execute("CREATE TABLE PROVEEDORES(ID_PROVEEDOR INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE CHAR(20),DIRECCION VARCHAR(50),TELEFONO INTEGER(50))")
    #cursor.execute("CREATE PROCEDURE PROCESO()") PROCEDIMIENTOS ALMACENADOS
    cursor.execute("CREATE VIEW NOMBRES_PROVEEDORES AS SELECT NOMBRE,TELEFONO FROM PROVEEDORES ") #CREACION DE UNA VISTA PARA VER DATOS ESPECIFICOS DIRECTAMENTE
    cursor.execute("CREATE TABLE TRIGGER_DE_INSERCION(HORARIO DATE)")
    conexion.commit()

def cerrar_software():
    respuesta=messagebox.askquestion('Cerrar gestor BBDD','Desea cerrar el gestor de BBDD?')
    if respuesta=='yes':
        root.destroy()

class frames():
    def __init__(self):
        self.mi_frame=Frame()
        self.mi_frame.pack()

        
root=Tk()
root.title("Gestor de BBDD")
root.geometry('500x300')

pestana_root=ttk.Notebook()
pestana_root.pack(fill='both',expand='yes')
pestana1=ttk.Frame(pestana_root)
pestana2=ttk.Frame(pestana_root)
pestana3=ttk.Frame(pestana_root)
pestana4=ttk.Frame(pestana_root)

pestana_root.add(pestana1,text='creacion de tablas') #agrego frame a la pestana root
pestana_root.add(pestana2,text='clientes')
pestana_root.add(pestana3,text='proveedores')
pestana_root.add(pestana4,text='productos')


frame_pes1=frames() #inicializo el objeto de pestana 1
frame_pes1.mi_frame=Frame(pestana1)
frame_pes1.mi_frame.pack()

frame_pes2=frames()
frame_pes2.mi_frame=Frame(pestana2)
frame_pes2.mi_frame.pack()

frame_pes3=frames()
frame_pes3.mi_frame=Frame(pestana3)
frame_pes3.mi_frame.pack()

frame_pes4=frames()
frame_pes4.mi_frame=Frame(pestana4)
frame_pes4.mi_frame.pack()



#pestana1 widgets
Button(frame_pes1.mi_frame,text='Crear tablas',command=tablas).grid(row=1,column=0)
Button(frame_pes1.mi_frame,text='Salir',command=cerrar_software).grid(row=2,column=0)

#VARIABLES ENTRY
cliente_nombre=StringVar()
cliente_direccion=StringVar()
cliente_telefono=StringVar()

proveedor_nombre=StringVar()
proveedor_direccion=StringVar()
proveedor_telefono=StringVar()

producto_desc=StringVar()
producto_precio=StringVar()

categoria_desc=StringVar()

#pestana2 CLIENTES
Label(frame_pes2.mi_frame,text='Nombre del cliente:').grid(row=0,column=0)
Entry(frame_pes2.mi_frame,textvariable=cliente_nombre).grid(row=0,column=1)
Label(frame_pes2.mi_frame,text='Direccion:').grid(row=1,column=0)
Entry(frame_pes2.mi_frame,textvariable=cliente_direccion).grid(row=1,column=1)
Label(frame_pes2.mi_frame,text='Telefono:').grid(row=2,column=0)
Entry(frame_pes2.mi_frame,textvariable=cliente_telefono).grid(row=2,column=1)
Button(frame_pes2.mi_frame,text='Guardar',command=guardado_cliente).grid(row=3,columnspan=5)


#pestana3 PROVEEDORES
Label(frame_pes3.mi_frame,text='Nombre del proveedor:').grid(row=0,column=0)
Entry(frame_pes3.mi_frame,textvariable=proveedor_nombre).grid(row=0,column=1)
Label(frame_pes3.mi_frame,text='Direccion:').grid(row=1,column=0)
Entry(frame_pes3.mi_frame,textvariable=proveedor_direccion).grid(row=1,column=1)
Label(frame_pes3.mi_frame,text='Telefono:').grid(row=2,column=0)
Entry(frame_pes3.mi_frame,textvariable=proveedor_telefono).grid(row=2,column=1)
Button(frame_pes3.mi_frame,text='Guardar',command=guardado_proveedor).grid(row=3,columnspan=5)

#pestana4 PRODUCTOS
Label(frame_pes4.mi_frame,text='Descripcion del producto:').grid(row=0,column=0)
Entry(frame_pes4.mi_frame,textvariable=producto_desc).grid(row=0,column=1)
Label(frame_pes4.mi_frame,text='precio:').grid(row=1,column=0)
Entry(frame_pes4.mi_frame,textvariable=producto_precio).grid(row=1,column=1)

Label(frame_pes4.mi_frame,text='Categoria:').grid(row=2,column=0)
Entry(frame_pes4.mi_frame,textvariable=categoria_desc).grid(row=2,column=1)
Button(frame_pes4.mi_frame,text='Guardar',command=guardado_producto).grid(row=3,columnspan=4)





root.mainloop()

