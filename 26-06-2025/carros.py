import matplotlib.pyplot as plt
import pandas as pd     
import numpy as np
import seaborn as sns

datitos = pd.read_excel('carros1.xlsx')

print("Vista previa de los datos:")
print(datitos.head())

print("\n Estadísticas Generales:")
print(datitos["precio"].describe())

ventas_por_marca = datitos.groupby("marca")["precio"].sum().sort_values(ascending=False)
print("\n Ventas Totales por Marca:")   
print(ventas_por_marca)

ventas_por_ciudad = datitos.groupby("ciudad")["precio"].sum().sort_values(ascending=False)
print("\n Ventas Totales por Ciudad:")
print(ventas_por_ciudad)

precio_modelo = datitos.groupby("modelo")["precio"].mean().sort_values(ascending=False)
print("\n Precio Promedio por Modelo:")
print(precio_modelo)

autos_year = datitos["año"].value_counts().sort_index()
print("\n Cantidad de Autos por Año:")
print(autos_year)

precio_promedio= datitos["precio"].mean()
print("\n Precio Promedio de Autos:")
print(precio_promedio)

autos_caros = datitos[datitos["precio"] > precio_promedio]
print(f"Autos con precio mayor al promedio ({precio_promedio:.2f}):")
print(autos_caros)  

plt.figure(figsize=(12, 6))
ventas_por_marca.plot(kind='bar', color='skyblue')
plt.title("Ventas Totales por Marca")
plt.xlabel("Marca")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
ventas_por_ciudad.plot(kind='bar', color='lightgreen')
plt.title("Ventas Totales por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
precio_mayor_promedio = datitos[datitos["precio"] > precio_promedio]
precio_mayor_promedio["modelo"].value_counts().plot(kind='bar', color='coral')
plt.title("Modelos con Precio Mayor al Promedio")
plt.xlabel("Modelo")
plt.ylabel("Cantidad de Autos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

