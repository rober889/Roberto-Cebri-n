#conjunción (se tienen que cumplir las 2 si no ejecuta else.)

print ('conjuncion (and)')

num_uno = int(input('Escribe un número mayor a 2 y menos a 5: '))

if num_uno > 2 and num_uno < 5:
    print("el numero ", num_uno, "cumple con la condicion.\n")
else:
    print ('No cumple con la condicion.\n')

#Disyunción (se ejecuta una o otra)
print ('Disyunción (or)')

palabra =  input("Para cumplir con la condicion escribe 'si' o 'no': ")

if palabra == 'si' or palabra == 'no':
    print ('\nla coindicion se ha cumplido.\n')
else:
    print ( 'la condicion NO se ha cumplido.\n')
    
#Negacion (si no es igual a...)
print ('negacion (not)')

if not num_uno == 5:
    print('\n El numero es diferente de cinco y SI cumple la condicion.\n')
else:
    print ('\n el numero es igual a cinco y no cumple la condicion.')

print('fin.')
