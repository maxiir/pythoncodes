def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplicacion(num1,num2):
	return num1*num2

def division(num1,num2):
	try:                                                  #saltar linea por un error en el codigo
		return num1/num2
	except ZeroDivisionError:                             #nombre del error
		print("imposible dividir entre 0")
		return "error en operacion"                          
def potencia(num1,num2):
	return num1**num2

while True:
	try:
		num1=int(input("\nintroduce un numero: "))
		num2=int(input("\n introduce otro numero: "))
		break
	except ValueError:
		print("\noperacion incorrecta, intenta nuevamente")
		
calculo=str(input("\nPon la primera letra de lo que desea hacer (suma,multiplicacion,division,resta,potencia): "))

if calculo=="s":
	print(suma(num1,num2))
elif calculo=="p":
	print(potencia(num1,num2))
elif calculo=="r":
	print(resta(num1,num2))
elif calculo=="m":
	print(multiplicacion(num1,num2))
elif calculo=="d":
	print(division(num1,num2))
else:
	print("error en el calculo")
print("finalizacion de operacion")

