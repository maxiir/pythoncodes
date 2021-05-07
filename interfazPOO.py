from sqlite3.dbapi2 import Cursor
from tkinter import*
from tkinter import messagebox
import sqlite3

global entrada1
global entrada2
global entrada3

class Interfaz():
    
    def __init__(self):
        global entrada1
        global entrada2
        global entrada3

        #campos:
        entrada1=StringVar()
        entrada2=StringVar()
        entrada3=StringVar()
        


        #-------------------------------------------------------------------
        
        root.title('nombre')
        

        self.frame=Frame(root,bg='black',width=700,heigh=500)
        self.frame.pack()
        self.frame2=Frame(root,bg='yellow',width=700,heigh=500)
        self.frame2.pack()
        self.frame3=Frame(root,bg='green',width=300,height=400)

        self.etiqueta=Label(self.frame,text='vacio1:').grid(row=0,column=0)
        self.etiqueta2=Label(self.frame,text='vacio2:').grid(row=1,column=0)
        self.etiqueta3=Label(self.frame,text='vacio3:').grid(row=2,column=0)

        self.entrada=Entry(self.frame,textvariable=entrada1).grid(row=0,column=1)
        self.entrada2=Entry(self.frame,textvariable=entrada2).grid(row=1,column=1)
        self.entrada3=Entry(self.frame,textvariable=entrada3).grid(row=2,column=1)

        self.boton=Button(self.frame2,text='aceptar',command=agregar).grid(row=0,column=0)
        self.boton2=Button(self.frame2,text='CERRAR',command=cerrar_TODO).grid(row=0,column=1)
        




class BBDD():
    def conexion(self):
        self.conexion=sqlite3.connect('bbdd')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("")
        self.conexion.commit()



def cerrar_TODO():
    root.destroy()
    #respuesta=messagebox.askquestion('bbdd','desea cerrar todo?')
    #if respuesta=='yes':
     #   root.destroy()


def crea_tab():
    
    
    conexion=sqlite3.connect('bbdd')
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE BBDD(COLUMNA1 VARCHAR(50),COLUMNA2 VARCHAR(50),COLUMNA3 VARCHAR(50))")
    except:
        messagebox.showinfo('BBDD','la base de datos ya existe!')
    conexion.commit()

    
def leer():
    funcionesBBDD=BBDD()
    funcionesBBDD.cursor.execute("SELECT* INTO")
    pass


def agregar():
    nuevo=Interfaz()    
    conexion=sqlite3.connect('bbdd')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO BBDD VALUES('"+entrada1.get()+"','"+entrada2.get()+"','"+entrada3.get()+"')")
    messagebox.showinfo('BBDD','agregado exitosamente!')
    conexion.commit()


def actualizar():
    funcionesBBDD=BBDD()
    funcionesBBDD.cursor.execute("UPDATE")
    pass
def eliminar():
    funcionesBBDD=BBDD()
    funcionesBBDD.cursor.execute("DELETE")
    pass




        


root=Tk() 
root.resizable(True,True)
root.geometry('240x150')

mi_ventana=Interfaz() #inicializacion del objeto





menuBar=Menu(root)
root.config(menu=menuBar)

BBDD=Menu(menuBar,tearoff=0)
BBDD.add_command(label='creacion de BBDD',command=crea_tab)
BBDD.add_command(label='Conexion clientes')
BBDD.add_command(label='Salir')
menuBar.add_cascade(menu=BBDD,label='BBDD')

opciones=Menu(menuBar,tearoff=0)
opciones.add_command(label='Leer')
opciones.add_command(label='Agregar')
opciones.add_command(label='Eliminar')
opciones.add_command(label='Actualizar')
opciones.add_command(label='Borrar todos los campos')
menuBar.add_cascade(menu=opciones,label='Opciones')
        
ayuda=Menu(menuBar,tearoff=0)
ayuda.add_command(label='Acerca de...')
ayuda.add_command(label='Licencia')
menuBar.add_cascade(menu=ayuda,label='Ayuda')






root.mainloop()


