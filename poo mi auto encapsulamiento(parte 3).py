class Autos():
	
	def __init__(self):          #(__init__)contructor----> da esas caracteristicas mensionadas por defecto(iniciales)
	    self.__ruedas=4                  #estoy encapsulando con "self.__" las caracteristicas para q no sea modificable//solo se modifica en la clase
	    self.__puertas=5                        #propiedades de la clase ---> las caracteristicas de los objetos
	    self.__color='black'
	    self.__encendido=False
	
	def arrancar(self, arrancamos):                              
		self.__encendido=arrancamos              #ya no se fija lo q dice la clase sino el parametro q yo le indico
		
		if (self.__encendido):
			verificacion=self.__check()
		if (self.__encendido and verificacion):
			return "el coche esta encendido"
		elif (self.__encendido and verificacion== False):
			return "algo anda mal"		
		else:
			return "el auto esta parado"
		
		
		
	def caracteristicas(self):                     #muestra todas las caracteristicas del objeto q esta en la clase
		print("el auto tiene ",self.__ruedas,"ruedas",self.__puertas,"puertas y es color:",self.__color)
		
	def __check(self):                              #se implementa un chequeo de motor de metodo // esta encapsulado para q nose pueda modificar desde afuera de la clase
		print("chequeo de motor...")
		self.aceite="ok"
		self.agua="ok"
		self.nafta="ok"
		
		if (self.aceite=="ok" and self.agua=="ok" and self.nafta=="ok"):  # "and" ---> y ademas...
		
		    return True
		else:
			return False



Micoche=Autos()   #objeto creado y nombre a la clase q pertenece *comienza la programacion para ese objeto creado*//ya tienen un estado inicial o de fabrica

Micoche.caracteristicas()
print(Micoche.arrancar(True))                                   #muestra en pantalla como se encuentra el objeto

print("\n************************************CREACION DEL 2do OBJETO*******************************************\n")

Micoche2=Autos()         #ya cree el 2do objeto

Micoche2.caracteristicas()       #no es necesario poner un print para las caracteristicas ya q en el metodo se pone
#Micoche2.ruedas=2                #no puede modificarse ya q fue encapsulado
print(Micoche2.arrancar(False))
#print(Micoche2.__check())        #ya no se puede pedir q imprima un cheqeo por el encapsulamiento

