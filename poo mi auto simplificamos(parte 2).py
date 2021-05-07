class Autos():
	
	def __init__(self):          #(__init__)contructor----> da esas caracteristicas mensionadas por defecto(iniciales)
	    self.ruedas=4
	    self.puertas=5                        #propiedades de la clase ---> las caracteristicas de los objetos
	    self.color='black'
	    self.encendido=False
	
	def arrancar(self, arrancamos):                              
		self.encendido=arrancamos              #ya no se fija lo q dice la clase sino el parametro q yo le indico
		if (self.encendido):                   #si encendido es "true" entonces.....
			return "el coche esta encendido"
		else:
			return "el coche esta apagado"
		
		
	def caracteristicas(self):                     #muestra todas las caracteristicas del objeto q esta en la clase
		print("el auto tiene ",self.ruedas,"ruedas",self.puertas,"puertas y es color:",self.color)



Micoche=Autos()   #objeto creado y nombre a la clase q pertenece *comienza la programacion para ese objeto creado*//ya tienen un estado inicial o de fabrica

Micoche.caracteristicas()
print(Micoche.arrancar(True))                                   #muestra en pantalla como se encuentra el objeto

print("\n************************************CREACION DEL 2do OBJETO*******************************************\n")

Micoche2=Autos()         #ya cree el 2do objeto

Micoche2.caracteristicas()       #no es necesario poner un print para las caracteristicas ya q en el metodo se pone
print(Micoche2.arrancar(False))

print("\n************************************CREACION DEL 3ro OBJETO********************************************\n")

Micoche3=Autos()
Micoche3.puertas=6
print("el auto tiene:",Micoche3.puertas,"puertas")   #con el punto "." accedes a las caracteristicas de una clase

