import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score, accuracy_score

# Cargar datos
datitos = pd.read_excel('carritos.xlsx')

print("Vista previa de los datos:")
print("\nDatos cargados:\n", datitos.head())

# Asegúrate de que la variable objetivo sea binaria (0 y 1)
if datitos['economico'].dtype == object:
    datitos['economico'] = datitos['economico'].map({'Sí': 1, 'No': 0})

# Codificar variables categóricas
datitos_marca = LabelEncoder()
datitos_tranmit = LabelEncoder()

datitos['marca'] = datitos_marca.fit_transform(datitos['marca'])
datitos['transmision'] = datitos_tranmit.fit_transform(datitos['transmision'])

# Definir variables predictoras y objetivo
X = datitos[['marca', 'transmision', 'año', 'kilometraje', 'precio']]
y = datitos['economico']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)

# Evaluar modelo
precision = precision_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"Precisión del modelo: {precision:.2f}")
print(f"Exactitud del modelo: {accuracy:.2f}")
