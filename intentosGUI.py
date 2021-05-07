cont=0
contrasena=str(input('ingrese la contrasena:'))
while contrasena!='maxi1234':
    cont=cont+1
    contrase=str(input('clave incorrecta, ingrese la contrasena:'))
    if contrasena=='maxi1234':
        print('contrasena ingresada con exito!')