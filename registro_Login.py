from sqlite3.dbapi2 import Date
from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import smtplib
import random

codigo_generado=''

def desuscribirse(): #revisar
    #buscador de peticiones de eliminacion:
    conexion=sqlite3.connect('bbdd_sesion')
    cursor=conexion.cursor()
    cursor.execute("SELECT CORREO_MAIL,PETICION_ELIMINACION FROM CUENTAS_CLIENTES WHERE CORREO_MAIL='"+DEL_CORREO.get()+"' AND PETICION_ELIMINACION='SI' ")
    buscar_peticion=cursor.fetchall()

    cursor.execute("SELECT CORREO_MAIL FROM CUENTAS_CLIENTES WHERE CORREO_MAIL='"+DEL_CORREO.get()+"' and CUENTA_VALIDADA='SI' ")
    buscar_correo_del=cursor.fetchall()

    cursor.execute("SELECT COD_VALIDACION,CORREO_MAIL FROM CUENTAS_CLIENTES WHERE COD_VALIDACION='"+DEL_CODIGO.get()+"' AND PETICION_ELIMINACION='SI' ")
    buscar_cod_del=cursor.fetchall()



    global codigo_generado
    caracteres=['C','D','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y','Z','2','3','4','6','7','9']
            
    for i in range(5):
        codigo_generado=codigo_generado+random.choice(caracteres)
            
    print(codigo_generado)

    if buscar_peticion==[] and DEL_CORREO.get()!=''and DEL_CODIGO.get()=='' and buscar_correo_del!=[]:
        while DEL_CORREO.get()!=''and DEL_CODIGO.get()=='':
            mensaje="Hola!, Lamentamos que se desuscriba de nuestra plataforma,su codigo de eliminacion\n\nCODIGO= '"+codigo_generado+"' " #NO PONER ':' EN LOS MENSAJES
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('maxiirucci@gmail.com','maxilo+10')
            try:
                server.sendmail('maxiirucci@gmail.com',DEL_CORREO.get(),mensaje)
            except:
                messagebox.showinfo('Error','Correo incorrecto,vuelva a introducirlo')
                codigo_generado=''
                DEL_CORREO.set('introduzca el @...')
                server.quit()
                break
            messagebox.showinfo('Desuscribcion','Revise su bandeja de entrada e introduzca el codigo de eliminacion')
            conexion=sqlite3.connect('bbdd_sesion')
            cursor=conexion.cursor()
            cursor.execute("UPDATE CUENTAS_CLIENTES SET COD_VALIDACION='"+codigo_generado+"',PETICION_ELIMINACION='SI',FECHA_DE_CARGA=CURRENT_TIMESTAMP WHERE CORREO_MAIL='"+DEL_CORREO.get()+"' and CUENTA_VALIDADA='SI' and PETICION_ELIMINACION='NO' ")
            conexion.commit()
            break
        
    elif buscar_peticion!=[] and DEL_CORREO.get()!='' and DEL_CODIGO.get()!='' and buscar_correo_del!=[] and buscar_cod_del!=[]:
        res=messagebox.askquestion('desuscricion','Esta seguro que desea eliminar su cuenta?')
        if res=='yes':
            cursor.execute("DELETE FROM CUENTAS_CLIENTES WHERE COD_VALIDACION='"+DEL_CODIGO.get()+"' ")
            conexion.commit()
            messagebox.showinfo("desuscribirse","Cuenta eliminada exitosamente!")
            #cosas q pueden pasar en los campos y respuestas--->
    elif DEL_CORREO.get()=='' and DEL_CODIGO.get()=='':
        messagebox.showinfo('Error','Campo correo vacio')
        codigo_generado=''
    elif DEL_CORREO.get()!=''and DEL_CODIGO.get()!='':
        messagebox.showinfo('Error','Correo y codigo incorrecto')
        codigo_generado=''
    elif DEL_CORREO.get()==''and DEL_CODIGO.get()!='':
        messagebox.showinfo('Error','Codigo incorrecto')
        codigo_generado=''
    
    elif buscar_correo_del==[] and DEL_CODIGO.get()=='':
        messagebox.showinfo('Error','Cuenta no encontrada')
        codigo_generado=''
        

