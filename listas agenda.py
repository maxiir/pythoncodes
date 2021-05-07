import pandas as pd

telefonos=[]

def agenda():
	numerosNEW=int(input("agregue un telefono: "))
	telefonos.append(numerosNEW)
	nombres=str(input("agregue el nombre a agendar: "))
	telefonos.append(nombres)
	
	respuesta=str(input("desea agregar mas numeros de telefono? s/n: "))
	while respuesta == 's':
		agenda()
	else:
		print("Datos almacenados: ",telefonos[:])
		exit()	
#---------------------------------------------------------------------------------------#
numerosNEW=int(input("agregue un telefono: "))
telefonos.append(numerosNEW)
nombres=str(input("agregue el nombre a agendar: "))
telefonos.append(nombres)


respuesta=str(input("desea agregar mas numeros de telefono? s/n: "))

while respuesta == 's':
	agenda()
else:
	print("Datos almacenados: ",telefonos[:])
	exit()
	
	
	
#valores.append(200) #append agrega de a un elemento por linea
#valores.append("maxi")

