
nombres=["maxi","tatiana","nicole","padilla","rucci"]  
#listas se llaman los arrays en phyton es lo mismo a otros lenguajes
print(nombres[:])            
#todos en la lista igual a ":" uno en especifico "el numero de indice"

#para excluir de la lista [0:2], para hacer de atras a adelante se usan indices negativos -
#.......................................................................................
nombres.append("ezequiel")  #append para agregar a la lista se usa append
print(nombres[:])
#.......................................................................................
nombres.insert(2,"pepe") #insert inserta un valor en el indice q desees
print(nombres)
#.......................................................................................
nombres.extend(["m","t","r"]) #extend agrega otra lista o array a continuacion
print(nombres)
#.......................................................................................
print(nombres.index("tatiana")) #index para saber en una lista en que posicion de indice esta el Valor
#.......................................................................................
print("tatiana" in nombres) #in para saber si esta en mi lista sierto valor 
#.......................................................................................
nombres.remove("maxi")
print(nombres[:])      #remove elimina un valor que no queremos en la lista... pop elimina el ultimo valor
nombres.pop()
print(nombres)
#........................................................................................
numeros1=[1,2,3,4,5]
numeros2=[6,7,8,9,10]
numeros3=numeros1+numeros2
print(numeros3)          #juntar dos listas diferentes en una con el +


