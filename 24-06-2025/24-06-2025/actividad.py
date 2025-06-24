import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Leer el archivo Excel
df = pd.read_excel("Calificaciones_estudiantes.xlsx")

# Mostrar todas las filas en consola (opcional)
print("Todos los estudiantes:")
print(df[['Estudiante', 'Calificación']])

# Gráfica de todos los estudiantes
plt.figure(figsize=(12, 5))  # Aumenta el ancho si hay muchos alumnos
plt.bar(df['Estudiante'], df['Calificación'], color='skyblue')
plt.title("Calificaciones de todos los estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Calificación")
plt.xticks(rotation=90)  # Rota los nombres para que no se encimen
plt.tight_layout()
plt.show()

#Calcular estadísticas descriptivas
# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df['Calificación'].describe())

# son un conjunto de herramientas y medidas que se utilizan para resumir 
# y describir las características principales de un conjunto de datos, sin hacer inferencias o predicciones.
# Histograma con línea de media
plt.figure(figsize=(10, 6))
plt.hist(df['Calificación'], bins=10, color='lightgreen', edgecolor='black')
media = df['Calificación'].mean()
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Media = {media:.2f}')
plt.title("Distribución de calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()


# Verificar valores nulos
print("\nValores nulos por columna:")
print(df[['Estudiante', 'Edad', 'Género', 'Calificación', 'Álgebra', 'Asistencia']].isnull().sum())

# Visualizar los valores nulos con nombres de columnas visibles
plt.figure(figsize=(10, 6))
sns.heatmap(
    df[['Estudiante', 'Edad', 'Género', 'Calificación', 'Álgebra', 'Asistencia']].isnull(),
    cmap='Purples',
    cbar=False,
    yticklabels=False  # Ocultar nombres de filas (registros) para mejor legibilidad
)
plt.title("Mapa de calor de valores nulos", pad=20)  # `pad` ajusta espacio del título
plt.xticks(rotation=45, ha='right')  # Rotar nombres de columnas para mejor visualización
plt.xlabel("Columnas")
plt.ylabel("Registros (filas)")
plt.tight_layout()  # Ajustar diseño para evitar cortes
plt.show()


#Histograma de calificaciones de Algebra
# es un gráfico de barras que muestra cómo se distribuyen 
# los datos numéricos agrupados en rangos (llamados intervalos o bins
print("\nHistograma de calificaciones de Álgebra:")
print(df['Álgebra'].hist())

plt.figure(figsize=(10, 6))
plt.hist(df['Álgebra'], bins=10, color='lightblue', edgecolor='black')
plt.title("Distribución de calificaciones de Álgebra")
plt.xlabel("Calificación de Álgebra")
plt.ylabel("Frecuencia")
plt.grid(axis='y', alpha=0.50)
plt.tight_layout()
plt.show()


#Dispersión entre asistencia y calificaciones

print("\nGráfico de dispersión: Asistencia vs Calificaciones")

# Gráfico básico
plt.figure(figsize=(10, 6))
plt.scatter(
    x=df['Asistencia'],
    y=df['Calificación'],
    color='purple',
    alpha=0.6
)

# Configuración simple
plt.title("Relación Asistencia-Calificaciones")
plt.xlabel("Asistencia (%)")
plt.ylabel("Calificación")
plt.grid(True, linestyle='--', alpha=0.3)

# Ajustar ejes (límites 0-100% para asistencia)
plt.xlim(0, 100)
plt.ylim(0, df['Calificación'].max()+1)

plt.tight_layout()
plt.show()