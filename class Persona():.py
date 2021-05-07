from random import random


import random
'''
class Persona():
    
    def estado(self,mts):                    #comportamiento del objeto==metodo/funcion
        if self.caminar==True:
            print('esta caminando')
            def calorias(self,mts):
                if self.mts==50:
                    return 'quemo 12 calorias'
                elif self.mts==100:
                    return 'quemo 24 calorias'
                else:
                    return 'no quemo calorias'
        else:
            print('esta quieta/o')
            


    def mover(self):                     #comportamientos del objeto
        self.caminar=True
    
    nombre=''                            #atributos de la clase estos vienen por defecto para todos los objetos
    edad=0
    apellido=''
    pais=''
    caminar=False
   

#self almacena el objeto en los metodos self==objeto
mujer=Persona()                       #se crea el objeto 'mujer'
mujer.nombre='Pamela'
mujer.edad=23
mujer.apellido='lopez'
mujer.pais='mexico'
mujer.mover()


hombre=Persona()
#hombre.mover()

print ("estado de la mujer:",mujer.estado(50))
#print('calorias m quemadas:',mujer.calorias(100))
#print('calorias h quemadas:',hombre.estado(),hombre.calorias(50))

'''










palabra=['la','le','li','lo','lu','sa','se','si','so','su','pa','pe','pi','po','pu','ra','re','ri','ro','ru','ya','ye','yi','yo','yu','da','de','di','do','du','na','ne','ni','no','nu','va','ve','vi','vo','vu','ta','te','ti','to','tu','ma','me','mi','mo','mu','fa','fe','fi','fo','fu','ga','ge','gi','go','gu','za','zo','ha','he']
palabra_full=''


for i in range(3):
    palabra_full=palabra_full+random.choice(palabra)
print(palabra_full)






