from tkinter import*
from tkinter import messagebox
import sqlite3

suma_productos=0

#--------------------------------------funciones_MENU---------------------------------------
def conexionBBDD():
    conexion=sqlite3.connect("productos")
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE PRODUCTOS(CODIGO INTEGER (4)PRIMARY KEY,PRODUCTO VARCHAR(50),STOCK INTEGER(50),VALOR INTEGER(50))")
        messagebox.showinfo('atencion','base de datos "productos" creada con exito!')
    except:
        messagebox.showwarning('atencion','Base de datos "productos" ya existe')
    
    conexion.commit()

def salir():
    respuesta=messagebox.askquestion('salir de la App','El programa se cerrara, desea cerrarlo?')
    if respuesta=='yes':
        root.destroy()

def BBDD_CLIENTES():
    conexion=sqlite3.connect("clientes")
    cursor=conexion.cursor()
    
    try:
        cursor.execute("CREATE TABLE CLIENTES(ID INTEGER PRIMARY KEY AUTOINCREMENT,COBRO INTEGER(500))")
        messagebox.showinfo("BBDD","BBDD clientes creada con exito!")
    except:
        messagebox.showinfo('BBDD','La BBDD "clientes",ya existe!')
    conexion.commit()


def acercade():
    messagebox.showinfo('Informacion del programa','Version: 1.0.0\nDesarollador:Maximiliano Rucci\nContacto:maxiirucci@gmail.com')

def licencia():
    messagebox.showinfo('Licencia','Licencia: Premium')

def borrar_campos():
    global suma_productos

    CODIGO.set('')
    PRODUCTO.set('')
    STOCK.set('')
    VALOR.set('')
    MONTO.set('')
    TOTAL.set('')
    CAMBIO.set('')
    suma_productos=0

def limpia_valor(): #limpia solo el campo valor para el carrito ,evitando inconvenientes de suma
    VALOR.set('')

#------------------------------------------funciones_BBDD---------------------------------

def leer():
    conexion=sqlite3.connect('productos')
    cursor=conexion.cursor()

    cursor.execute("SELECT* FROM PRODUCTOS WHERE CODIGO="+CODIGO.get())

    elproducto=cursor.fetchall() #FETCHALL DEVUELVE UNA LISTA EN SU LUGAR

    for mostrar in elproducto:
        CODIGO.set(mostrar[0])
        PRODUCTO.set(mostrar[1])
        STOCK.set(mostrar[2])
        VALOR.set(mostrar[3])

def eliminar():
    conexion=sqlite3.connect('productos')
    cursor=conexion.cursor()

    cursor.execute("DELETE FROM PRODUCTOS WHERE CODIGO="+CODIGO.get())
    respuesta=messagebox.askquestion('BBDD','Se ELIMINARA el registro indicado, esta seguro de borrarlo?')
    if respuesta=='yes':
        messagebox.showinfo('BBDD','Registro ELIMINADO exitosamente!')
    
    conexion.commit()

def agregar():
    conexion=sqlite3.connect('productos')
    cursor=conexion.cursor()
    
    cursor.execute("INSERT INTO PRODUCTOS VALUES('"+CODIGO.get()+"','"+PRODUCTO.get()+"','"+STOCK.get()+"','"+VALOR.get()+"')")
    #utilizar la doble comillas en las query 
    conexion.commit()
    messagebox.showinfo('BBDD','Productos agregados con exito!')   

def actualizar():
    conexion=sqlite3.connect('productos')
    cursor=conexion.cursor()

    cursor.execute("UPDATE PRODUCTOS SET PRODUCTO='"+PRODUCTO.get()+"',STOCK='"+STOCK.get()+"',VALOR='"+VALOR.get()+"'WHERE CODIGO="+CODIGO.get())
    conexion.commit()
    messagebox.showinfo('BBDD','Datos ACTUALIZADOS con exito!')


def agregar_cobros():
    
    
    conexion=sqlite3.connect("clientes")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO CLIENTES VALUES(NULL,'"+TOTAL.get()+"')")
    messagebox.showinfo('BBDD','cobro agregado a la BBDD')
    
    conexion.commit()
    

#--------------------------------------------funciones_BOTONES----------------------------------

