def start():
	
	def area_triangulo ():
		base,altura=float(input("\nbase:")),float(input("altura:"))
		resultado=(base*altura)/2
		return print("area del triangulo:",resultado)
	try:
		triangulo=area_triangulo()
	except ValueError:
		print("                         [Por favor no introduzca LETRAS o COMAS]")
		
		respuesta2=str(input("\ndesea volver a intentarlo?(yes/no):"))
		
		while respuesta2!='yes'and respuesta2!='no':
			respuesta2=input("por favor coloque la respuesta correcta:")
			
		if respuesta2=='yes':
			start()
			
		else:
			print("muchas gracias!")
			exit()

	respuesta=input("desea calcular otro triangulo?(yes/no):")
		
	while respuesta!='yes' and respuesta!='no':
		respuesta=input("por favor coloque (YES/NO):")
	if respuesta=='yes':
		start()
	else:
		print("muchas gracias!")
		exit()
	
#<--------------------------------------------------------------------start-------------------------------------------------------------------->	
def area_triangulo ():
	base,altura=float(input("\nbase:")),float(input("altura:"))
	resultado=(base*altura)/2
	return print("area del triangulo:",resultado)
try:
	triangulo=area_triangulo()
except ValueError:
	print("                         [Por favor no introduzca LETRAS o COMAS]")
	
	respuesta2=str(input("\ndesea volver a intentarlo?(yes/no):"))
	
	while respuesta2!='yes' and respuesta2!='no':
		respuesta2=input("por favor coloque la respuesta correcta:")
	
	if respuesta2=='yes':
		start()
	
	else:
		print("muchas gracias!!")
		exit()
	
respuesta=input("desea calcular otro triangulo?(yes/no):")
	
while respuesta!='yes' and respuesta!='no':
	respuesta=input("por favor coloque (YES/NO):")
if respuesta=='yes':
	start()
else:
	print("muchas gracias!")
	exit()



#Area_De_Un_Triangulo= lambda base, altura:(base*altura)/2   #lamda sirve solo para calcular sin condicionales y sin bucles es para calculos rapidos

