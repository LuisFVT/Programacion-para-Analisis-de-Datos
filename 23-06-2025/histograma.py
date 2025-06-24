import matplotlib.pyplot as plt
import numpy as np

datos = np.random.randn(1000)
plt.hist(datos, bins=10000, color='y', edgecolor='black')
plt.title('Histograma de Datos Aleatorios') 
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()
# Este código genera un histograma de datos aleatorios utilizando la biblioteca matplotlib.