def carrito():
    global suma_productos

    suma_productos=suma_productos+VALOR.get()
    VALOR.set(suma_productos)
    limpia_valor()

def comprar():
    global suma_productos

    dinMONTO=MONTO.get()
    precioT=TOTAL.get()
    vuelto=dinMONTO-precioT
    CAMBIO.set(vuelto)
    suma_productos=0
    agregar_cobros()

def fin_compra():

    try:
        TOTAL.set(VALOR.get()) #muestra en la entrada de texto el total con el valor obtenido del campo valor
    except:TOTAL.set(suma_productos)
#*******ver para agregar la solucion de sumar lo del carrito y el campo valor****************


def elstock():
    conexion=sqlite3.connect('productos')
    cursor=conexion.cursor()
    cursor.execute("UPDATE PRODUCTOS SET STOCK='"+STOCK.GET()+"'WHERECODIGO="+CODIGO.get())
    pass


#-------------------------------------interfaz--------------------------------------------
root=Tk()
root.title("Caja")
root.geometry('390x500')
root.resizable(True,True)

frame=Frame(root,bg="#5C6BC0")
frame.pack()
frame2=Frame(root,bg='#5C6BC0')
frame2.pack()
frame3=Frame(root,bg='#5C6BC0')
frame3.pack()

#barra_menu-------------------------------
menubar=Menu(root)
root.config(menu=menubar,bg='#5C6BC0')

BBDD=Menu(menubar,tearoff=0)
BBDD.add_command(label='Conexion productos',command=conexionBBDD)
BBDD.add_command(label='Conexion clientes',command=BBDD_CLIENTES)
BBDD.add_command(label='Salir',command=salir)
menubar.add_cascade(menu=BBDD,label='BBDD')

opciones=Menu(menubar,tearoff=0)
opciones.add_command(label='Leer',command=leer)
opciones.add_command(label='Agregar',command=agregar)
opciones.add_command(label='Eliminar',command=eliminar)
opciones.add_command(label='Actualizar',command=actualizar)
opciones.add_command(label='Borrar todos los campos',command=borrar_campos)
menubar.add_cascade(menu=opciones,label='Opciones')

ayuda=Menu(menubar,tearoff=0)
ayuda.add_command(label='Acerca de...',command=acercade)
ayuda.add_command(label='Licencia',command=licencia)
menubar.add_cascade(menu=ayuda,label='Ayuda')

#campos----------------------------------
CODIGO=StringVar()
PRODUCTO=StringVar()
STOCK=StringVar()

VALOR=IntVar()#modi

MONTO=IntVar()#modi

TOTAL=IntVar()#modi

CAMBIO=IntVar()#modi


Label(frame,text='CODIGO:',width=12,height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=0,column=0,padx=5,pady=5)
Entry(frame,width=12,textvariable=CODIGO).grid(row=0,column=1)

Label(frame,text='Producto:',width=12,height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=2,column=0)
Entry(frame,width=12,textvariable=PRODUCTO).grid(row=2,column=1)

Label(frame,text='Stock:',width=12,height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=3,column=0)
Entry(frame,width=12,textvariable=STOCK).grid(row=3,column=1)

Label(frame,text='Valor:',width=12,height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=4,column=0)
Entry(frame,width=12,textvariable=VALOR).grid(row=4,column=1)

Label(frame2,text='Monto:',height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=1,column=0)
Entry(frame2,width=12,textvariable=MONTO).grid(row=1,column=1)
Label(frame2,text='Cambio:',height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=2,column=0)
Entry(frame2,width=12,textvariable=CAMBIO).grid(row=2,column=1,columnspan=2)
Label(frame2,text='TOTAL:',height=3,font=('calibri 15'),bg='#5C6BC0').grid(row=3,column=0)
Entry(frame2,width=12,textvariable=TOTAL).grid(row=3,column=1,columnspan=2)

#botones------------------------------------
Button(frame,text='escanear',width=12,command=leer).grid(row=1,column=1)
Button(frame,text='carrito',width=12,command=carrito).grid(row=5,column=0)
Button(frame,text='=',width=12,command=fin_compra).grid(row=5,column=1)
Button(frame2,text='cobrar',width=12,command=comprar).grid(row=1,column=2)

root.mainloop()



