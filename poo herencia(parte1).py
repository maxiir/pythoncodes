class vehiculos():
	
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.marcha=False
		self.frena=False
		self.acelera=False
	
	def enmarcha(self):
		self.marcha=True
	
	def frenada(self):
		self.frena=True
	
	def aceleracion(self):
		self.acelera=True
	
	def caracteristicas(self):
		print(" marca:",self.marca,"\n modelo:",self.modelo, "\n marcha:",self.marcha,"\n frena:",self.frena,"\n acelera:",self.acelera)
	
class moto(vehiculos): #ponemos la clase y de donde heredamos 	
	
	elcaballito=""
	def caballito(self):   #metodo propio de la moto//comportamientos propios		
		self.elcaballito="haciendo caballito"
	def caracteristicas(self):
		print(" marca:",self.marca,"\n modelo:",self.modelo, "\n marcha:",self.marcha,"\n frena:",self.frena,"\n acelera:",self.acelera,"\n",self.elcaballito)	

Mimoto=moto("honda","C90")
#Mimoto.caballito()
Mimoto.caracteristicas()


class camion(vehiculos):          #nueva clase "camion" hereda de la clase "vehiculos"
	def carga (self, carga):
		self.cargar=carga
		if(self.cargar):
			return " el camion esta cargado"
		else:
			return " el camion esta vacio"

miCamion=camion("volvo","78BBT")
miCamion.caracteristicas()
print(miCamion.carga(True))
miCamion.enmarcha()

class VElectricos():
	def __init__(self):
		self.autonomia=100
	
	def CargaDeEnergia(self):
		self.cargando=True
		
class bici_Electrica(vehiculos, VElectricos):  #la nueva clase tiene herencia multiple (dos herencias en una). Siempre la primera herencia es la de mayor importancia	
	pass
	
mibici=bici_Electrica("Fox", "BMX")
	
	
 
	
		
		
	
		
	