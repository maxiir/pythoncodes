from tkinter import*
from tkinter import ttk

'''
root=Tk()
root.title("GB modificar busqueda de perfil")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

Label(frame1,text='Nombre:').grid(row=0,column=0)
Entry(frame1).grid(row=0,column=1)
Label(frame1,text='Tipo:').grid(row=1,column=0)
Entry(frame1).grid(row=1,column=1)
Label(frame1,text='Descripcion:').grid(row=2,column=0)
Entry(frame1).grid(row=2,column=1)
Label(frame1,text='Perfil:').grid(row=3,column=0)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text='Requisitos:').grid(row=4,column=0)
Entry(frame1).grid(row=4,column=1)
Label(frame1,text='Categoria:').grid(row=5,column=0)
box=ttk.Combobox(frame1).grid(row=5,column=1)
#box['values']='profesional'
Label(frame1,text='Responsable:').grid(row=6,column=0)
Entry(frame1).grid(row=6,column=1)
Label(frame1,text='Direccion:').grid(row=7,column=0)
Entry(frame1).grid(row=7,column=1)
Label(frame1,text='Nivel de puesto:').grid(row=8,column=0)
box2=ttk.Combobox(frame1).grid(row=8,column=1)
Label(frame1,text='Lugar:').grid(row=9,column=0)
box3=ttk.Combobox(frame1).grid(row=9,column=1)
Label(frame1,text='Fecha de comienzo:').grid(row=10,column=0)
box4=ttk.Combobox(frame1).grid(row=10,column=1)
Label(frame1,text='Vacante disponible:').grid(row=11,column=0)
box5=ttk.Combobox(frame1).grid(row=11,column=1)
Label(frame1,text='Vacante cubiertas:').grid(row=12,column=0)
box5=ttk.Combobox(frame1).grid(row=12,column=1)
Label(frame1,text='Fecha de cierre:').grid(row=13,column=0)
box5=ttk.Combobox(frame1).grid(row=13,column=1)

Button(frame2,text='Modificar').grid(row=0,column=1)
Button(frame2,text='Salir').grid(row=0,column=0)

'''
'''

root=Tk()
root.title("GB consultar busqueda de perfil")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

Label(frame1,text='Nombre:').grid(row=0,column=0)
Entry(frame1).grid(row=0,column=1)

Label(frame1,text='Descripcion:').grid(row=1,column=0)
Entry(frame1).grid(row=1,column=1)


Label(frame1,text='Categoria:').grid(row=2,column=0)
box=ttk.Combobox(frame1).grid(row=2,column=1)
#box['values']='profesional'
Label(frame1,text='Responsable:').grid(row=3,column=0)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text='Direccion:').grid(row=4,column=0)
Entry(frame1).grid(row=4,column=1)
Label(frame1,text='Nivel de puesto:').grid(row=5,column=0)
box2=ttk.Combobox(frame1).grid(row=5,column=1)
Label(frame1,text='Lugar:').grid(row=6,column=0)
box3=ttk.Combobox(frame1).grid(row=6,column=1)

Label(frame1,text='Busquedas cerradas:').grid(row=7,column=0)
box5=ttk.Combobox(frame1).grid(row=7,column=1)
Label(frame1,text='Vacantes pendientes:').grid(row=8,column=0)
box5=ttk.Combobox(frame1).grid(row=8,column=1)


Button(frame2,text='Filtrar').grid(row=0,column=1)
Button(frame2,text='Limpiar').grid(row=0,column=2)
Button(frame2,text='Salir').grid(row=0,column=0)
'''
'''
root=Tk()
root.title("GB registrar busqueda de perfil")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

Label(frame1,text='Nombre:').grid(row=0,column=0)
Entry(frame1).grid(row=0,column=1)
Label(frame1,text='Tipo:').grid(row=1,column=0)
Entry(frame1).grid(row=1,column=1)
Label(frame1,text='Descripcion:').grid(row=2,column=0)
Entry(frame1).grid(row=2,column=1)
Label(frame1,text='Perfil:').grid(row=3,column=0)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text='Requisitos:').grid(row=4,column=0)
Entry(frame1).grid(row=4,column=1)
Label(frame1,text='Categoria:').grid(row=5,column=0)
box=ttk.Combobox(frame1).grid(row=5,column=1)
#box['values']='profesional'
Label(frame1,text='Responsable:').grid(row=6,column=0)
Entry(frame1).grid(row=6,column=1)
Label(frame1,text='Direccion:').grid(row=7,column=0)
Entry(frame1).grid(row=7,column=1)
Label(frame1,text='Nivel de puesto:').grid(row=8,column=0)
box2=ttk.Combobox(frame1).grid(row=8,column=1)
Label(frame1,text='Lugar:').grid(row=9,column=0)
box3=ttk.Combobox(frame1).grid(row=9,column=1)
Label(frame1,text='Fecha de comienzo:').grid(row=10,column=0)
box4=ttk.Combobox(frame1).grid(row=10,column=1)
Label(frame1,text='Vacante disponible:').grid(row=11,column=0)
box5=ttk.Combobox(frame1).grid(row=11,column=1)
Label(frame1,text='Vacante cubiertas:').grid(row=12,column=0)
box5=ttk.Combobox(frame1).grid(row=12,column=1)
Label(frame1,text='Fecha de cierre:').grid(row=13,column=0)
box5=ttk.Combobox(frame1).grid(row=13,column=1)

Button(frame2,text='Nuevo').grid(row=0,column=1)
Button(frame2,text='Salir').grid(row=0,column=0)
Button(frame2,text='Limpiar campos').grid(row=0,column=2)
Button(frame2,text='Guardar').grid(row=0,column=3)
'''
root=Tk()
root.title("GB eliminar busqueda de perfil")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()

