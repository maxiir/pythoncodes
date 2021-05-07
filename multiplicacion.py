
def inicio():
	
	def mult(num1,num2):
		return num1*num2
	print("\ningresa tus numeros de a uno:\n")
	num1=int(input("> "))
	num2=int(input("> "))
	
	mult(num1, num2)
	print(mult(num1, num2))
	respuesta=str(input("\ndesea continuar?(yes/no): "))
	
	if respuesta=="yes":
		inicio()
	else:
		exit()
	
	inicio()


def mult(num1,num2):
	return num1*num2
	
print( "                                  Ah multiplicar!\n")

print("ingresa tus numeros de a uno:\n")
num1=int(input("> "))
num2=int(input("> "))

mult(num1, num2)
print(mult(num1, num2))
respuesta=str(input("\ndesea continuar?(yes/no): "))

if respuesta=="yes":
	inicio()
else:
	exit()
	
	