def inicio_sesion():
    
    while LOG_CORREO.get()!='' and LOG_CONTRASENA.get()!='':
        conexion=sqlite3.connect('bbdd_sesion')
        cursor=conexion.cursor()
        try:
            cursor.execute("CREATE TABLE INICIOS_SESION (ID INTEGER PRIMARY KEY AUTOINCREMENT, CORREO VARCHAR(50),CONTRASENA VARCHAR(50),FECHA_HORA DATE)")
            conexion.commit()
        except:
            print('ya esta creada la tabla INICIOS_SESION')
        
        #busca datos de inicio de sesion-------------------------------->
        cursor.execute("SELECT CORREO_MAIL, CONTRASENA FROM CUENTAS_CLIENTES WHERE CORREO_MAIL='"+LOG_CORREO.get()+"' and CONTRASENA='"+LOG_CONTRASENA.get()+"' and CUENTA_VALIDADA='SI' ")
        
        inicio=cursor.fetchall() #MUSTRA RESULTADOS DE SQL BBDD EN VARIABLE
        #print('lo q se encontro',inicio)
        if inicio==[]:
            messagebox.showinfo('Login','Error no registrado o correo/contrasena incorrecta')
            
        else:
            messagebox.showinfo('Login','Inicio de sesion con exito!')
            cursor.execute("INSERT INTO INICIOS_SESION VALUES(NULL, '"+LOG_CORREO.get()+"','"+LOG_CONTRASENA.get()+"',CURRENT_TIMESTAMP)")
            conexion.commit()
        break

    
    if LOG_CORREO.get()=='' and LOG_CONTRASENA.get()=='':
        messagebox.showinfo('Login','Error, campos vacios')
    elif LOG_CORREO.get()=='':
        messagebox.showinfo('login','Error, campo correo vacio')
    elif LOG_CONTRASENA.get()=='':
        messagebox.showinfo('login','Error, campo contrasena vacio')
    

def validar(): #NO TOCAR
    #BUSCAR CODIGO GENERADO Y CORREO REGISTRADO------>

    conexion=sqlite3.connect('bbdd_sesion')
    cursor=conexion.cursor()
    
    cursor.execute("SELECT COD_VALIDACION FROM CUENTAS_CLIENTES WHERE COD_VALIDACION='"+VAL_CODIGO.get()+"' ")
    conexion.commit()
    buscar_code=cursor.fetchall()
    #print('buco el codigo==',buscar_code)
    
    cursor.execute("SELECT CORREO_MAIL FROM CUENTAS_CLIENTES WHERE CORREO_MAIL='"+VAL_CORREO.get()+"' ")
    conexion.commit()
    buscar_correo=cursor.fetchall()
    #print('busco el correo==',buscar_correo)


    while buscar_correo!=[] and buscar_code!=[]:
        #conexion=sqlite3.connect(host='localhost',user='root',password='123',database='bbdd_sesion') # OTRA FORMA DE ARMAR
        conexion=sqlite3.connect('bbdd_sesion')
        cursor=conexion.cursor()
        cursor.execute("UPDATE CUENTAS_CLIENTES SET CUENTA_VALIDADA='SI',FECHA_DE_CARGA=CURRENT_TIMESTAMP WHERE CORREO_MAIL='"+VAL_CORREO.get()+"' ")
        conexion.commit()
        messagebox.showinfo('Validacion','Cuenta creada con exito!')
        break
    
    if VAL_CODIGO.get()=='' and buscar_correo!=[]:
        messagebox.showinfo('Validacion','Error campo codigo vacio')
    elif buscar_code!=[] and VAL_CORREO.get()=='':
        messagebox.showinfo('Validacion','Error campo correo vacio')
    elif VAL_CORREO.get()=='' and VAL_CODIGO.get()=='':
        messagebox.showinfo('Validacion','Error campo correo y codigo vacios')
    elif buscar_code!=[] and buscar_correo==[]:
        messagebox.showinfo('Validacion','Error correo no registrado')
    elif buscar_correo!=[] and buscar_code==[]:
        messagebox.showinfo('Validacion','Error codigo incorrecto')
    elif buscar_code==[] and buscar_correo==[]:
        messagebox.showinfo('Validacion','Error campos codigo y correo incorrectos')
    

