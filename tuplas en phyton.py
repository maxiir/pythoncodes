nombre=("pepe","pepino","pepino","pelele")  #esta en formato de tupla(), no se puede modificar nada 
print(nombre)
#................................................
nombres=list(nombre)
print(nombres) #convierto la tupla en lista con "list" para lograr lo inverzo se pone "tuple"
#.................................................
print(nombre.count("pepino")) #count contar cuantas veces aparece sierto elemento en la tupla
#.................................................
print(len(nombre)) #te dice cuantos valores estan en la tupla
#.................................................
fecha=(22,"abril",1997)  #desempaquetar tumplas asignando categoria
dia,mes,ano=fecha
print(ano)
print(mes)
print(dia)