Label(frame1,text='Nombre:').grid(row=0,column=0)
Entry(frame1).grid(row=0,column=1)
Label(frame1,text='Tipo:').grid(row=1,column=0)
Entry(frame1).grid(row=1,column=1)
Label(frame1,text='Descripcion:').grid(row=2,column=0)
Entry(frame1).grid(row=2,column=1)
Label(frame1,text='Perfil:').grid(row=3,column=0)
Entry(frame1).grid(row=3,column=1)
Label(frame1,text='Requisitos:').grid(row=4,column=0)
Entry(frame1).grid(row=4,column=1)
Label(frame1,text='Categoria:').grid(row=5,column=0)
box=ttk.Combobox(frame1).grid(row=5,column=1)
#box['values']='profesional'
Label(frame1,text='Responsable:').grid(row=6,column=0)
Entry(frame1).grid(row=6,column=1)
Label(frame1,text='Direccion:').grid(row=7,column=0)
Entry(frame1).grid(row=7,column=1)
Label(frame1,text='Nivel de puesto:').grid(row=8,column=0)
box2=ttk.Combobox(frame1).grid(row=8,column=1)
Label(frame1,text='Lugar:').grid(row=9,column=0)
box3=ttk.Combobox(frame1).grid(row=9,column=1)
Label(frame1,text='Fecha de comienzo:').grid(row=10,column=0)
box4=ttk.Combobox(frame1).grid(row=10,column=1)
Label(frame1,text='Vacante disponible:').grid(row=11,column=0)
box5=ttk.Combobox(frame1).grid(row=11,column=1)
Label(frame1,text='Vacante cubiertas:').grid(row=12,column=0)
box5=ttk.Combobox(frame1).grid(row=12,column=1)
Label(frame1,text='Fecha de cierre:').grid(row=13,column=0)
box5=ttk.Combobox(frame1).grid(row=13,column=1)

Button(frame2,text='Eliminar').grid(row=0,column=1)
Button(frame2,text='Salir').grid(row=0,column=0)



root.mainloop()