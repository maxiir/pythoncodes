from random import*
import pandas as pd

diccionario={}

def nuevo():
	for i in range(61):
		nuevodic={ randint(99,999):{'valor':randint(0,99)}}
		diccionario.update(nuevodic)
		df = pd.DataFrame([key for key in diccionario.keys()], columns=['clave'])
		df['valor'] = [value['valor'] for value in diccionario.values()]
	print(df)


nuevo()

print(diccionario['valor'])

