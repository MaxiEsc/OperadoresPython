#Prestamo Libro
print("*** Sistema de prestamo de Libro ***")

DISTANCIA_PERMITIDA = 3
tiene_credencial = input("Cuantas credencial de estudiante (Si/No)?: ")
distancia_blblioteca_km = int(input("A cuantos kilometros vive de la biblioteca?: "))

print("El prestamo es Aprobado? {}".format(DISTANCIA_PERMITIDA < distancia_blblioteca_km or tiene_credencial.strip().lower() == 'si'))