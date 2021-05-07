print("""               ANSES 
             BECAS 2020""")
edad= int(input("\nQue edad tenes? "))                       #>18 o 25 anos
salario_fam= int(input("\nCual es tu salario familiar? "))   #no superar 40 mil pesos
otraBeca=int(input("\nCobras otra beca? 1 para si, 0 para no: "))

if edad>=18 and edad<25 and salario_fam<40000 or otraBeca==0: # and "y ademas" or "o sino"
	print("\nUsted puede tener una beca")
else:
	print("\nLo sentimos, Usted no puede tener una beca")
	
#.....................................................................
#tranformar un texto de mayuscula a minuscula variable=variable.lower()
#                                                              .upper()









