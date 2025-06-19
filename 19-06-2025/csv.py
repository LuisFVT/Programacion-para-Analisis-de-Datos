import pandas as pd

# Cargar el archivo CSV
cargar = pd.read_csv("estudiantes.csv")

# Mostrar las primeras filas del DataFrame
print("\n--- Primeras filas del DataFrame ---")
print(cargar.head())

# Mostrar la estructura del DataFrame
print("\n--- Información del DataFrame ---")
print(cargar.info())    

# Ver estadísticas básicas
print("\n--- Estadísticas básicas del DataFrame ---")
print(cargar.describe())

# Mostrar los alumnos con calificación mínima de 70
print("\n--- Alumnos con calificación mínima de 70 ---")
aprobados = cargar[cargar["Calificacion"] >= 70]
print(aprobados)


print ("\n Alumnos que estan en el grupo C --- ")  
grupo_c = cargar[cargar["Grupo"].isin(["C", "c"])]
print(grupo_c)