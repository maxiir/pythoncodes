import sqlite3
from tkinter import*
from sqlite3 import*
import sqlite3

root=Tk()
conexion=sqlite3.connect('BBDD')
cursor=conexion.cursor()

cursor.execute("SELECT DESCRIPCION FROM CATEGORIAS")
conexion.commit()




root.mainloop()