def notificacion():
#----------------------------------BBDD---------------------------------------->



    conexion=sqlite3.connect('bbdd_sesion')
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE CUENTAS_CLIENTES(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50),APELLIDO VARCHAR(50),CONTRASENA VARCHAR(50),REPE_CONTRASENA VARCHAR(50),CORREO_MAIL VARCHAR(50),COD_VALIDACION VARCHAR(50),CUENTA_VALIDADA CHAR(50),PETICION_ELIMINACION CHAR(50),FECHA_DE_CARGA DATE )")
        conexion.commit()
    except:
        print('ya fue creada la tabla cuentas_clientes')
    
    #busca cuentas ya validadas------->
    #se pueden mandar mail al mismo correo hasta q se valide

    cursor.execute("SELECT CORREO_MAIL,CUENTA_VALIDADA FROM CUENTAS_CLIENTES WHERE CORREO_MAIL='"+CORREO.get()+"' AND CUENTA_VALIDADA='SI' ")
    conexion.commit()
    buscar_cuenta_vali=cursor.fetchall()
    #print('lo q se encontro de cuenta validada',buscar_cuenta_vali)


    while REP_CONTRASENA.get()==CONTRASENA.get() and CONTRASENA.get()!='' and  REP_CONTRASENA.get()!='' and CORREO.get()!='' and NOMBRE.get()!='' and APELLIDO.get()!='' and buscar_cuenta_vali==[]: #and (y ademas...)agrega una condicion mas q se tiene q cumplir- mientras se cumpla se hace 

        #---------------------CREACION_DEL_CODIGO---------------------------------------------
        global codigo_generado
        caracteres=['C','D','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y','Z','2','3','4','6','7','9']
            
        for i in range(5):
            codigo_generado=codigo_generado+random.choice(caracteres)
            
        print(codigo_generado)
            
        #----------------------MAIL_POR_CORREO-------------------------------------------------
        mensaje="Hola '"+NOMBRE.get()+"'!,su codigo de validacion\n\nCODIGO= '"+codigo_generado+"' " #NO PONER ':' EN LOS MENSAJES
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('maxiirucci@gmail.com','maxilo+10')
        try:
            server.sendmail('maxiirucci@gmail.com',CORREO.get(),mensaje)
        except:
            messagebox.showinfo('Error','Correo incorrecto,vuelva a introducirlo')
            codigo_generado=''
            CORREO.set('introduzca el @...')
            server.quit()
            break #evita q se envie el mail a un correo erroneo para luego volver a introducirlo bien
        

        cursor.execute("INSERT INTO CUENTAS_CLIENTES VALUES(NULL,'"+NOMBRE.get()+"','"+APELLIDO.get()+"','"+CONTRASENA.get()+"','"+REP_CONTRASENA.get()+"','"+CORREO.get()+"','"+codigo_generado+"','NO','NO',CURRENT_TIMESTAMP)")
        conexion.commit()
        messagebox.showinfo('Registro','Revise su bandeja de entrada de Mail e inicie sesion')
        codigo_generado=''
        break
             
    if buscar_cuenta_vali!=[] and NOMBRE.get()!='' and APELLIDO.get()!='' and CONTRASENA.get()!='' and REP_CONTRASENA.get()==CONTRASENA.get() and CORREO.get()!='':
        messagebox.showinfo('Error','El correo ya fue registrado')
        print('*salto un error') 

    elif REP_CONTRASENA.get()!= CONTRASENA.get() or REP_CONTRASENA.get()=='' or CONTRASENA.get()=='': #modifique if
        messagebox.showerror('Error','contrasenas diferentes o campo vacio, vuelva a intentarlo nuevamente')
        #exit('mal contrasena') se cierra todo completamente y da un mensaje en consola
        REP_CONTRASENA.set('')
        CONTRASENA.set('')
        print('*salto un error')
        
    elif NOMBRE.get()=='' or APELLIDO.get()=='' or CORREO.get()=='':
        messagebox.showerror('Error','campo vacio, vuelva a intentarlo nuevamente')
        print('*salto un error')
    '''
    elif NOMBRE.get()==True or APELLIDO.get()==True or NOMBRE.get() and APELLIDO.get()==True:#ver
        messagebox.showinfo('Error','Numeros en campo apellido y nombre no validos')
'''
        
    


def salir_app():
    root.destroy()
    
class los_frames():
    def __init__(self):
        self.frame=Frame()
        self.frame.pack()
        
root=Tk()
root.geometry('500x400')
root.title('Inicio de sesion')
pestana_root=ttk.Notebook()
pestana_root.pack(fill='both',expand='yes')

pestana_registrarse=ttk.Frame(pestana_root)
pestana_validacion=ttk.Frame(pestana_root)
pestana_login=ttk.Frame(pestana_root)
pestana_desuscribir=ttk.Frame(pestana_root)

pestana_root.add(pestana_registrarse,text='Registrarse')
pestana_root.add(pestana_validacion,text='Validacion de cuenta')
pestana_root.add(pestana_login,text='Login')
pestana_root.add(pestana_desuscribir,text='Desuscribirse')

frame1_pes_registrar=los_frames()
frame1_pes_registrar.frame=Frame(pestana_registrarse)
frame1_pes_registrar.frame.pack()
frame2_pes_registrar=los_frames()
frame2_pes_registrar.frame=Frame(pestana_registrarse)
frame2_pes_registrar.frame.pack()

frame1_pes_validacion=los_frames()
frame1_pes_validacion.frame=Frame(pestana_validacion)
frame1_pes_validacion.frame.pack()
frame2_pes_validacion=los_frames()
frame2_pes_validacion.frame=Frame(pestana_validacion)
frame2_pes_validacion.frame.pack()

