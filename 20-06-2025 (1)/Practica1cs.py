import pandas as pd

# Cargar el archivo CSV
cargar = pd.read_csv("Practica1.csv")

#Mostrar las 5 primeras filas

print("\n Mostrar las 5 primeras filas--- ")
print("\n", cargar.head(5))


#total de alumnos
print("\n -------Total de alumnos------- ")
total_alumnos = len(cargar)
print (total_alumnos)

#promedio general
print("\n Promedio General ---")
print (cargar ["calificacion"].mean())

#
#---------------filtros--------------

#alumnos con calificación mínima de 70
print("\n Alumnos con Calificación Exacta de 7.0 ---")
minima = cargar[cargar["calificacion"] == 7.0][["nombre", "calificacion"]]
print(minima)


#alumnos del grupo A
print ("\n Alumnos que estan en el grupo A --- ")  
grupo_a = cargar[cargar["grupo"].isin(["A", "a"])]
print(grupo_a)


#alumnos menores de 21
print("\n--- Alumnos menores de 21 años ---")
menores = cargar[cargar["edad"] <= 21]
print(menores)

#---------------Ordenar-------------
#mayor a menor calificación
print("\n -------Alumnos Ordenados de Mayor a Menor en Calificaciones------- ")
print(cargar.sort_values(by="calificacion", ascending=False))


#Si la calificacion es mayor o igual a 70 aprobado
print("\n--- Alumnos con calificación iguales o mayores de 7.0 ---")
aprobados = cargar[cargar["calificacion"] >= 7.0]
print(aprobados)

## Si la calificacion es menor a 70 reprobado
print("\n--- Alumnos con calificación reprobatoria ---")
reprobado = cargar[cargar["calificacion"] <= 6.9]
print(reprobado)
