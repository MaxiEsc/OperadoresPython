#Revisar si la variable esta en el rango de a y b
a,b = 1, 100
c = int(input("Ingrese un nuemero si la variable esta entre 1 y 100: -> "))
print("la variable esta fuera de rango?: {}".format( not ((a<c) and (b>c)) ))