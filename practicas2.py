class Auto():
    color='rojo'
    puertas=3
    ruedas=4
    marca='chevy'

urbano=Auto()
urbano.color='gris'


class Camioneta():
    def __init__(self): #inicializar/ valores de fabrica en un objeto
        self.__color='azul'
        self.__velocidaMax=230
        self.__marca='toyota' #se encapsula con dos giones delanteros
        self.__traccion='4x4'

miCamioneta=Camioneta()
miCamioneta.__marca='ford'
print(miCamioneta.marca)

print 'mi auto es marca:',urbano.marca,'\n','mi camioneta es traccion:',miCamioneta.traccion
