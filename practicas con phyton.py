def numeros ():   #funcion
   print(8)
   print(10)      #cuerpo de la funcion 
   print(30)

numeros()        #llamado de la funcion propia

def producto ():  #otra funcion propia
	num1=30
	num2=90
	print(num1*num2)

producto()      #llamado a funcion propia
#.............................................................................

def multiplicacion(num1, num2):
	print(num1*num2)

multiplicacion(33, 5)

multiplicacion(22, 4)

multiplicacion(20, 2)

#.....................................................................

def producto (num1, num2):
	resultado=num1*num2
	return resultado          #devuelve un valor guardado en memoria
EstoVale=producto(5,15)
print(EstoVale)

#.....................................................................



