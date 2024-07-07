import matplotlib.pyplot as plt

# Datos
data = [100.0, 240.0, 340.0, 360.0, 396.0, 450.0, 500.0, 510.0, 530.0, 540.0, 960.0, 960.0, 1000.0, 1050.0, 1120.0, 1240.0, 1250.0, 1280.0, 1320.0, 1419.0, 1670.0, 1850.0, 1890.0, 2100.0, 2109.0, 2120.0, 2250.0, 2320.0, 2400.0, 2400.0, 2460.0, 2700.0, 2730.0, 3060.0, 3150.0, 3150.0, 3330.0, 3350.0, 3380.0, 3870.0, 4390.0, 4770.0, 5220.0, 5320.0, 5700.0, 5770.0, 5850.0]

# Definir los límites de los intervalos
bins = range(0, int(max(data) + 1000), 1000)

# Crear el histograma
plt.hist(data, bins=bins, edgecolor='red')

# Configurar las etiquetas y títulos
plt.xlabel('Intervalo')
plt.ylabel('Frecuencia')
plt.title('Histograma con intervalos de 1000 unidades')
plt.grid()
plt.yticks(range(0, int(max(plt.hist(data, bins=bins, edgecolor='black')[0])) + 1))


# Mostrar el histograma
plt.show()
