print ("Equipo ciclista ganador por tiempo!")


print ("Equipo once: ")

ciclistan1 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 1: "))

                    
ciclistan2 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 2: "))


ciclistan3 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 3: "))


Equipo_once = (ciclistan1 + ciclistan2 + ciclistan3)
Promedio_once = round((ciclistan1 + ciclistan2 + ciclistan3)/3,2)

print ('El teiempo equipo once: ', Equipo_once)
print ( 'promedio: ', Promedio_once)

print ("Equipo saunier: ")

Ciclistan1 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 1: "))

                    
Ciclistan2 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 2: "))


Ciclistan3 = float(input ("Cuanto tiempo ha tardado en recorrer el corredor numero 3: "))


equipo_saunier = (Ciclistan1 + Ciclistan2 + Ciclistan3)
promedio_saunier = round ((Ciclistan1 + Ciclistan2 + Ciclistan3)/3,2)

print ('El teiempo equipo saunier: ', equipo_saunier)
print ('Promedio:', promedio_saunier)

if Equipo_once > equipo_saunier:
    print ('Enorabuena Equipo once es el ganador!!!!', Equipo_once)
if Equipo_once < equipo_saunier:
        print ('Enorabuena Equipo saunier es el ganador!!!!', equipo_saunier)

       
       
