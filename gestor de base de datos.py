from tkinter import*
import sqlite3 
from tkinter import messagebox

#------------------------------------------funciones---------------------------------------------------------#
def nuevaBBDD():
	conexion=sqlite3.connect("nuevaBBDD")
	cursorBBDD=conexion.cursor()
	cursorBBDD.execute("CREATE TABLE CONTRASENAS (ID INTEGER PRIMARY KEY AUTOINCREMENT ,USUARIO VARCHAR(50), CONTRASENA VARCHAR(50),SITIO VARCHAR(50))")
	messagebox.showinfo("BBDD","Se creo exitosamente la nueva BBDD!")
	conexion.commit()



def conexionBBDD():
	
	conexion=sqlite3.connect("CLIENTES")
	cursorBBDD=conexion.cursor()
	
	
	try:
		cursorBBDD.execute("CREATE TABLE DATOSCLIENTES(ID INTEGER PRIMARY KEY AUTOINCREMENT, CLIENTE VARCHAR(50),TELEFONOS INTEGER(50),DIRECCION_LOCALIDAD VARCHAR(100),CORREO VARCHAR(50), INICIOS_AVANCES VARCHAR (200))")
		
		messagebox.showinfo("gestor de base de datos","Base de datos creada con exito!")
		
	except:
		
		messagebox.showwarning("atencion!","la base de datos ya existe!")

def salirapp():
	
	respuesta=messagebox.askquestion("salir","Desea salir del programa?") #genera una pregunta antes de salir
	if respuesta=="yes":
		root.destroy()#salir completamente del programa

def limpiarCAMPOS():
	
	Id.set("")
	cliente.set("")
	telefonos.set("")
	direccion.set("")
	correo.set("")
	iniciosAvances.set("")
		

def agregar():
	
	conexion=sqlite3.connect("CLIENTES")
	cursorBBDD=conexion.cursor()
	
	cursorBBDD.execute("INSERT INTO DATOSCLIENTES VALUES(NULL,'"+ cliente.get()+"','"+telefonos.get()+"','"+direccion.get()+"','"+correo.get()+"','"+iniciosAvances.get()+"')")
	conexion.commit()
	messagebox.showinfo("BBDD","Los registros fueron AGREGADOS exitosamente!")



def leer():
	
	conexion=sqlite3.connect("CLIENTES")
	cursorBBDD=conexion.cursor()
	
	cursorBBDD.execute("SELECT * FROM DATOSCLIENTES WHERE ID ="+ Id.get())
	
	elCliente=cursorBBDD.fetchall()
	
	for mostrarDATO in elCliente: #mostrarDATO creado nuevo
		
		Id.set(mostrarDATO[0])
		cliente.set(mostrarDATO[1])
		telefonos.set(mostrarDATO[2])
		direccion.set(mostrarDATO[3])
		correo.set(mostrarDATO[4])
		iniciosAvances.set(mostrarDATO[5])
	
	conexion.commit()


def actualizar():
	
	conexion=sqlite3.connect("CLIENTES")
	cursorBBDD=conexion.cursor()
		
	cursorBBDD.execute("UPDATE DATOSCLIENTES SET CLIENTE='"+cliente.get()+"',TELEFONOS='"+telefonos.get()+"',DIRECCION_LOCALIDAD='"+direccion.get()+"',CORREO='"+correo.get()+"',INICIOS_AVANCES='"+iniciosAvances.get()+"' WHERE ID="+Id.get())
	
	conexion.commit()
	messagebox.showinfo("BBDD","Los registros fueron ACTUALIZADOS exitosamente!")	


def eliminar():
	
	conexion=sqlite3.connect("CLIENTES")
	cursorBBDD=conexion.cursor()
	
	cursorBBDD.execute("DELETE FROM DATOSCLIENTES WHERE ID="+Id.get())
	
	conexion.commit()
	
	messagebox.showinfo("Base de datos","Registro ELIMINADO exitosamente!")

