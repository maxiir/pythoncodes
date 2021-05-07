from random import*

valores=[]

def start():
    global valores
    respuesta=input(str('quiere ingresar un valor? ingrese "yes/no": '))
    
    if respuesta=='yes':
        while respuesta=='yes':
            valores.append(randint(0,10))
            print(valores)
            start()
    elif respuesta !='yes':
        print('termino el programa')
        suma=sum(valores)
        print('total de la suma:',suma)
        valores=[]
        exit()

respuesta=input(str('quiere ingresar un valor? ingrese "yes/no": '))

if respuesta=='yes':
    while respuesta=='yes':
        valores.append(randint(0,10))
        print(valores)
        start()

elif respuesta !='yes':
    print('termino el programa')
    suma=sum(valores)
    print('total de la suma:',suma)
    valores=[]
    exit()
    


	



	
	


	

	