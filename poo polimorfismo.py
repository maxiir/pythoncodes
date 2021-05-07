class auto():
	def circula(self):
		print("circula con 4 ruedas")

class moto():
	def circula(self):
		print("circula con 2 ruedas")

class camion():
	def circula(self):
		print("circula con 6 ruedas")	

def desplazamiento (vehiculo):         #polimorfismo 
	vehiculo.circula()

#vehiculo=camion()
#vehiculo.circula()

#vehiculo2=auto()
#vehiculo2.circula()                     #todo remplazado por el polimorfismo

#vehiculo3=moto()
#vehiculo3.circula()

Mi_vehiculo=auto()                    #polimorfismo
desplazamiento(Mi_vehiculo)