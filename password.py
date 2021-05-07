def start():                                 #funcion para repetir bloque de codigo
                                             #inicia el bloque de funcion
	
	respuesta=str(input("por favor ingrese su password: "))
	
	cont=0

	while respuesta!= '1234':
		cont=cont+1
		respuesta=str(input("coloque de nuevo el password: "))
		if cont==2:
			print("intentos agotados!")
			condicion=str(input("desea volver a intentarlo?(yes/no): "))
			if condicion=='yes':
				start()
			else:
				exit()
			
	if respuesta == '1234':
		print("muchas gracias!")
		condicion=str(input("quiere intentar lo de nuevo? (yes/no): "))
		if condicion=='yes':
			start()
		else:
			exit()	
start()                                       #termina bloque de funcion

respuesta=str(input("por favor ingrese su password: "))

cont=0

while respuesta!= '1234':
	cont=cont+1
	respuesta=str(input("coloque de nuevo el password: "))
	if cont==2:
		print("intentos agotados!")
		condicion=str(input("desea volver a intentarlo?(yes/no): "))
		if condicion=='yes':
			start()
		else:
			exit()
		
if respuesta == '1234':
	print("muchas gracias!")
	condicion=str(input("quiere intentar lo de nuevo? (yes/no): "))
	if condicion=='yes':
		start()
	else:
		exit()
		
	

	