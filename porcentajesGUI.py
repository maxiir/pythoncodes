from os import stat
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#promedio:
cont=0
lista=[]

#moda:
lista_moda=[]
la_moda=[]


class frames():
    def __init__(self):
        self.frame=Frame()
        self.frame.pack()


def limpiar():
    valor.set('')
    porcentaje.set('')
    descuento.set('')

    valores.set('')
    media.set('')

    numeros.set('')
    moda.set('')

def cerrar_prog():
    root.destroy()

def calcular(): #porcentaje
    total=valor.get()*porcentaje.get()
    total=total/100
    descuento.set(total)
    
    conexion=sqlite3.connect('porcentajes')
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO PORCENTAJE VALUES(NULL,'"+descuento.get()+"')")
    conexion.commit()
    messagebox.showinfo('Calculo realizado',descuento.get())

def nueva_tab():
    conexion=sqlite3.connect('porcentajes')
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE PORCENTAJE(ID INTEGER PRIMARY KEY AUTOINCREMENT, PORCENTAJES INTEGER(50))")
        messagebox.showinfo('BBDD','Conexion establecida con exito!')
    except:
        messagebox.showinfo('BBDD','Ya existe la conexion con la base de datos!')
    conexion.commit()

def cal_promedio():
    global cont
    global lista

    promedio=sum(lista) #se suman todos los valores agregados
    for i in lista: #cuenta todos los valores q tiene la lista
        if i>0:
            cont=cont+1
    promedio=promedio/cont
    media.set(promedio) #guardar en el entry el resultado

    #limpiar contador y lista de valores:
    cont=0
    lista=[]

def cal_moda():
    global lista_moda
    global la_moda
    repeticiones=0

    for i in lista_moda:
        apariciones=lista_moda.count(i)
        if apariciones>repeticiones:
            repeticiones=apariciones
    for i in lista_moda:
        apariciones=lista_moda.count(i)
        if apariciones==repeticiones and i not in la_moda:
            la_moda.append(i)
        
    moda.set(la_moda)

    lista_moda=[]
    la_moda=[]

def add_moda():
    lista_moda.append(numeros.get())
    numeros.set('')


def agregarVAL():
    lista.append(valores.get()) #se guardan todos los valores en una lista
    valores.set('')

    

def suma_column():
    descuento.set('')
    conexion=sqlite3.connect('porcentajes')
    cursor=conexion.cursor()
    cursor.execute("SELECT SUM (PORCENTAJES) FROM PORCENTAJE") #suma toda una columna 
    conexion.commit()
    
    porcentajes=cursor.fetchall()
    for mostrar in porcentajes:
        descuento.set(mostrar[0])
      

root=Tk()
root.title('Calculos')
root.geometry('500x200')

#pestanas ==notebook-----------------------------------
pestana_root=ttk.Notebook()
pestana_root.pack(fill='both',expand='yes')

pestana1=ttk.Frame(pestana_root) #crea pestanas,frames individuales para cada pestana
pestana2=ttk.Frame(pestana_root)
pestana3=ttk.Frame(pestana_root)

pestana_root.add(pestana1,text='Porcentaje') #anade los frames creados anteriormente
pestana_root.add(pestana2,text='Promedio')
pestana_root.add(pestana3,text='Moda')

#frames de porcentaje:
pes1=frames()
pes1.frame=Frame(pestana1)
pes1.frame.pack()
pes1.frame2=Frame(pestana1)
pes1.frame2.pack()

#frames de promedio:
pes2=frames()
pes2.frame=Frame(pestana2)
pes2.frame.pack()
pes2.frame2=Frame(pestana2)
pes2.frame2.pack()

#frames de moda:

pes3=frames()
pes3.frame=Frame(pestana3)
pes3.frame.pack()
pes3.frame2=Frame(pestana3)
pes3.frame2.pack()

menubarra=Menu(root)
root.config(menu=menubarra)
conexion=Menu(menubarra,tearoff=0)

conexion.add_command(label='crear tabla',command=nueva_tab)
menubarra.add_cascade(menu=conexion,label='conexion')

#--------------------------porcentaje------------------------------------
#campos:
valor=IntVar()
porcentaje=IntVar()
descuento=StringVar()

Label(pes1.frame,text='valor:').grid(row=1,column=0)
Entry(pes1.frame,textvariable=valor).grid(row=1,column=1)

Label(pes1.frame,text='porcentaje:').grid(row=2,column=0)
Entry(pes1.frame,textvariable=porcentaje).grid(row=2,column=1)

Label(pes1.frame,text='descuento:').grid(row=3,column=0)
Entry(pes1.frame,textvariable=descuento).grid(row=3,column=1)

Button(pes1.frame2,text='calcular',command=calcular).grid(row=1,column=0)
Button(pes1.frame2,text='limpiar',command=limpiar).grid(row=1,column=1)
Button(pes1.frame2,text='sumar todo',command=suma_column).grid(row=1,column=2)
Button(pes1.frame2,text='CERRAR',command=cerrar_prog).grid(row=2,columnspan=3)

#--------promedio---------------------------------------------
#campos:
valores=IntVar()
media=StringVar()

Label(pes2.frame,text='valores:').grid(row=0,column=0)
Entry(pes2.frame,textvariable=valores).grid(row=0,column=1)
Button(pes2.frame,text='agregar',command=agregarVAL).grid(row=0,column=3)

Label(pes2.frame,text='Promedio:').grid(row=1,column=0)
Entry(pes2.frame,textvariable=media).grid(row=1,column=1)

Button(pes2.frame2,text='calcular',command=cal_promedio).grid(row=0,column=0)
Button(pes2.frame2,text='limpiar',command=limpiar).grid(row=0,column=1)
Button(pes2.frame2,text='CERRAR',command=cerrar_prog).grid(row=1,columnspan=3)


#------moda------------------------------------------------

numeros=IntVar()
moda=StringVar()

Label(pes3.frame,text='valores:').grid(row=0,column=0)
Entry(pes3.frame,textvariable=numeros).grid(row=0,column=1)
Button(pes3.frame,text='agregar',command=add_moda).grid(row=0,column=3)

Label(pes3.frame,text='Moda:').grid(row=1,column=0)
Entry(pes3.frame,textvariable=moda).grid(row=1,column=1)

Button(pes3.frame2,text='calcular',command=cal_moda).grid(row=0,column=0)
Button(pes3.frame2,text='limpiar',command=limpiar).grid(row=0,column=1)
Button(pes3.frame2,text='CERRAR',command=cerrar_prog).grid(row=1,columnspan=3)


root.mainloop()