def acerca():
	messagebox.showinfo("acerca de...","Desarrollador: Maximiliano Rucci\nversion: 1.0.0\nCorreo:Maxiirucci@gmail.com")


root=Tk()
root.title("Gestor de BBDD")



#---------------------------barraMenu---------------------------------------------------------#
barraMenu=Menu(root)
root.config(menu=barraMenu ,bg="#2874A6")#,width=200,height=300)

bbddMENU=Menu(barraMenu,tearoff=0)
bbddMENU.add_command(label="crear BBDD", command=conexionBBDD) #lo q se despliega en el menu al pulsar
bbddMENU.add_command(label="nueva BBDD",command=nuevaBBDD)
bbddMENU.add_command(label="salir", command=salirapp)

optMENU=Menu(barraMenu,tearoff=0)
optMENU.add_command(label="borrar todos los campos",command=limpiarCAMPOS)

ayudaMENU=Menu(barraMenu,tearoff=0)
ayudaMENU.add_command(label="acerca de...",command=acerca)
ayudaMENU.add_command(label="licencia")

barraMenu.add_cascade(label="BBDD",menu=bbddMENU) #agregar a la barra de menu los ya creados label y menus
barraMenu.add_cascade(label="opciones",menu=optMENU)
barraMenu.add_cascade(label="Acerca de...",menu=ayudaMENU)


root.geometry("540x450+0+0")
root.resizable(False,False)
frame=Frame(root,bg="#2874A6",width=500,height=500)
frame.pack()
frame2=Frame(root,bg="#2874A6",width=500,height=500)
frame2.pack()
frame3=Frame(root,bg="#2874A6",width=500,height=200)
frame3.pack()

#---------------------------------------------------campos-----------------------------------------------------#
Id=StringVar()
cliente=StringVar()
telefonos=StringVar()
direccion=StringVar()
correo=StringVar()
iniciosAvances=StringVar()

imagen=PhotoImage(file="derecho.gif")
Label(frame,image=imagen,bg="#2874A6",fg="#2874A6").grid(row=1,column=1)

Label(frame2,text="ID",bg="#2874A6").grid(row=3,column=0,padx=5,pady=5)
Entry(frame2,textvariable=Id).grid(row=3,column=1,padx=5,pady=5)

Label(frame2,text="Cliente",bg="#2874A6").grid(row=4,column=0,padx=5,pady=5)
Entry(frame2,textvariable=cliente).grid(row=4,column=1,padx=5,pady=5)

Label(frame2,text="Telefono-Cel",bg="#2874A6").grid(row=5,column=0,padx=5,pady=5)
Entry(frame2,textvariable=telefonos).grid(row=5,column=1,padx=5,pady=5)

Label(frame2, text="Direccion-Localidad",bg="#2874A6").grid(row=6,column=0,padx=5,pady=5)
Entry(frame2,textvariable=direccion).grid(row=6,column=1,padx=5,pady=5)

Label(frame2, text="Correo",bg="#2874A6").grid(row=7,column=0,padx=5,pady=5)
Entry(frame2,textvariable=correo).grid(row=7,column=1,padx=5,pady=5)

Label(frame2, text="inicios/avaces",bg="#2874A6").grid(row=8,column=0,padx=5,pady=5)
Entry(frame2,textvariable=iniciosAvances).grid(row=8,column=1,padx=5,pady=5)


Label(frame3,text="Opciones:",bg="#5DADE2").grid(row=9,column=0,padx=5,pady=5)
Button(frame3,text="AGREGAR",command=agregar).grid(row=9,column=1,padx=5,pady=5)
Button(frame3,text="LEER",command=leer).grid(row=9,column=2,padx=5,pady=5)
Button(frame3,text="ELIMINAR",command=eliminar).grid(row=9,column=3,padx=5,pady=5)
Button(frame3,text="ACTUALIZAR",command=actualizar).grid(row=9,column=4,padx=5,pady=5)





root.mainloop()
