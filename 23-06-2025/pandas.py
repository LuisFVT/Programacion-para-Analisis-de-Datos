import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('datos.xlsx')

datitos = df["valores"].dropna()

media= np.mean(datitos)
desviacion = np.std(datitos)

plt.hist(datitos, bins=30, color='blue', edgecolor='black', alpha=0.5)
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')

plt.axvline(media + desviacion, color='green', linestyle='dotted', linewidth=2, label=f'+1 Desviación: {media + desviacion:.2f}')
plt.axvline(media - desviacion, color='green', linestyle='dashed', linewidth=2, label=f'-1 Desviación: {media - desviacion:.2f}')
plt.title('Histograma de Valores')

plt.title('Histograma de Valores')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')    
plt.legend()
plt.show()
