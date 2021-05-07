class veiculo: #creacion de clase(plantilla o molde para creacion de objetos)
    marca=''   #atributos o variables
    modelo=''
    max_vel=0
    
#objetos:
camioneta=veiculo() #hereda de clase veiculo los atributos
camioneta.marca='toyota'
camioneta.modelo='hilux'
camioneta.max_vel=230
#objeto.atributo=valor
auto=veiculo()
auto.marca='chevrolet'
auto.modelo='corsa classic'
auto.max_vel=200

print(camioneta.max_vel)

class Matematicas:
    def suma(self): #metodo es como una funcion// self.nombre de la variable= algoritmo
        self.num=int(input('ingrese un numero a sumar:'))
        self.num2=int(input('ingrese un numero a sumar:'))
#objetos:
operacion=Matematicas()
operacion.suma()
print(operacion.num+operacion.num2)
