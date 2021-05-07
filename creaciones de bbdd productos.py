from tkinter import*
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('gestor de base de datos')
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()


def close_program():
    root.destroy()

def abrir_conexion():
    conexion=sqlite3.connect('bbdd_productos')
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE PRODUCTOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,ARTICULO VARCHAR(50),CATEGORIA VARCHAR(50),ORIGEN VARCHAR(50),PRECIO VARCHAR(50),STOCK INTEGER(50))")
        conexion.commit()
        messagebox.showinfo('bbdd','base de datos creada exitosamente!')
    except:
        messagebox.showinfo('bbdd','la base datos ya existe!')

def almacenar():
    conexion=sqlite3.connect('bbdd_productos')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'"+articulo.get()+"','"+categoria.get()+"','"+origen.get()+"','"+precio.get()+"','"+stock.get()+"')")
    messagebox.showinfo('bbdd','datos agregados exitosamente!')
    conexion.commit()
    articulo.set("")
    categoria.set("")
    origen.set("")
    precio.set("")
    stock.set("")

articulo=StringVar()
categoria=StringVar()
origen=StringVar()
precio=StringVar()
stock=StringVar()


Label(frame1,text='articulo:').grid(row=0,column=0)
Entry(frame1,textvariable=articulo).grid(row=0,column=1)
Label(frame1,text='categoria:').grid(row=1,column=0)
Entry(frame1,textvariable=categoria).grid(row=1,column=1)
Label(frame1,text='origen:').grid(row=2,column=0)
Entry(frame1,textvariable=origen).grid(row=2,column=1)
Label(frame1,text='precio:').grid(row=3,column=0)
Entry(frame1,textvariable=precio).grid(row=3,column=1)
Label(frame1,text='stock:').grid(row=4,column=0)
Entry(frame1,textvariable=stock).grid(row=4,column=1)


Button(frame2,text='aceptar',command=almacenar).grid(row=0,column=1)
Button(frame2,text='salir',command=close_program).grid(row=0,column=2)
Button(frame2,text='abrir conexion',command=abrir_conexion).grid(row=1,columnspan=3)





root.mainloop()








    
        


        





























