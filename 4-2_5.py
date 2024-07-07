import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo
ruta_del_archivo = r'C:\UNI\Materias\Probabilidad y estadística\Prácticas\Carbon.dat'

# Leer los datos del archivo .dat
# Asumiendo que el archivo está separado por espacios y tiene una estructura similar a la proporcionada
data = pd.read_csv(ruta_del_archivo, delim_whitespace=True)

# Mostrar los datos leídos
print(data)
co2 = sorted((data['CO2'].values).tolist())
bins = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(co2)

# Realizar los cálculos requeridos
max_value = data['CO2'].max()
min_value = data['CO2'].min()
mean_value = data['CO2'].mean()
median_value = data['CO2'].median()
mode_value = data['CO2'].mode()[0]
std_dev = data['CO2'].std()
quartiles = data['CO2'].quantile([0.25, 0.5, 0.75])

# Mostrar los resultados
print(f"Valor máximo: {max_value}")
print(f"Valor mínimo: {min_value}")
print(f"Media: {mean_value}")
print(f"Mediana: {median_value}")
print(f"Moda: {mode_value}")
print(f"Desvío estándar: {std_dev}")
print(f"Cuartiles: {quartiles}")

# Histograma
plt.hist(co2, bins = bins, edgecolor='black')
plt.xlabel('Emisiones de CO2 (millones de toneladas)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Emisiones de CO2')
plt.grid()
plt.show()

# Crear el diagrama de caja
plt.figure(figsize=(10, 6))
plt.boxplot(co2, vert=False, patch_artist=True)

# Configurar las etiquetas y el título
plt.title('Diagrama de Cajas de Emisiones de CO2 en Países Europeos')
plt.xlabel('Emisiones de CO2 (millones de toneladas)')

# Mostrar el diagrama de caja
plt.grid(True)
plt.show()

print((co2[7]+co2[8])/2)
print((co2[15+7]+co2[15+8])/2)
