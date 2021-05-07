 
import pandas as pd

cambio=0
total=0
total2=0
def algomas():
	codigoNUEVO=int(input("codigo del producto: "))
	for i in precios:
		if i==codigoNUEVO:
			total2=precios.get(codigoNUEVO)+total
			
				
	print("-le sale:",total2)
	respuesta2=str(input("*algo mas? s/nn: "))
	while respuesta2=='s':
		algomas()
	else:
		pago=int(input("dinero: "))
		cambio=pago-total2
		print("su cambio:",cambio)
		exit()


#------------------------------------------------------------------------------#


productos={
	"codigo":[2234,2345,7553,5578],
	"producto":["cerveza","harina","leche","yogurt"],
	"cantidad":[1000,1500,5000,2000],
	"valor":[230,60,100,90] }

precios={2234:230,
2345:60,
7553:100,
5578:90 }
	
df=pd.DataFrame(productos)
print(df)

codigo=int(input("codigo del producto: "))
for i in precios:
	if i==codigo:
		total=precios.get(codigo)
		
print("-le sale:",total)

respuesta=str(input("*algo mas? s/n: "))

while respuesta=='s':
	algomas()
	
else:
	pago=int(input("ingrese el dinero:"))
		
	for i in precios:
		if i==codigo:
			cambio=pago-precios.get(codigo)
	print("su cambio:",cambio)
	exit()

#for i in productos["codigo"]:
#	if i==codigo:
#		codigo=precios
#		print(productos["valor"][3])
		
		
					
	