print ('Calculadora con una sola variable\n ')

print ('********************')
print ('* Menu de opciones *')
print ('********************')

print ('''1. Suma
2. Resta
3. multiplicación
4. División
5. División entera
6. Exponente
7. Modulo o resto''')


numero = int(input('\nIntroduce la opcion deseada: '))

if numero == 1:
    numero =int(input ('Introduce el primer numero: '))
    numero +=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 2:
    numero =int(input ('Introduce el primer numero: '))
    numero -=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 3:
    numero =int(input ('Introduce el primer numero: '))
    numero *=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 4:
    numero =int(input ('Introduce el primer numero: '))
    numero /=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 5:
    numero =int(input ('Introduce el primer numero: '))
    numero //=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 6:
    numero =int(input ('Introduce el primer numero: '))
    numero **=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

elif numero == 7:
    numero =int(input ('Introduce el primer numero: '))
    numero %=int( input ('Introduce el segundo numero: ' ))
    print ('Resultado : ', numero)

else:
    print('No existe la opcion elegida')
    
