print("             Programa de indice de masa corporal (I.M.C)")

def multi (altura):
	return altura*altura
def div (peso,altura):
	return peso/altura
	
def start():                                                   #funcion para repetir desde inicio
	try:
		peso=float(input("\nIntroduzca su PESO en (kg): "))
	except ValueError:
		print("(No use comas solo puntos)")
		peso=float(input("\nVuelva a introducir su PESO en (kg): "))
			
	try:
		altura=float(input("\nIntroduzca su ALTURA en (mts): "))
	except ValueError:
		print("(No use comas solo puntos)")
		altura=float(input("\nVuelva a introducir su ALTURA en (mts): "))
		
	try:	
		edad=int(input("\nIntroduzca su EDAD: "))
	except ValueError:
		print("(No coloque comas solo puntos)")
		edad=int(input("\nVuelva a introducir su EDAD: "))
		
	while peso<=0 or peso>=500:
		print("Peso incorrecto")
		peso=float(input("Vuelva a introducir su PESO: "))

	while altura<=0 or altura>=3.00:
		print("Altura incorrecta")
		try:
			altura=float(input("Vuelva a introducir su ALTURA en (mts): "))
		except ValueError:
			print("(Coloque la altura sin COMA solo con PUNTOS)")
		
	while edad<=0 or edad>=110:
		print("Edad incorrecta")
		edad=int(input("Vuelva a introducir su EDAD: "))
		
	calculo=multi(altura)
	imc=div(peso,calculo)


	if imc < 18.50:
		print("\nUsted esta por debajo del peso normal")
		print("I.M.C: "+str(imc))
	elif imc >18.50 and imc <25.00:
		print("\nUsted esta con un peso normal")
		print("I.M.C: "+str(imc))
	elif imc>25.00:
		print("\nUsted tiene sobre peso")
		print("I.M.C: "+str(imc))

	print("\nFinalizacion del programa de I.M.C...                                                          By: MaxiRucci")

	print("\nDesea calcular otro I.M.C?")
	respuesta=str(input("(yes,no): "))

	while respuesta!="yes" and respuesta!="no":
		print("respuesta incorrecta")
		respuesta=str(input("Vuelva a introducir su respuesta: "))
		
	if respuesta=="no":
			print("muchas gracias!")
			exit()                                   #terminar el programa en esa linea

	else:
		print("okay")
		start()                                      #llama funcion q inicia el codigo desde el inicio
	
try:
	peso=float(input("\nIntroduzca su PESO en (kg): "))
except ValueError:
	print("(No use comas solo puntos)")
	peso=float(input("\nVuelva a introducir su PESO en (kg): "))
		
try:
	altura=float(input("\nIntroduzca su ALTURA en (mts): "))
except ValueError:
	print("(No use comas solo puntos)")
	altura=float(input("\nVuelva a introducir su ALTURA en (mts): "))
	
try:	
	edad=int(input("\nIntroduzca tu EDAD: "))
except ValueError:
	print("(No coloque comas solo puntos)")
	edad=int(input("\nVuelva a introducir su EDAD: "))
	
while peso<=0 or peso>=500:
	print("Peso incorrecto")
	peso=float(input("Vuelva a introducir su PESO: "))

while altura<=0 or altura>=3.00:
	print("Altura incorrecta")
	try:
		altura=float(input("Vuelva a introducir su ALTURA en (mts): "))
	except ValueError:
		print("(Coloque la altura sin COMA solo con PUNTOS)")
	
while edad<=0 or edad>=110:
	print("Edad incorrecta")
	edad=int(input("Vuelva a introducir su EDAD: "))
	
calculo=multi(altura)
imc=div(peso,calculo)


if imc < 18.50:
	print("\nUsted esta por debajo del peso normal")
	print("I.M.C: "+str(imc))
elif imc >18.50 and imc <25.00:
	print("\nUsted esta con un peso normal")
	print("I.M.C: "+str(imc))
elif imc>25.00:
	print("\nUsted tiene sobre peso")
	print("I.M.C: "+str(imc))

print("\nFinalizacion del programa de I.M.C...                                                          By: MaxiRucci")

print("\nDesea calcular otro I.M.C?")
respuesta=str(input("(yes,no): "))

while respuesta!="yes" and respuesta!="no":
	print("respuesta incorrecta")
	respuesta=str(input("Vuelva a introducir su respuesta: "))
	
if respuesta=="no":
		print("muchas gracias!")
		exit()                                                               #terminar el programa ahi

else:
	print("okay")
	start()





 










