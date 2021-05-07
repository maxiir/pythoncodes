#promedios de una lista de valores al azar

from random import*

MIlista=[]

def prom(MIlista):
	suma=0
	for i in MIlista:
		suma=suma+i    #+i suma el siguiente valor 
		prom=suma/cont
	return prom

cont=0
for i in range(999999):
	MIlista.append(randint(0,999999))
	cont=cont+1
	if cont==999999:
		print("Promedio de los valores:", prom(MIlista))

print(MIlista)