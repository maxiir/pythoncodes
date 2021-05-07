class auto():
	
	tipo="deportivo"
	interior="blanco"
	ruedas=4
	puertas=5
	color="negro"
	encendido=False
	
	def estadoV (self,arrancar):
		encendido=arrancar
		if encendido==True:
			return "* Esta en marcha *"
		else:
			return "* Esta apagado *"
	
	def caracteristicas(self):
		print("tipo:",self.tipo,"\ninterior:",self.interior,"\nruedas:",self.ruedas,"\npuertas:",self.puertas,"\ncolor:",self.color)
		
class camion():
	
	TipoRuedas="todo terreno"
	puertas=2
	CantRuedas=6
	color="rojo"
	cargado=False
	
	def cargamento (self,cargar):
		cargado=cargar
		if cargado==True:
			return "* Esta lleno *"
		else:
			return "* Esta vacio *"
	
	def caracteristicas(self):
		print("Tipo de ruedas:",self.TipoRuedas,"\nPuertas:",self.puertas,"\ncantidad de ruedas:",self.CantRuedas,"\nColor:",self.color)
		

	
print("           AUTO")	
miAuto=auto()
print(miAuto.estadoV(False))
miAuto.caracteristicas()

print("\n         CAMION")
miCamion=camion()
print(miCamion.cargamento(False))
miCamion.caracteristicas()


class auto_de_carreras(auto):	
	print("\n      AUTO DE CARRERAS")

autoCarreras=auto_de_carreras()
print(autoCarreras.estadoV(True))
autoCarreras.caracteristicas()
	
	

