import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta del archivo CSV
ruta_del_archivo = r'C:\UNI\Materias\Probabilidad y estadística\Prácticas\tiempo_respuesta.csv'

# Leer los datos del archivo CSV
# Leer los datos del archivo CSV
data = pd.read_csv(ruta_del_archivo, header=None, names=['Category', 'Value'])

# Filtrar y guardar los datos que dicen "A"
a_values = data[data['Category'] == 'A']['Value'].tolist()

# Filtrar y guardar los datos que dicen "B"
b_values = data[data['Category'] == 'B']['Value'].tolist()

a_values = [int(x) for x in a_values]
b_values = [int(x) for x in b_values]

# Imprimir los resultados
print("Valores para A:", a_values)
print("Valores para B:", b_values)
# Histograma
plt.figure(figsize=(10, 6))
plt.hist(a_values, bins=10, edgecolor='black')

# Configurar las etiquetas y el título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores para A')

# Mostrar el histograma
#plt.show()# Histograma


plt.figure(figsize=(10, 6))
plt.hist(b_values, bins=10, edgecolor='black')

# Configurar las etiquetas y el título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores para B')

# Mostrar el histograma
#plt.show()


plt.figure(figsize=(10, 6))
plt.boxplot(a_values, vert=False, patch_artist=True)

# Configurar las etiquetas y el título

# Mostrar el diagrama de caja
plt.grid(True)
#plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot(b_values, vert=False, patch_artist=True)

# Configurar las etiquetas y el título

# Mostrar el diagrama de caja
plt.grid(True)
#plt.show()


plt.figure(figsize=(10, 6))
plt.boxplot(a_values)
plt.xlabel('Conjunto de datos')
plt.ylabel('Valor')
plt.title('Diagrama de cajas de a_values')
plt.grid(True)
#plt.show()


plt.figure(figsize=(10, 6))
plt.boxplot(b_values)
plt.xlabel('Conjunto de datos')
plt.ylabel('Valor')
plt.title('Diagrama de cajas de b_values')
plt.grid(True)
#plt.show()

varianza_a = np.var(a_values)
varianza_b = np.var(b_values)

print(varianza_a)
print(varianza_b)
"""
media = sum(a_values)/len(a_values)

suma = 0

for value in a_values:
    suma += (value - media)**2

varianza_a_calculada = suma / len(a_values)

print(varianza_a_calculada)
"""