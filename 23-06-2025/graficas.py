import matplotlib.pyplot as plt

# Datos de ejemplo 
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6] 

# Crear el gráfico
plt.plot(x, y, color="Red", marker="o", linestyle="-")

# Personalizar el gráfico
plt.title("Gráfica de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()
