# creacion de una base de datos:
	#crear una coneccion
	#crear un cursor
	#crear la base de datos
	#crear las query(consultas de insertar,eliminar,etc)
	#guardar cambios
	#cerrar la coneccion
	#[ver la base con el programa visor db]

import sqlite3 

miconexion=sqlite3.connect("DATABASE")


micursor=miconexion.cursor()  #se crea el cursor

#micursor.execute("CREATE TABLE CLIENTES (NOMBRE_CLIENTE VARCHAR(50), DNI INTEGER, CORREO VARCHAR(50))") #una sola vez se ejecuta esta linea de creacion de tabla sino da error al ya estar creada la base

#---micursor.execute("INSERT INTO CLIENTES VALUES('MAXIMILIANO',40208871,'MAXIIRUCCI@GMAIL.COM')")


#---variosclientes=[("pepe",565659,"pepe123@gmail.com"),("lola",67363763,"lola@hotmail.com"),("tati",343545,"tati@gmail.com")]

#---micursor.executemany("INSERT INTO CLIENTES VALUES(?,?,?)",variosclientes) #se pone un signo de pregunta por cada item

micursor.execute("SELECT * FROM CLIENTES")  #ver en consola
variosclientes=micursor.fetchall() #ver en consola
print(variosclientes) #ver en consola

miconexion.commit() #confirma los cambios realizados en la tabla se hace una vez

miconexion.close()