import pandas as pd



def nuevoRE():
	
	nuevoDATO={input("nombre: "):{"numero":input("numero: ")}}
	dataBase.update(nuevoDATO) #.update() extiende el diccionario antes creado con lo nuevo
	
	df = pd.DataFrame([key for key in dataBase.keys()], columns=['Nombre'])
	df['numero'] = [value['numero'] for value in dataBase.values()]
		
	respuesta=str(input("desea agregar otro dato? s/n: \n"))
	
	while respuesta=='s':
		nuevoRE()
	else:
		print("\n\nDATOS ALMACENADOS EN LA BASE DE DATOS:\n\n",df)
		exit()


#---------------------------------------------------------------------------------#

dataBase={input("nombre: "):{"numero":input("numero: ")}}

df = pd.DataFrame([key for key in dataBase.keys()], columns=['Nombre'])
df['numero'] = [value['numero'] for value in dataBase.values()]

respuesta=str(input("desea agregar otro numero? s/n: \n"))

while respuesta=='s':
	nuevoRE()
else:
	print("\n\nDATOS ALMACENADOS EN LA BASE DE DATOS:\n\n",df)
	exit()
	



