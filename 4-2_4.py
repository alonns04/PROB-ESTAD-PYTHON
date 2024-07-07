import matplotlib.pyplot as plt
import numpy as np

ruta_del_archivo = r'C:\UNI\Materias\Probabilidad y estadística\Prácticas\Suministro.dat'
datos = np.loadtxt(ruta_del_archivo)

datos = sorted(datos.tolist())
print(datos)

lista = [[], [], [], [], [], []]

for dato in datos:
    dato_nuevo = dato
    index = int(dato_nuevo // 1000)
    if index >= 1:
        dato_nuevo = dato_nuevo - (index * 1000)
    lista[index].append(dato_nuevo)

print(datos)
print(lista)

tallos = list(range(len(lista)))

# Crear el gráfico de hojas y tallos
plt.figure(figsize=(10, 6))

for i, hojas in enumerate(lista):
    plt.scatter([tallos[i]] * len(hojas), hojas, marker='o', color='blue')

# Etiquetas y título
plt.xlabel('Tallos')
plt.ylabel('Hojas')
plt.title('Gráfico de Hojas y Tallos')

# Mostrar el gráfico
plt.yticks(np.arange(0, 1001, 50))  # Separar el eje X cada 50 unidades
plt.xticks(np.arange(0, 5, 1))  # Separar el eje Y cada 0.1 unidades
plt.xticks(tallos)
plt.grid(True)