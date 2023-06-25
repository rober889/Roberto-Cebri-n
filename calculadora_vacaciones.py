#calculador de vacaciones

print('calcular vacaciones empresa')

nombre = input('Por favor, indique su nombre: \n')
clave = int(input('''Por favor indique su harea detrabajo:
\n Indieque el numero del departamento al que
corresponda:\n 1.-atencion al cliente\n 2.-Logistica\n 3.-gerencia \n'''))
años = float(input('Indique los años como empleado: \n'))


if clave == 1:
    if años == 1 and años < 2:
        print (nombre +'\n Le corresponden 6 días de vacaciones.')

    if años >=2 and años <= 6:
               print (nombre + '\n le corresponden 14 dias de vacaciones.')
    if años >= 7:
                      print(nombre +'\n Le corresponden 20 dias de vacaciones.')


elif clave == 2:
    if años == 1 and años < 2:
        print (nombre +'\n Le corresponden 10 días de vacaciones.')

    if años >=2 and años <= 6:
               print (nombre + '\n le corresponden 16 dias de vacaciones.')
    if años >= 7:
                      print(nombre +'\n Le corresponden 28 dias de vacaciones.')


elif clave == 3:
    if años == 1 and años < 2:
        print (nombre +'\n Le corresponden 15 días de vacaciones.')

    if años >=2 and años <= 6:
               print (nombre + '\n le corresponden 24 dias de vacaciones.')
    if años >= 7:
                      print(nombre +'\n Le corresponden 35 dias de vacaciones.')

else:
    print('La clave no existe, vuelve a intentarlo.')

               
