'''
Created on Apr 26, 2020

@author: griselvargas

Una cadena de hoteles cuenta con 10 filiales y necesita obtener algunas estadísticas para mejorar sus servicios. 
Para ello se ingresan:

Nombre de la ciudad de la filial //String
Capacidad total del hotel (en cuanto a huéspedes) //Int
Cantidad de habitaciones //Int
Cantidad de huéspedes en un mes. //Int

Calcular y mostrar:

Cantidad de huéspedes que puede alojar toda la cadena de hoteles //Capacidades totales 
Porcentaje de ocupación de cada hotel. // Capacidad total vs Cant de huespedes
El nombre de la ciudad con la mayor cantidad de habitaciones. //Mayor

'''

huespedestotales = 0
mayor_hab = 0
hotel_mas_grande = 0

for i in range (0, 10, 1):
    nombre_ciudad = str(input("Nombre de ciudad: "))
    capacidad = int(input("Capacidad total de este hotel? (Cuantos huespedes totales se pueden alojar?): "))
    
    while capacidad == 0:  # Verifico division por cero
        capacidad = int(input("La capacidad no puede ser 0. Ingrese capacidad total del hotel: "))
    
    habitaciones = int(input("Cuantas habitaciones tiene?: "))
    
    while habitaciones == 0:  # Verifico division por cero
        habitaciones = int(input("La cantidad de habitaciones no puede ser 0. Ingrese cantidad de habitaciones: "))
        
    unmes = int(input("Cuantos huespedes tiene en un mes?: "))
            
    while unmes == 0:  # Verifico division por cero
        unmes = int(input("La cantidad de huespedes en un mes no puede ser 0. Ingrese cantidad de huespedes en un mes: "))
    
    if habitaciones > mayor_hab:  # El nombre de la ciudad con la mayor cantidad de habitaciones 
        mayor_hab = habitaciones
        hotel_mas_grande = nombre_ciudad
    
    huespedestotales = huespedestotales + capacidad  # Cantidad de huéspedes que puede alojar toda la cadena de hoteles

    print ("El porcentaje de ocupacion es %.2f" % (((unmes * 100) / capacidad)), chr(37))  # Porcentaje de ocupación de cada hotel
    
# Fuera del ciclo
print("\nLa cantidad de huespedes que puede alojar toda la cadena es %d huespedes" % (huespedestotales))
print("La ciudad con mayor cantidad de habitaciones es %s" % (hotel_mas_grande))
