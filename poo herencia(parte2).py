class persona():
	
	def __init__(self, edad, nombre, dni):
		
		self.edad=edad  #edad=edad--> se guarda 
		self.nombre=nombre
		self.dni=dni
		
	def identidad(self):
		print("\nnombre:",self.nombre,"\nedad:",self.edad,"\ndni:",self.dni)
		
class empleado(persona):
	
	def __init__ (self, salario, antiguedad):
		
		self.salario=salario
		self.antiguedad=antiguedad

persona1=persona("23", "maxi", "40.208.871")
persona1.identidad()

print(isinstance(persona1,persona)) #muy util "isinstance()" para saber si un objeto pertenece o no a la clase q se le indica por la herencia
		
		
		 
		
	
	