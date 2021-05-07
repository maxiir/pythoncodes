import pickle

lista_nombre=["maxi","tatiana","rucci","padilla"]

fichero_binario=open("lista_nombre","wb")        #la "b" significa binario para crear ficheros en binario

pickle.dump(lista_nombre,fichero_binario)        #dump() vuelca toda la informacion de la lista en el archivo. sus parametros necesarios son nombre de archivo donde esta la informacion a volcar y nombre del archivo al q se va a volcar esa informacion 

fichero_binario.close()

#para rescatar un archivo codificado se utiliza .load()