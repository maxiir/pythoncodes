i=1                             #de donde arranca el contador
while i<=10:                    #sentencia verdadera o farza
	print("proceso")            #lo q va a ir poniendo mientras sea falsa la sentencia
	i=i+1 
	                            #de a cuanto queremos ir contando
print("finalizacion")           #finaliza el siclo de while
#...........................................................................................
mi_edad=int(input("\npor favor coloca tu edad: "))

while mi_edad<=0 or mi_edad>=100:        #while sentencia a validar para continuar, "or" para agregar mas requisitos 
	print("edad incorrecta pon otra: ")
	mi_edad=int(input("por favor coloca tu edad de nuevo: "))	

print("\nmuchas gracias!")
print("su edad: "+ str(mi_edad)+ " años")      #puede concatenar con la suma mas texto o valores en el print.

#...............................................................................................

contraseña=str(input("\ningrese su contraseña de desbloqueo: "))
intentos=0                                                          #contador de intentos

while contraseña!= "maxi":
	
	print("error, contraseña incorrecta")
	contraseña=str(input("ingrese otra contraseña: "))
	intentos=intentos+1
	if intentos==3:
		print("intentos agotados, bloqueo definitivo")
		break                                                        #finaliza el bucle while con break y sigue el codigo
	
if intentos<3:
	print("Muy bien contraseña correcta! "+str(intentos)+" intentos fallidos")


	


	
	