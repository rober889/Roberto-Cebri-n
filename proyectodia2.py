#programa para calcular la paga empleado comision 13%

nombre = input('cual es tu nombre? ')
ingresos = float (input('cuanto vendiste: '))
ingresos = round (ingresos * 13 / 100,2)

print(f'{nombre} tu paga es de {ingresos}')