import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [5,8,9,8]

plt.bar(categorias, valores, color='blue')
plt.title('Diagrama de barras')

plt.xlabel('Categorías')
plt.ylabel('Valores')       

plt.show()
# Este código crea un diagrama de barras con las categorías A, B, C y D
# y sus respectivos valores 5, 8, 9 y 8. El diagrama se muestra en color azul.
# El título del diagrama es "Diagrama de barras" y los ejes están etiquetados
# como "Categorías" y "Valores". Finalmente, se muestra el diagrama con plt     

