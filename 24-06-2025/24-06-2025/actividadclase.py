import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns   

# Cargar los datos
cargar = pd.read_excel("Calificaciones_estudiantes.xlsx")

# Estadísticas descriptivas
print(cargar.describe())

# Conteo de valores nulos por columna
print(cargar.isnull().sum())

# Histograma de Calificaciones
plt.hist(cargar['Calificación'], bins=50, color='lightgreen', edgecolor='black')
plt.title("Distribución de Calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")

# Boxplot de Calificaciones por Género
sns.boxplot(x='Género', y='Calificación', data=cargar, hue='Género')
plt.title("Calificaciones por Género")
plt.show()

# Gráfico de dispersión de Calificaciones vs Asistencia
sns.scatterplot(x='Asistencia', y='Calificación', data=cargar, hue='Género')
plt.title("Calificaciones vs Asistencia")
plt.xlabel("Asistencia (%)")
plt.ylabel("Calificación")
plt.show()  

#mapa de calor 
plt.figure(figsize=(10, 6))
sns.heatmap(
    cargar.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=.5,
    cbar_kws={"shrink": .8}
)   
plt.title("Mapa de Calor de Correlaciones")
plt.show()  

