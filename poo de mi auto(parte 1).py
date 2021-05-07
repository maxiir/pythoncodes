class Autos():
	ruedas=4
	puertas=5                        #propiedades de la clase ---> las caracteristicas del objeto
	color='black'
	encendido=False
	
	def arrancar(self):                               # def ---> metodos "lo q puede hacer el objeto *comportamientos de la clase*
		self.encendido=True
	def estado(self):
		if(self.encendido):                           #'self' hace de puente para interactuar entre metodo(funcion) y propiedades de clase
			return "el auto esta encendido"
		else:
			return "el auto esta apagado"



Micoche=Autos()   #objeto creado y nombre a la clase q pertenece *comienza la programacion para ese objeto creado*
print("el auto tiene:",Micoche.ruedas, "ruedas")                #muestra en pantalla una propiedad de objeto mi coche
Micoche.arrancar()                                             #hago una llamada para realizar ese metodo
print(Micoche.estado())                                   #muestra en pantalla el estado del metodo "estado"
print("el auto tiene", Micoche.puertas,"puertas")

print("************************************CREACION DEL 2do OBJETO*******************************************")

Micoche2=Autos()         #ya cree el 2do objeto
print("mi 2do auto tiene:" ,Micoche2.ruedas, "ruedas")
