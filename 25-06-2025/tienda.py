import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np  
import seaborn as sns

sns.set(style="darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

datitos = pd.read_excel("tienda.xlsx")

datitos['Fecha'] = pd.to_datetime(datitos['Fecha'])
datitos['Mes'] = datitos['Fecha'].dt.to_period('M')

#ingresos por productos
top_productos = datitos.groupby('Producto')['Ingresos'].sum().sort_values(ascending=False).head(10)
top_productos.plot(kind='bar', color='skyblue')
plt.title('Top 10 Productos por Ingresos')
plt.xlabel('Producto')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#ingresos por cuidad
ingresos_ciudad = datitos.groupby('Ciudad')['Ingresos'].sum().sort_values(ascending=False)
ingresos_ciudad.plot(kind='bar', color='lightcoral')    
plt.title('Ingresos por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Agrupa los datos por la columna 'Mes' y suma los ingresos de cada mes
ingresos_mes = datitos.groupby("Mes")['Ingresos'].sum()
ingresos_mes.plot(marker='o', color='purple', linestyle='-',title='Ingresos Mensuales')

plt.ylabel('Ingresos')

plt.show()

#metodos de pago
metodos_pago = datitos['Método de Pago'].value_counts()
metodos_pago.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Distribución de Métodos de Pago')
plt.ylabel('')
plt.tight_layout()
plt.show()

