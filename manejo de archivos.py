from io import open                     #creacion de un archivo de texto 

archivo_texto=open("archivo.txt","w")   #W=escribir, creacion del archivo de texto y le decimos q sea para escribir

escritura="hooolaa mundoo!!!"           #variable con lo q va a decir adentro del archivo txt

archivo_texto.write(escritura)    #modificacion del archivo 

archivo_texto.close()             #cerramos el archivo q modificamos 


print(escritura)