class Calculadora():
    def operaciones(self,num,num2):
        self.suma=num+num2
        self.resta=num-num2

operacion=Calculadora()
operacion.operaciones(12,40)
print(operacion.resta)


num=12
num2=30
print(num+num2)


def sumas(num,num2):
    return num+num2
print(sumas(76,233))

suma=lambda a,b:a+b
print(suma(12,2))