frame1_pes_login=los_frames()
frame1_pes_login.frame=Frame(pestana_login)
frame1_pes_login.frame.pack()
frame2_pes_login=los_frames()
frame2_pes_login.frame=Frame(pestana_login)
frame2_pes_login.frame.pack()

frame1_pes_desuscribirse=los_frames()
frame1_pes_desuscribirse.frame=Frame(pestana_desuscribir)
frame1_pes_desuscribirse.frame.pack()
frame2_pes_desuscribirse=los_frames()
frame2_pes_desuscribirse.frame=Frame(pestana_desuscribir)
frame2_pes_desuscribirse.frame.pack()

NOMBRE=StringVar()
APELLIDO=StringVar()
CONTRASENA=StringVar()
REP_CONTRASENA=StringVar()
CORREO=StringVar()

VAL_CORREO=StringVar()
VAL_CODIGO=StringVar()

LOG_CORREO=StringVar()
LOG_CONTRASENA=StringVar()

DEL_CORREO=StringVar()
DEL_CODIGO=StringVar()

#-----------------------REGISTRAR
Label(frame1_pes_registrar.frame,text='Nombre:').grid(row=0,column=0)
Entry(frame1_pes_registrar.frame,textvariable=NOMBRE).grid(row=0,column=1)

Label(frame1_pes_registrar.frame,text='Apellido:').grid(row=1,column=0)
Entry(frame1_pes_registrar.frame,textvariable=APELLIDO).grid(row=1,column=1)

Label(frame1_pes_registrar.frame,text='Contrasena:').grid(row=2,column=0)
Entry(frame1_pes_registrar.frame,textvariable=CONTRASENA,show='*').grid(row=2,column=1)

Label(frame1_pes_registrar.frame,text='Repita la contrasena:').grid(row=3,column=0)
Entry(frame1_pes_registrar.frame,textvariable=REP_CONTRASENA,show='*').grid(row=3,column=1)

Label(frame1_pes_registrar.frame,text='Correo electronico:').grid(row=4,column=0)
Entry(frame1_pes_registrar.frame,textvariable=CORREO).grid(row=4,column=1)

Button(frame2_pes_registrar.frame,text='Aceptar',command=notificacion).grid(row=0,columnspan=2)
Button(frame2_pes_registrar.frame,text='Salir',command=salir_app).grid(row=1,columnspan=3)

#---------------------VALIDACION
Label(frame1_pes_validacion.frame,text='Correo:').grid(row=0,column=0)
Entry(frame1_pes_validacion.frame,textvariable=VAL_CORREO).grid(row=0,column=1)

Label(frame1_pes_validacion.frame,text='CODIGO:').grid(row=1,column=0)
Entry(frame1_pes_validacion.frame,textvariable=VAL_CODIGO).grid(row=1,column=1)


Button(frame2_pes_validacion.frame,text='Aceptar',command=validar).grid(row=0,columnspan=2)
Button(frame2_pes_validacion.frame,text='Salir',command=salir_app).grid(row=1,columnspan=3)

#----------------------LOGIN
Label(frame1_pes_login.frame,text='Correo:').grid(row=0,column=0)
Entry(frame1_pes_login.frame,textvariable=LOG_CORREO).grid(row=0,column=1)
Label(frame1_pes_login.frame,text='Contrasena:').grid(row=1,column=0)
Entry(frame1_pes_login.frame,textvariable=LOG_CONTRASENA,show='*').grid(row=1,column=1)

Button(frame2_pes_login.frame,text='iniciar sesion',command=inicio_sesion).grid(row=0,columnspan=2)
Button(frame2_pes_login.frame,text='Salir',command=salir_app).grid(row=1,columnspan=3)

#---------------------DESUSCRIBIRSE
Label(frame1_pes_desuscribirse.frame,text='Correo').grid(row=0,column=0)
Entry(frame1_pes_desuscribirse.frame,textvariable=DEL_CORREO).grid(row=0,column=1)
Label(frame1_pes_desuscribirse.frame,text='CODIGO').grid(row=1,column=0)
Entry(frame1_pes_desuscribirse.frame,textvariable=DEL_CODIGO).grid(row=1,column=1)

Button(frame2_pes_desuscribirse.frame,text='Salir',command=salir_app).grid(row=1,columnspan=3)
Button(frame2_pes_desuscribirse.frame,text='Eliminar cuenta',command=desuscribirse).grid(row=0,columnspan=3)



root.mainloop()

#IMPEDIR Q SE PUEDAN COLOCAR NUMEROS/alfanumericos EN EL CAMPO NOMBRE Y APELLIDO
#isnumeric()